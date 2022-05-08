# EGM722_Assignment
This repository has been prepared as part of the Assignment for EGM722.  It contains information for Schools 
in Co Fermanagh on the location of Areas of Special Scientific Inerest (ASSIs) and bog land class in Co. Fermanagh.  
Schools can find their nearest ASSI.  

## Getting started

Install 'git' and 'conda'.  Follow the instructions for installing git from [here](https://git-scm.com/downloads), 
and Anaconda from [here](https://docs.anaconda.com/anaconda/install/). An IDE such as [PyCharm](https://www.jetbrains.com/pycharm/download/#section=windows) can assist with running the code. 


###  Creating and setting up the environment

-  Download/clone this repository to the computer. 

   Once you have Git and Anaconda installed, __clone__ this repository to your computer.  Choose one of the following methods to do this:-

1. Open GitHub Desktop and select __File__ > __Clone Repository__. Select the __URL__ tab, then enter the URL for this 
   repository.
2. Open __Git Bash__ (from the __Start__ menu); navigate to the folder where the repository is to be located and   
   execute the following command: `git clone https://github.com/amcd08/EGM722_Assignmentgit`. You should see some messages
   about downloading/unpacking files, and the repository should be set up.


##  
 
- Create a conda environment

  Once you have successfully cloned the repository, you can then create a `conda` environment.

  To do this, use the environment.yml file provided in the repository. With Anaconda Navigator,
  you can do this by selecting __Import__ from the bottom of the __Environments__ panel. 

  Otherwise, you can open a command prompt (on Windows, you may need to select an Anaconda command prompt). Navigate
  to the folder where you cloned this repository and run the following command:

```
C:\Users\amcd0812> conda env create -f environment.yml
```

##  
 
- Open the project

 From Anaconda Navigator, activate to the environment created and launch Pycharm (or another IDE of choice).  
 Navigate to the folder where the repository is stored.



## Data Files
  -The location of schools in Northern Ireland.  This is available from the NI Government OpenData NI website, with the csv file 
 of the list of schools available here.  The list was filtered to select just the primary and secondary schools in County Fermanagh -  
 53 in total and is provided in the repository data files as FermSchl_l.txt. 
- The location of ASSIs in Northern Ireland.  This  is available from the OpenData NI website and is provided in shapefile format
 here. This shapefile was filtered to select just the ASSIs in Co Fermanagh, 95 in total; the shapefile is provided in the repository data files. 
 -The Land Cover Map 2015 (25m raster, N. Ireland).  This can be obtained on request from the Environmental Information Data Centre, 
https://eidc.ac.uk/.   
- The Northern Ireland County boundaries shapefile, available from  Open Data NI. It is provided in the datafiles. 
- The NI Mosaic tif, provided as part of the module. 



##There are three aspects to the project. The Scripts for each aspect are detailed below.
	The creation of the map of Co Fermanagh, which displays ASSIs and the locations of the primary and secondary schools.  
	Script:   schools.py 

	A function which identifies the nearest ASSI to each school.  
	Script:   Nearest_ASSI.py . 

	Extracting and displaying landclass data for Co. Fermanagh 
	Scripts: reproject_nilc25raster.py, fermanagh_raster.py, ferm_mosaic.py - reprojecting the landclass data and masking the landclass and NI mosaic to 
	the county boundary.
	fermanagh_landclass_stats.py and : lcdisplay.py - calculating land class areas and displaying areas of bog.		 




## Next Steps
-

 
-


