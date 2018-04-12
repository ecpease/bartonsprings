import flopy
import numpy as np
import matplotlib.pyplot as plt

# Convert Units to feet per year
rech = np.loadtxt('prism_201305.txt') # mm * 100
rech = rech / 100 # mm
rech = .00328084 * rech # feet/month
rech = rech * 12 #feet/year = inch/month, still need to convert to feet per day for MODFLOW model
print('loaded text')

# Begin Plotting (matplotlib)
fig, ax = plt.subplots() # initiate plot

plt.imshow(rech,cmap='jet') # colormap with color scheme specified
plt.colorbar() # create colorbar
plt.title('Aquifer Recharge (inches/month)')



nrow, ncol = rech.shape # 1124=rows, 1412=columns

mf = flopy.modflow.Modflow('trinity_rech') # this is the main flopy.modflow model object; https://modflowpy.github.io/flopydoc/mf.html 

nper = 82 # years 
perlen = [365.25] # time in each stress period
steady = [True] # stady state the first year
for sp in range(1,nper):
	perlen.append(365.25)
	steady.append(False) # transient after
nstp = 1 # number of time steps in each stress period
delr, delc = 5280, 5280 
lenuni = 1 # is feet
top, botm = 100, 0 # top elevation of the model is 100, botm elevation is 0
dis = flopy.modflow.ModflowDis(mf,1,nrow,ncol,nper,delr,delc,0,top,botm,perlen,nstp,steady=steady,itmuni=4,lenuni=lenuni,rotation=65) # discritization object; https://modflowpy.github.io/flopydoc/mfdis.html

# now we need recharge in ft/day becuse modflow has no idea what the units are and it is up to us to keep the correct. (ft and day)
rech = rech / 12 / 30.4  # ft/day

rch = flopy.modflow.ModflowRch(mf,rech=rech) # is the recharge pckage https://modflowpy.github.io/flopydoc/mfrch.html

mf.write_input() # write the modflow files, the ".rch" file is the recharge package for modflow


rch.plot(colorbar=True) # plot with modflow properties (in ft/day)

plt.show()












