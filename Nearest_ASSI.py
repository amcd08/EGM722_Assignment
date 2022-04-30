from shapely.strtree import STRtree
import geopandas as gpd


def get_nearest_assi_to_sch(sch_name, assis_ferm, my_schs):
    assis_tree = STRtree(assis_ferm['geometry'].values) # creates an STRtree object with the ASSI data

    Fschs = my_schs.loc[my_schs['Name'] == sch_name, 'geometry'].values[0]
    nearest = assis_tree.nearest(Fschs) # gets the closest ASSI  to each sch

    nearest_row = assis_ferm[assis_ferm['geometry'] == nearest]
    return nearest_row

sch_name = input("Enter school name: ")
assis_ferm = gpd.read_file('data_files/Assis_Fermanagh.shp')
myschs = gpd.read_file('data_files/schoolF_points.shp')

nearest_row = get_nearest_assi_to_sch(sch_name, assis_ferm, myschs)
print(f'Name: {nearest_row.NAME} ')#Type: {nearest_row.Type}')


