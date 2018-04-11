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

How the recharge file was created.

Here, we assume that the precipitation is recharge.

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
	
