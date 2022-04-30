# EGM722_Assignment
A tool for Schools in Co Fermanagh to find their nearest ASSI

## Getting started

The school should first install 'git' and 'conda' on a computer.  Follow the instructions for installing git from [here](https://git-scm.com/downloads), 
and Anaconda from [here](https://docs.anaconda.com/anaconda/install/). 


###  Obtaining the data

-  Download/clone this repository to the school computer. 

    Once you have Git and Anaconda installed, __clone__ this repository to your computer.  Choose one of the following methods to do this:-

1. Open GitHub Desktop and select __File__ > __Clone Repository__. Select the __URL__ tab, then enter the URL for this 
   repository.
2. Open __Git Bash__ (from the __Start__ menu), then navigate to the folder where this tool is to be located.  
   Now, execute the following command: `git clone https://github.com/iamdonovan/egm722.git`. You should see some messages
   about downloading/unpacking files, and the repository should be set up.


##  
 
- Creat a conda environment

  Once you have successfully cloned the repository, you can then create a `conda` environment.

  To do this, use the environment.yml file provided in the repository. If you have Anaconda Navigator installed,
  you can do this by selecting __Import__ from the bottom of the __Environments__ panel. 

  Otherwise, you can open a command prompt (on Windows, you may need to select an Anaconda command prompt). Navigate
  to the folder where you cloned this repository and run the following command:

```
C:\Users\amcd0812> conda env create -f environment.yml
```

  This may take some time!  


- Open the file to run the programme.
From the Anaconda Navigator, activate the environment created and launch Pycharm (or another IDE of choice).  Navigate to the folder.  



## Next Steps

 
- Enter the name of the School to get the nearest ASSI. 


