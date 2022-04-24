import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
from cartopy.feature import ShapelyFeature
import cartopy.crs as ccrs
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
import pandas as pd
from shapely.geometry import Point

plt.ion() # make the plotting interactive

# generate matplotlib handles to create a legend of the features we put in our map.
def generate_handles(labels, colors, edge='k', alpha=1):
    lc = len(colors)  # get the length of the color list
    handles = []
    for i in range(len(labels)):
        handles.append(mpatches.Rectangle((0, 0), 1, 1, facecolor=colors[i % lc], edgecolor=edge, alpha=alpha))
    return handles

# create a scale bar of length 20 km at the bottom of the map
def scale_bar(ax, location=(0.5, 0.05)):
    llx0, llx1, lly0, lly1 = ax.get_extent(ccrs.PlateCarree())
    sbllx = (llx1 + llx0) / 2
    sblly = lly0 + (lly1 - lly0) * location[1]

    tmc = ccrs.TransverseMercator(sbllx, sblly)
    x0, x1, y0, y1 = ax.get_extent(tmc)
    sbx = x0 + (x1 - x0) * location[0]
    sby = y0 + (y1 - y0) * location[1]

    plt.plot([sbx, sbx - 20000], [sby, sby], color='k', linewidth=9, transform=tmc)
    plt.plot([sbx, sbx - 10000], [sby, sby], color='k', linewidth=6, transform=tmc)
    plt.plot([sbx-10000, sbx - 20000], [sby, sby], color='w', linewidth=6, transform=tmc)

    plt.text(sbx, sby-2500, '20 km', transform=tmc, fontsize=8)
    plt.text(sbx-10500, sby-2500, '10 km', transform=tmc, fontsize=8)
    plt.text(sbx-20500, sby-2500, '0 km', transform=tmc, fontsize=8)

myFig = plt.figure(figsize=(10, 10))  # create a figure of size 10x10 (representing the page size in inches)

myCRS = ccrs.UTM(29)  # create a Universal Transverse Mercator reference system to transform our data.

ax = plt.axes(projection=ccrs.Mercator())  # create an axes object using a Mercator projection

#import text file of school locations
df = pd.read_csv('data_files/FermSchl_l.txt')
df.head()
#assign point geometry to the dataframe
df['geometry'] = list(zip(df['lon'], df['lat'])) # zip is an iterator, so we use list to create
df['geometry'] = df['geometry'].apply(Point)
df
#convert df to GDF and assign CRS UTM29
gdf = gpd.GeoDataFrame(df)
gdf.set_crs("EPSG:4326", inplace=True) # this sets the coordinate reference system to epsg:4326, wgs84 lat/lon

gdf = gdf.to_crs(epsg=32629)
gdf

#convert to points shapefile and import
gdf.to_file('schoolF_points.shp')
myshcs = gpd.read_file('data_files/schoolF_points.shp')
print(myshcs.head())


#plot the point shapefile in matplotlib axis
sch_handle = ax.plot(myshcs.geometry.x, myshcs.geometry.y, 's', color='b', ms=7, transform=myCRS)

#import the Assis_Fermanagh shapefile and create geometry col using geppandas
assis_ferm = gpd.read_file('data_files/Assis_Fermanagh.shp')
#print(assis_ferm.head())

assisferm_feat = ShapelyFeature(assis_ferm['geometry'], myCRS, edgecolor='k', facecolor='w')
xmin, ymin, xmax, ymax = assis_ferm.total_bounds

# using the boundary of the shapefile features, zoom the map to our area of interest
ax.set_extent([xmin, xmax, ymin, ymax], crs=myCRS) # because total_bounds gives output as xmin, ymin, xmax, ymax,
# but set_extent takes xmin, xmax, ymin, ymax, we re-order the coordinates here.


#get the number of ASSI types and assign a colour to each
num_types = len(assis_ferm.Type.unique())
print('Number of unique features: {}'.format(num_types)) # note how we're using {} and format here!
assi_colors = ['forestgreen', 'cyan', 'green', 'purple','gold','red']
type_names = list(assis_ferm.Type.unique())

type_names.sort() # sort the types  alphabetically by name

for i, name in enumerate(type_names):
    feat = ShapelyFeature(assis_ferm['geometry'][assis_ferm['Type'] == name], myCRS,
                          edgecolor='black',
                          facecolor=assi_colors[i],
                          linewidth=2,
                          alpha=0.25)
    ax.add_feature(feat)
    #myFig  # to show the updated figure


#generate_handles for ASSI Type
assif_handles = generate_handles(assis_ferm.Type.unique(), assi_colors, alpha=0.25)
nice_names = [name.title() for name in type_names]


# ax.legend() takes a list of handles and a list of labels corresponding to the objects you want to add to the legend

handles = assif_handles + sch_handle
labels = nice_names


leg = ax.legend(handles, labels, title='ASSIs by type', title_fontsize=14,
                 fontsize=12, loc='upper right', frameon=True, framealpha=1)

#for i, row in myshcs.iterrows():
 #   x, y = row.geometry.x, row.geometry.y # get the x,y location for each town
  #  plt.text(x, y, row['Level'].title(), fontsize=6, transform=myCRS) # use plt.text to place a label at x,y

myFig # to show the updated figure
myFig.savefig('mapAssi_Schools.png', bbox_inches='tight', dpi=300)


gridlines = ax.gridlines(draw_labels=True,
                         xlocs=[-8, -7.5],
                         ylocs=[55, 54.5])
gridlines.left_labels = False # turn off the left-side labels
gridlines.bottom_labels = False # turn off the bottom labels
ax.set_extent([xmin, xmax, ymin, ymax], crs=myCRS) # set the extent to the boundaries of the NI outline
#myFig # to show the updated figure
scale_bar(ax)
myFig # to show the updated figure

# Create a output path for the data
#out = r"/home/geo/Data/DAMSELFISH_distributions_SELECTION.shp"

#counties = gpd.read_file('data_files/Counties.shp')
#out = ('data_files/Co_Ferm.shp')
# Select Co Fermanagh

#selection = counties[counties['CountyName'] == 'FERMANAGH']
# Write those rows into a new Shapefile (the default output file format is Shapefile)
#selection.to_file(out)