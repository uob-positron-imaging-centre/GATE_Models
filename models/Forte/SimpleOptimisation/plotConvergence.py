import coexist
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


sns.set_style('whitegrid')



# Use path to either the `access_info_<random_seed>` folder itself, or its
# parent directory

access_data = coexist.AccessData("access_seed12349")


data = access_data.epochs_scaled
epochs = access_data.num_epochs

print(data)


p1 = data['dt1_std']
#p2 = data['dt2_std']
#p3 = data['pileup_std']
#p4 = data['lld_std']
#p5 = data['uld_std']
p6 = data['tres_std']

plt.plot(np.arange(epochs)+1, p1)
#plt.plot(np.arange(epochs)+1, p2)
#plt.plot(np.arange(epochs)+1, p3)
#plt.plot(np.arange(epochs)+1, p4)
#plt.plot(np.arange(epochs)+1, p5)
plt.plot(np.arange(epochs)+1, p6)

plt.scatter(np.arange(epochs)+1, p1, marker='o', label='Singles Dead-Time')
#plt.scatter(np.arange(epochs)+1, p2, marker='^', label='Coincidence Dead-Time')
#plt.scatter(np.arange(epochs)+1, p3, marker='s', label='Pile-up')
#plt.scatter(np.arange(epochs)+1, p4, marker='d', label='Lower Energy Discriminator')
#plt.scatter(np.arange(epochs)+1, p5, marker='x', label='Upper Energy Discriminator')
plt.scatter(np.arange(epochs)+1, p6, marker='^', label='Time Resolution')
plt.xlabel('Epochs (#)', fontsize=20)
plt.ylabel('Scaled Standard Deviation', fontsize=20)
plt.xlim(0, 30)
plt.ylim(bottom=0)
plt.legend(fontsize=14)
plt.savefig('convergenceScatterSimple.png', dpi=300, bbox_inches='tight')
plt.close()



data = access_data.epochs

p1 = data['dt1_std']
#p2 = data['dt2_std']
#p3 = data['pileup_std']
#p4 = data['lld_std']
#p5 = data['uld_std']
p6 = data['tres_std']
#print('stds', p1, p2, p3, p4, p5, p6)

m1 = data['dt1_mean']
#m2 = data['dt2_mean']
#m3 = data['pileup_mean']
#m4 = data['lld_mean']
#m5 = data['uld_mean']
m6 = data['tres_mean']

"""
plt.figure(figsize=(25, 15))
plt.subplot(231)
plt.errorbar(np.arange(epochs)+1, m1*1000, yerr=p1*1000, color='tab:blue')
plt.title('Singles Dead-Time (ns)', fontsize=25)
plt.xlabel('Epochs (#)', fontsize=22)
plt.xticks(size=20)
plt.yticks(size=20)

#plt.subplot(232)
#plt.errorbar(np.arange(epochs)+1, m2*1000, yerr=p2*1000, color='tab:orange')
#plt.title('Coincidence Dead-Time (ns)', fontsize=25)
#plt.xlabel('Epochs (#)', fontsize=22)
#plt.xticks(size=20)
#plt.yticks(size=20)

plt.subplot(233)
plt.errorbar(np.arange(epochs)+1, m3, yerr=p3, color='tab:green')
plt.title('Pileup (ns)', fontsize=25)
plt.xlabel('Epochs (#)', fontsize=22)
plt.xticks(size=20)
plt.yticks(size=20)

plt.subplot(234)
plt.errorbar(np.arange(epochs)+1, m4, yerr=p4, color='tab:red')
plt.title('Lower Energy Discriminator (keV)', fontsize=25)
plt.xlabel('Epochs (#)', fontsize=22)
plt.xticks(size=20)
plt.yticks(size=20)

plt.subplot(235)
plt.errorbar(np.arange(epochs)+1, m5, yerr=p5, color='tab:purple')
plt.title('Upper Energy Discriminator (keV)', fontsize=25)
plt.xlabel('Epochs (#)', fontsize=22)
plt.xticks(size=20)
plt.yticks(size=20)

plt.subplot(236)
plt.errorbar(np.arange(epochs)+1, m6, yerr=p6, color='tab:brown')
plt.title('Time Resolution (ns)', fontsize=25)
plt.xlabel('Epochs (#)', fontsize=22)
plt.xticks(size=20)
plt.yticks(size=20)

plt.savefig('subplots.png', dpi=300, bbox_inches='tight')
plt.close()
"""

data = access_data.epochs

p1 = data['dt1_std']
#p2 = data['dt2_std']
#p3 = data['pileup_std']
#2p4 = data['lld_std']
#p5 = data['uld_std']
p6 = data['tres_std']


