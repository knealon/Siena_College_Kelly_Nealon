import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('CosmicData2.txt', delimiter=',')

x = np.array([15,45,75])
y = np.array([12,16,17])

# Plot the triggered values
plt.figure(1)
histy,xedges,patches = plt.hist(data,bins=3,range=(0,90))
xedges += 15
print xedges
histx = xedges[0:3]

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(1,1,1)
plt.errorbar(histx,histy,yerr=np.sqrt(histy),xerr=15,fmt='o',linewidth=2,color='r',label='Visually observed')

# Plot the ``seen" values.
plt.errorbar(x,y,yerr=np.sqrt(y),xerr=15,fmt='o',linewidth=2,color='k',label='Triggered')

plt.xlabel(r'$\theta$ as measured from vertical (degrees)',fontsize=24)
plt.ylabel(r'# of tracks/ 30$^\circ$',fontsize=24)

plt.legend(loc='upper left')

plt.tight_layout()

plt.savefig('image.png')

#plt.plot(15,12,'rs')
#plt.plot(45,16,'rs')
#plt.plot(75,17,'rs')
#plt.figure(2)
#plt.hist([15,15,15,15,15,15,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75],bins=3)

plt.show()
