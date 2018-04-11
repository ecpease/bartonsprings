# TrinityGAM

## Introduction

Here's the intro ...

## Package Installation

** Python versions:**

 **Python** 3.6. is required.

**Dependencies:**

Running this GAM model requires **Numpy** 1.12 (or higher), **matplotlib** 2.0 (or higher), **os**, **gdal**, **geopandas**, and **FloPy**.

**For base Python distributions:**

To install the above packages, see their given documentations.

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

	
