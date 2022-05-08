import matplotlib.pyplot as plt
import numpy as np
import rasterio as rio
from rasterio.plot import show

def read_land_class_file(land_class_file):
    '''
    Read the first dataset from a landclass file

    :param land_class_file: the landclass tif file
    :return: the first dataset in the landclass tif file and the CRS

    '''
    dataset = rio.open(land_class_file) #parameter is the file path
    land_cover = dataset.read(1)
    return land_cover, dataset


def count_unique(array, nodata=0):
    '''
    Get the number of pixels of each land class

    :param array: array of the raster dataset
    :param nodata: indicates the value that represents no data. Default = 0.
    :return: A dictionary containing a count of the number of pixels of each land class.
    '''
    count_dict = {}
    for val in np.unique(array):
        if val == nodata:
            continue
        count_dict[str(val)] = np.count_nonzero(array == val)
    return count_dict


def rename_dict(dict_in, new_names):
    '''
    Rename the keys of a dictionary, given a list of new keynames

    :param dict_in: the dictionary to rename
    :param new_names: a list of new key names

    :returns dict_out: a dictionary with the keys re-named
    '''
    old_names = unique_land_cover.keys()
    dict_out = {}
    for new, old in zip(new_names, old_names):
        try:
            dict_out[new] = dict_in[old]
        except KeyError:
            continue
    return dict_out


new_names = ['Broadleaved woodland','Coniferous Woodland','Arable and horticulture','Improved Grassland','Neutral Grassland','Calcareous Grassland','Acid grassland','Fen, Marsh, Swamp',
'Heather','Heather grassland','Bog','Inland Rock','Saltwater','Freshwater','Supra-littoral Rock','Supra-littoral sediment','Littoral Rock','Littoral sediment',
'Saltmarsh','Urban','Suburban']


#read the Fermamagh land class 25m raster
land_cover, land_cover_dataset = read_land_class_file('data_files/output/fermlandclass25m.tif')
print(land_cover_dataset.crs)
unique_land_cover = count_unique(land_cover)
print(unique_land_cover)

#assign names to landclass values and print results
named_count_unique = rename_dict (unique_land_cover, new_names)

#print land class and pixel count as table
print("{:<40} {:>15} {:>15}".format('Land class', 'Pixel Count', 'Area(ha)'))
for key, val in named_count_unique.items():
    area = int((val*25*25)/10000)
    print("{:<40} {:>15} {:>15}".format(key, val, area))

#display the Co Fermanagh raster showing the land classes by colour
plt.rcParams.update({'font.size': 10})
show(land_cover_dataset, cmap = "Paired", title = 'Land Cover, Fermanagh')

