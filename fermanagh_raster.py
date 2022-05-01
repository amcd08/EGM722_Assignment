import geopandas as gpd
import rasterio as rio
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
from rasterio import mask
import numpy as np
from rasterstats import zonal_stats


counties = gpd.read_file('data_files/Counties.shp')
fermanagh_gdf = counties[counties['CountyName'] == 'FERMANAGH']
shape = fermanagh_gdf['geometry']

with rio.open('data_files/lcm2015ni25mfinal_UTM.tif') as dataset:
    xmin, ymin, xmax, ymax = dataset.bounds
    crs = dataset.crs
    landcover = dataset.read(1)
    out_image, out_transform = rio.mask.mask(dataset, shape, crop=True)
    out_meta = dataset.meta
    out_meta.update({
    "driver": 'Gtiff',
    'height':out_image.shape[1],
    'width':out_image.shape[2],
    'transform': out_transform
})
dst = rio.open('data_files/output/fermlandclass25m.tif', 'w', **out_meta)
dst.write(out_image)
dst.close()

