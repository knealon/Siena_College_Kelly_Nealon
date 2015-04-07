import numpy as np
import matplotlib.pyplot as plt

#import seaborn as sn

data = np.loadtxt('CosmicData2.txt', delimiter=',')

x = np.array([15,45,75])
yseen = np.array([17.,13.,5.]) #
ytrig = np.array([3.,4.,4.]) #

# Plot the raw data (triggered from LoggerPro
plt.figure(1)
data,xedges,patches = plt.hist(data,bins=3,range=(0,90),color='green')
plt.xlabel(r'$\theta$ as measured from vertical (degrees)',fontsize=24)
plt.ylabel(r'# of tracks/ 30$^\circ$',fontsize=24)
xedges += 15
print xedges
histx = xedges[0:3]
plt.ylim(0,17)
plt.tight_layout()

# Plot the trigger study.
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(1,1,1)
plt.errorbar(x,yseen,yerr=np.sqrt(yseen),xerr=15,fmt='o',linewidth=3,color='g',label='Visually observed')
plt.errorbar(x,ytrig,yerr=np.sqrt(ytrig),xerr=15,fmt='o',linewidth=3,color='k',label='Triggered')
plt.xlabel(r'$\theta$ as measured from vertical (degrees)',fontsize=24)
plt.ylabel(r'# of tracks/ 30$^\circ$',fontsize=24)
plt.legend(loc='upper right',fontsize=24)
plt.tight_layout()
plt.savefig('image.png')

# Plot the efficiency
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(1,1,1)
eff_err = (1./yseen)*np.sqrt(ytrig*(1-(ytrig/yseen)))
eff = ytrig/yseen
plt.errorbar(x,eff,yerr=eff_err,xerr=15,fmt='o',linewidth=3,color='g',label='Trigger efficiency')
plt.xlabel(r'$\theta$ as measured from vertical (degrees)',fontsize=24)
plt.ylabel(r'Fractional efficiency',fontsize=24)
plt.legend(loc='upper left',fontsize=24)
plt.ylim(0,1.2)
plt.tight_layout()
plt.savefig('image.png')

# Plot the acceptance corrected data.
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(1,1,1)

data_err = np.sqrt(data)

err0 = ((data/(eff*eff))*eff_err)
err1 = ((1./eff)*data_err)
acc_corr_data_err = np.sqrt(err0*err0 + err1*err1)

acc_corr_data = data/eff

plt.errorbar(x,acc_corr_data,yerr=acc_corr_data_err,xerr=15,fmt='o',linewidth=3,color='g',label='Acceptance corrected data')
plt.xlabel(r'$\theta$ as measured from vertical (degrees)',fontsize=24)
plt.ylabel(r'# of tracks/ 30$^\circ$',fontsize=24)
plt.tight_layout()
xpts = np.linspace(0,90,1000)
ypts = np.cos(np.deg2rad(xpts))
plt.plot(xpts,20*ypts,'r-',linewidth=3,label='Predicted distribtion')
plt.legend(loc='upper right',fontsize=18)
plt.ylim(0,50.)

plt.savefig('image.png')




#plt.plot(15,12,'rs')
#plt.plot(45,16,'rs')
#plt.plot(75,17,'rs')
#plt.figure(2)
#plt.hist([15,15,15,15,15,15,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75],bins=3)

plt.show()
