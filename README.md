# EGM722_Assignment
This repository has been prepared as part of the Assignment for EGM722.  It contains information for Schools 
in Co. Fermanagh on the location of Areas of Special Scientific Inerest (ASSIs) and areas of bog in county, as a basis for field trips or ecology projects. 
Schools can also find their nearest ASSI and some information on the designation features.

## Getting started

Firstly, install 'git'. The instructions can be found  [here](https://git-scm.com/downloads). 
conda is the package management system recommended for creating the environment.  The conda GUI Anaconda Navigator can be downloaded [here](https://docs.anaconda.com/anaconda/install/). 


###  Creating and setting up the environment

-  Once you have Git and Anaconda installed, __clone__ this repository to your computer.  Either:-

1. Open GitHub Desktop and select __File__ > __Clone Repository__. Select the __URL__ tab, then enter the URL for this 
   repository.
2. Open __Git Bash__ (from the __Start__ menu); navigate to the folder where the repository is to be located and   
   execute the following command: `git clone https://github.com/amcd08/EGM722_Assignmentgit`. Messages about downloading/unpacking files will appear and the repository should be set up.


##  
 
- Once you have successfully cloned the repository, you can then create a `conda` environment.

  The **environment.yml** file provided in the repository loads the packages and modules needed to run the script (it may take some time for all these to load). 
  With Anaconda Navigator, you can set up the environment by selecting __Import__ from the bottom of the __Environments__ panel. 

  Otherwise, you can open a command prompt (on Windows, you may need to select an Anaconda command prompt). Navigate
  to the folder where you cloned this repository and run the following command:

```
C:\Users\amcd0812> conda env create -f environment.yml
```

##  
 
- Open the project

  From Anaconda Navigator, activate the project environment and navigate to the folder where the repository is stored.
  An IDE can assist wiht running the code. The [PyCharm](https://www.jetbrains.com/pycharm/download/#section=windows) IDE can be launched from the Navigator. 
 



## Data Files
- The location of schools in Northern Ireland.  This is available from the NI Government OpenData NI website [here](https://www.opendatani.gov.uk/dataset/locate-a-school).  The list was filtered to select just the primary and secondary schools in County Fermanagh -  
 53 in total and is provided in the repository data files as FermSchl_l.txt. 
- The location of ASSIs in Northern Ireland. This  is available from the OpenData NI website [here](https://www.opendatani.gov.uk/dataset?tags=ASSI). This shapefile was filtered to select just the ASSIs in Co Fermanagh, 95 in total; the shapefile is provided in the repository data files. 
 -The Land Cover Map 2015 (25m raster, N. Ireland).  This can be obtained on request from the Environmental Information Data Centre, 
https://eidc.ac.uk/.   
- The Northern Ireland County boundaries shapefile, available from  Open Data NI. It is provided in the datafiles. 
- The NI Mosaic tif, provided as part of the module. 


## Next Steps
  -There are three aspects to the project.  
 1. The creation of the map of Co Fermanagh, which displays ASSIs and the locations of the primary and secondary schools.  
    -*Script: schools.py* 

 2. A function which identifies the nearest ASSI to each school.  
   -*Script: Nearest_ASSI.py* 

 3. Extracting and displaying landclass data for Co. Fermanagh. 
   -Reprojecting the landclass data and masking the landclass and NI mosaic to the county boundary.
   -*Scripts: reproject_nilc25raster.py, fermanagh_raster.py, ferm_mosaic.py*.  
    -Calculating land class areas and displaying areas of bog.
   -*Scripts: fermanagh_landclass_stats.py, lcdisplay.py*


 
- The scripts should be run in the order above.


