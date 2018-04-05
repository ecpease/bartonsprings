import flopy
import numpy as np
import matplotlib.pyplot as plt

# Convert Units to feet per year
rech = np.loadtxt('prsim_201305.txt') # mm # 100
rech = rech / 100 # mm
rech = .00328084 * rech # feet/month
rech = rech * 12 #feet/year = inch/month
print('loaded text')

# Begin Plotting (matplotlib)
fig, ax = plt.subplots() # initiate plot

plt.imshow(rech,cmap='jet') # colormap with color scheme specified
plt.colorbar() # create colorbar
plt.title('Aquifer Recharge (inches/month)')

nrow, ncol = rech.shape # 1124=rows, 1412=columns

mf = flopy.modflow.Modflow('trinity_rech')

nper = 82 # years 
perlen = [365.25] # time in each stress period
steady = [True] # stady state the first year
for sp in range(1,nper):
	perlen.append(365.25)
	steady.append(False) # transient after
nstp = 1 # number of time steps in each stress period
delr, delc = 5280, 5280 
lenuni = 1 # is feet
top, botm = 100, 0
dis = flopy.modflow.ModflowDis(mf,1,nrow,ncol,nper,delr,delc,0,top,botm,perlen,nstp,steady=steady,itmuni=4,lenuni=lenuni)
rch = flopy.modflow.ModflowRch(mf,rech=rech)
mf.write_input()

plt.show()












