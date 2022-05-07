import geopandas as gpd
import rasterio as rio
from rasterio import mask


#mask the NI Mosaic tif to County Fermanagh
counties = gpd.read_file('data_files/Counties.shp')
fermanagh_gdf = counties[counties['CountyName'] == 'FERMANAGH']
shape = fermanagh_gdf['geometry']

with rio.open('data_files/NI_Mosaic.tif') as dataset:
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
dst = rio.open('data_files/output/fermosaic.tif', 'w', **out_meta)
dst.write(out_image)
dst.close()#the close statement is needed to write the new tif to file