import rasterio as rio
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import numpy as np
plt.ion() # make the plotting interactive

dataset = rio.open('data_files/output/fermosaic.tif')

print('image has {} band(s)'.format(dataset.count))
print(dataset.crs)

img = dataset.read()#loads the raster data
xmin, ymin, xmax, ymax = dataset.bounds

myCRS = ccrs.UTM(29) # note that this matches with the CRS of our image
fig, ax = plt.subplots(1, 1, figsize=(10, 10), subplot_kw=dict(projection=myCRS))


#percentile stretch returns to best results to display the background mosaic
def percentile_stretch(image, pmin=0., pmax=100.):
    '''
    Display a raster with the percentile stretch contrast applied

    :param image: the raster to be displayed
    :param pmin: default min value is set to 0%
    :param pmax: default max value is set to 100%
    :return: the percentile stretch is applied when the image is displayed
    '''

    # ensure that pmin < pmax, and that they are between 0 and 100%
    if not 0 <= pmin < pmax <= 100:
        raise ValueError('0 <= pmin < pmax <= 100')
    # here, we make sure that the image is only 2-dimensional
    if not image.ndim == 2:
        raise ValueError('Image can only have two dimensions (row, column)')

    minval = np.percentile(image, pmin)
    maxval = np.percentile(image, pmax)

    stretched = (image - minval) / (maxval - minval)  # stretch the image to 0, 1
    stretched[image < minval] = 0  # set anything less than minval to the new minimum, 0.
    stretched[image > maxval] = 1  # set anything greater than maxval to the new maximum, 1.

    return stretched


def img_display(image, ax, bands, transform, extent, pmin=0, pmax=100):
    '''
 scales an image to have values between 0 and 1 and re-orders the indices for display in imshow

    :param image: the image to be displayed
    :param ax: the axis of the plot
    :param bands: the number of bands
    :param transform: the transform of the image
    :param extent: the image extent or bounds
    :param pmin: default value of 0
    :param pmax: default value of 1
    :return: the image has a scalar floating point value; indices are ordered in rows, columns, bands
    '''

    dispimg = image.copy().astype(np.float32)  # make a copy of the original image,
    #cast it as a floating-point image, rather than an integer

    for b in range(image.shape[0]):  # loop over each band, stretching using percentile_stretch()
        dispimg[b] = percentile_stretch(image[b], pmin=pmin, pmax=pmax)

    # next, we transpose the image to re-order the indices
    dispimg = dispimg.transpose([1, 2, 0])

    # finally, we display the image
    handle = ax.imshow(dispimg[:, :, bands], transform=transform, extent=extent)

    return handle, ax
h, ax = img_display(img, ax, [2, 1, 0], myCRS, [xmin, xmax, ymin, ymax], pmin=0.1, pmax=99.9)


background = dataset.read() #sets the Co. Fermanagh mosaic as background

bg, ax = img_display(background, ax, [2, 1, 0], myCRS, [xmin, xmax, ymin, ymax], pmin=0.1, pmax=99.9)

#open the Fermanagh land class raster and display land class 11, Bog
with rio.open('data_files/output/fermlandclass25m.tif') as src:
    xmin, ymin, xmax, ymax = src.bounds
    landcover = src.read(1)
    affine_tfm = src.transform

#using the numpy masked arrays (ma) function, mask all landclsses iexcept lc 11 (Bog)
ax.imshow(np.ma.masked_not_equal(landcover, 11), cmap='autumn', transform=myCRS, extent=[xmin, xmax, ymin, ymax])
ax.set_title('Areas of bog in Co Fermanagh')

