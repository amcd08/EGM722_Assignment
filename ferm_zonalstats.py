import numpy as np
import rasterio as rio
import geopandas as gpd
import matplotlib.pyplot as plt
from rasterstats import zonal_stats
plt.rcParams.update({'font.size': 22})

#read the Fermamagh land class 25m raster
dataset = rio.open('data_files/output/fermlandclass25m.tif')
print(dataset.crs)
landcover = dataset.read(1)
affine_tfm = dataset.transform

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


#generate 3km buffer around the schools
schools = gpd.read_file('data_files/schoolF_points.shp')
type(schools['geometry'])
buffer3km_sch = schools['geometry'].buffer(distance=3000)
buffer3km_sch.to_file('buffer3kmfsch.shp')
sch3 = gpd.read_file('buffer3kmfsch.shp')

#generate the occurence of differernt land classes within 3km of each school
buffer_stats = zonal_stats(sch3, landcover, affine=affine_tfm, categorical=True, nodata=0)
print(buffer_stats[0])