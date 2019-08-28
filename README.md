# TrinityGAM

## Introduction

The Trinity Groundwater Availability Model is a Texas Water Development Board tool used for assessing the Trinity Aquifer water supply into the future.  Here, as a UT class project in Intelligent Systems for Geosciences, the class worked to develop an understanding of Python, the importance of automated workflows, and reproducible science using the Trinity GAM as a case study.  The research file of the MODFLOW model was replaced with a class-constructed recharge file derived from the 30 year mean precipitation in the region.  This repository demonstrates how this can be done using FloPy as the Python interface for MODFLOW as well as data preparation packages in Python (Pandas, Geopandas) and gridded data management (NumPy, GDAL). 

## Package Installation

** Python versions:**

 **Python** 3.6. is required.

**Dependencies:**

Running this GAM model requires **Numpy** 1.12 (or higher), **matplotlib** 2.0 (or higher), **os**, **gdal**, **geopandas**, and **FloPy**.


To install the above packages, see their given documentations.
<<<<<<< HEAD

## Recharge File

***Here, we assume that the precipitation is recharge.***

### Part A. Convert the raster to a NumPy array, then resize it to match model array.  Create .txt file 

1. import all packages required (see above dependencies).
2. input the GAM shapefile from the Texas Water Development Board.
3. Determine number of rows, columns, and layers
4. Array output is .txt file that has the same number of rows and columns as our model.

### Part B. Conversions, Data Visualization

1. Load .txt file created in Part A.
2. Convert NumPy array units to ft/year
3. Give number of years and the time per period
4. Create colormap of NumPy array
=======

## Recharge File

***Here, we assume that the precipitation is recharge.***

### Part A. Convert the raster to a NumPy array, then resize it to match model array.  Create .txt file 

1. import all packages required (see above dependencies).
2. input the GAM shapefile from the Texas Water Development Board.
3. Determine number of rows, columns, and layers
4. Array output is .txt file that has the same number of rows and columns as our model.

### Part B. Conversions, Data Visualization

1. Load .txt file created in Part A.
2. Convert NumPy array units to ft/year
3. Give number of years and the time per period
4. Create colormap of NumPy array

## Introduction to Using Git and GitHub

### When you want to push a commit to the TrinityGAM repository:
*****Helpful resource: https://gist.github.com/spences10/5c492e197e95158809a83650ff97fc3a*****

1. Fork the TrinityGAM (you'll see your username now / TrinityGAM)
2. Clone the repo to your desired location (I make a GitHub folder and put everything in that)
2a. ex) git clone [the copied 'clone' URL]
3. Type into command prompt: git remote add upstream [the copied 'clone' URL]
4. Google what's next sorry

