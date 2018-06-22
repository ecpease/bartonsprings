import flopy
import numpy as np
import matplotlib.pyplot as plt

# Convert Units to feet per year
rech = np.loadtxt('prism_mean_rch.txt')
rech = rech / 100 # mm / year
rech = .00328084 * rech * 12 # feet/ year
rech = rech * 12 #feet/year = inch/month, still need to convert to feet per day for MODFLOW model
print('loaded text')

fig, ax = plt.subplots()
plt.imshow(rech, cmap='jet')
plt.colorbar()
plt.title('Aquifer Recharge (Base, inches/month)')
nrow, ncol = rech.shape  # 743=rows, 1412=columns

nper = 50 # years
perlen = [365.25] # time in each stress period
steady = [True] # stady state the first year
for sp in range(1,nper):
	perlen.append(365.25)
	steady.append(False) # transient after
nstp = 1 # number of time steps in each stress period
delr, delc = 5280, 5280
lenuni = 1 # feet
top, botm = 100, 0 # top elevation of the model is 100, botm elevation is 0
rech = rech / 12 / 30.4 # to feet per day

case = ['min','mid','max']
mult = [.75,1,1.25]
for i in range(len(mult)):
    mf = flopy.modflow.Modflow('trinity_rech_'+case[i]) # this is the main flopy.modflow model object;
    dis = flopy.modflow.ModflowDis(mf,1,nrow,ncol,nper,delr,delc,0,top,botm,perlen,nstp,steady=steady,itmuni=4,
                                   lenuni=lenuni,rotation=65)
    rch = flopy.modflow.ModflowRch(mf,rech=rech*mult[i])  # is the recharge pckage
    mf.write_input()
    print(f'finished case {case[i]}')
rch.plot(colorbar=True)
plt.show()
















