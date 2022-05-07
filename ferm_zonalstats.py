import matplotlib.pyplot as plt
import numpy as np
import rasterio as rio
from rasterio.plot import show, show_hist
plt.rcParams.update({'font.size': 16})

#read the Fermamagh land class 25m raster
dataset = rio.open('data_files/output/fermlandclass25m.tif')
print(dataset.crs)
landcover = dataset.read(1)
affine_tfm = dataset.transform

#show(dataset, cmap = "Paired", title = 'Land Cover, Fermanagh')
#show_hist(dataset, bins=50, title = 'Land Cover, Fermanagh')

#define the function to return the no of pixels of each land class
def count_unique(array, nodata=0):
    count_dict = {}
    for val in np.unique(array):
        if val == nodata:
            continue
        count_dict[str(val)] = np.count_nonzero(array == val)
    return count_dict

unique_landcover = count_unique(landcover)
print(unique_landcover)

#assign names to landclass values

def rename_dict(dict_in, old_names, new_names):
    '''
    Rename the keys of a dictionary, given a list of old and new keynames

    :param dict_in: the dictionary to rename
    :param old_names: a list of old keys
    :param new_names: a list of new key names

    :returns dict_out: a dictionary with the keys re-named
    '''
    dict_out = {}
    for new, old in zip(new_names, old_names):
        try:
            dict_out[new] = dict_in[old]
        except KeyError:
            continue
    return dict_out

old_names = [float(i) for i in range(1, 22)]
new_names = ['Broadleaved woodland','Coniferous Woodland','Arable and horticulture','Improved Grassland','Neutral Grassland','Calcareous Grassland','Acid grassland','Fen, Marsh, Swamp',
'Heather','Heather grassland','Bog','Inland Rock','Saltwater','Freshwater','Supra-littoral Rock','Supra-littoral sediment','Littoral Rock','Littoral sediment',
'Saltmarsh','Urban','Suburban']

rename_dict(count_dict, old_names, new_names)

