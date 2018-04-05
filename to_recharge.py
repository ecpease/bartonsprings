import geopandas as gpd
import os
import numpy as np
from osgeo import gdal

df = gpd.read_file(os.path.join('trnt_n_grid_poly082615.shp')) # read in shapefile
print(df.head())
print('loaded shapefile')

nrow, ncol = df['ROW'].max(), df['COL'].max() # nrow and ncol are the maximum number of row and col in this case. 
print(nrow,ncol)

delr, delc = 5280, 5280 # mile x mile in feet


nlay = 8 # 8 layers in model, but not important



def get_raster_value(xcoords,ycoords,nrow,ncol,mfrows,mfcols,raster_path,name='name'):
    """
    :param xcoords:
    :param ycoords:
    :param nrow:
    :param ncol:
    :param mfrows:
    :param mfcols:
    :param raster_path:
    :param name:
    :return:
    """
    # print('getting data for '+ name)
    driver = gdal.GetDriverByName('GTiff')
    dataset = gdal.Open(raster_path)
    band = dataset.GetRasterBand(1)

    cols, rows = dataset.RasterXSize, dataset.RasterYSize

    transform = dataset.GetGeoTransform()

    xOrigin = transform[0]
    yOrigin = transform[3]
    pixelWidth = transform[1]
    pixelHeight = -transform[5]
    # print(xOrigin, yOrigin)
    data = np.array(band.ReadAsArray(0, 0, cols, rows))
    print(data.shape)
    # print(data)
    array = np.ones((nrow,ncol)) * -12345
    for i in range(len(xcoords)):
        if (xcoords[i]>xOrigin) and (yOrigin > ycoords[i]):# and (xcoords[i]<(xOrigin+ncol*pixelWidth)) and (yOrigin+nrow*pixelHeight < ycoords[i]):
        # print(xcoords[i],xOrigin,pixelWidth)
            try:
                col = abs(int((xcoords[i] - xOrigin) / pixelWidth))
                row = abs(int((yOrigin - ycoords[i]) / pixelHeight))
                # print(row,col, 'row, col')
                # try:
                r, c = int(mfrows[i]-1), int(mfcols[i]-1)
                # print(r,c, 'r,c')
                v = data[row, col]
                array[r, c] = v
            except:
                pass
        # except:
        #     pass

        # print(array[r,c])
        # print(data[row,col])
        # exit()
    array[array<=-12345] = np.nan

    # fig, ax = plt.subplots()
    # plt.imshow(array,cmap='jet')
    # plt.colorbar()
    # plt.show()
    return array


array = get_raster_value(df['CentroidX'],df['CentroidY'],nrow,ncol,df['ROW'],df['COL'],raster_path=os.path.join('rech_201305_clipped_GAM.tif'),name='prism')

np.savetxt('prsim_201305.txt',array)