m1 = data['dt1_mean']
#m2 = data['dt2_mean']
#m3 = data['pileup_mean']
#m4 = data['lld_mean']
#m5 = data['uld_mean']
m6 = data['tres_mean']
parameters = access_data.parameters

"""
plt.errorbar(np.arange(epochs)+1, m1*1000, yerr=p1*1000, color='tab:blue')
plt.plot(np.arange(epochs)+1, m1*1000, lw=2, color='tab:blue')
#plt.title('Singles Dead-Time (ns)', fontsize=26)
plt.xlabel('Epochs (#)', fontsize=18)
plt.xticks(size=14)
plt.yticks(size=14)
plt.ylim(parameters['min'].dt1*1000, parameters['max'].dt1*1000)
plt.xlim(left=0, right=epochs+1.5)
plt.savefig('pics/Forte_subplot1.png', dpi=300, bbox_inches='tight')
plt.close()

#plt.subplot(132)
#plt.errorbar(np.arange(epochs)+1, m2*1000, yerr=p2*1000, color='tab:orange')
#plt.plot(np.arange(epochs)+1, m2*1000, lw=2, color='tab:orange')
#plt.title('Noise Frequency', fontsize=26)
#plt.xlabel('Epochs (#)', fontsize=18)
#plt.xticks(size=14)
#plt.yticks(size=14)
#plt.ylim(parameters['min'].dt2*1000, parameters['max'].dt2*1000)
#plt.xlim(left=0, right=epochs+1.5)
#plt.savefig('pics/Forte_subplot2.png', dpi=300, bbox_inches='tight')
#plt.close()

plt.errorbar(np.arange(epochs)+1, m3, yerr=p3, color='tab:green')
plt.plot(np.arange(epochs)+1, m3, lw=2, color='tab:green')
#plt.title('Pileup (ns)', fontsize=26)
plt.xlabel('Epochs (#)', fontsize=18)
plt.xticks(size=14)
plt.yticks(size=14)
plt.ylim(parameters['min'].pileup, parameters['max'].pileup+100)
plt.xlim(left=0, right=epochs+1.5)
plt.savefig('pics/Forte_subplot3.png', dpi=300, bbox_inches='tight')
plt.close()

#plt.savefig('pics/subplots_modular1.png', dpi=300, bbox_inches='tight')
#plt.close()


#plt.figure(figsize=(26, 8))
#plt.subplot(131)
plt.errorbar(np.arange(epochs)+1, m4, yerr=p4, color='tab:red')
plt.plot(np.arange(epochs)+1, m4, lw=2, color='tab:red')
#plt.title('Lower Energy Discriminator (keV)', fontsize=26)
plt.xlabel('Epochs (#)', fontsize=18)
plt.xticks(size=14)
plt.yticks(size=14)
plt.ylim(parameters['min'].lld, parameters['max'].lld)
plt.xlim(left=0, right=epochs+1.5)
plt.savefig('pics/Forte_subplot4.png', dpi=300, bbox_inches='tight')
plt.close()


#plt.subplot(132)
plt.errorbar(np.arange(epochs)+1, m5, yerr=p5, color='tab:brown')
plt.plot(np.arange(epochs)+1, m5, lw=2, color='tab:brown')
#plt.title('Time Resolution (ns)', fontsize=26)
plt.xlabel('Epochs (#)', fontsize=18)
plt.xticks(size=14)
plt.yticks(size=14)
plt.ylim(parameters['min'].uld, parameters['max'].uld)
plt.xlim(left=0, right=epochs+1.5)
plt.savefig('pics/Forte_subplot5.png', dpi=300, bbox_inches='tight')
plt.close()


#plt.subplot(133)
plt.errorbar(np.arange(epochs)+1, m6, yerr=p6, color='tab:purple')
plt.plot(np.arange(epochs)+1, m6, lw=2, color='tab:purple')
#plt.title('Upper Energy Discriminator (keV)', fontsize=26)
plt.xlabel('Epochs (#)', fontsize=18)
plt.xticks(size=14)
plt.yticks(size=14)
plt.ylim(parameters['min'].tres, parameters['max'].tres)
plt.xlim(left=0, right=epochs+1.5)
plt.savefig('pics/Forte_subplot6.png', dpi=300, bbox_inches='tight')
plt.close()

"""

#import pept.tracking.trajectory_separation as tsp
#import matplotlib.pyplot as plt


#fig = coexist.plots.access(access_data, overall=False)
#fig.show()
#fig.write_image("convergence.png")
#fig.write_image("convergence.html")


fig = coexist.plots.access2d(access_data)
fig.write_html("convergence2D.html")
#fig.show()

