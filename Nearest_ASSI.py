from shapely.strtree import STRtree
import geopandas as gpd

def get_nearest_assi_to_sch(sch_name, assis_ferm, my_schs):
    '''

    :param sch_name: Enter the full name of the school
    :param assis_ferm: the Areas of Special Scientific Interest in Co Fermanagh
    :param my_schs: the schools point shapefile
    :return: returns selected information on the nearest ASSI to each School
    '''

    assis_tree = STRtree(assis_ferm['geometry'].values) # creates an STRtree object with the ASSI data
    Fschs = my_schs.loc[my_schs['Name'] == sch_name, 'geometry'].values[0]
    nearest = assis_tree.nearest(Fschs) # gets the closest ASSI  to each sch

    nearest_row = assis_ferm[assis_ferm['geometry'] == nearest]
    return nearest_row

sch_name = input("Enter school name: ")
assis_ferm = gpd.read_file('data_files/Assis_Fermanagh.shp')
myschs = gpd.read_file('data_files/schoolF_points.shp')

nearest_row = get_nearest_assi_to_sch(sch_name, assis_ferm, myschs)
print(f'Name: {nearest_row.NAME.values[0]}, Type: {nearest_row.Type.values[0]}, Habitat: {nearest_row.HABITAT.values[0]}, Species: {nearest_row.SPECIESPT1.values[0]}')
