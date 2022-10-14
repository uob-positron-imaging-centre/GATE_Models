import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pept


sns.set_style('whitegrid')

print('test')

acts = np.arange(1, 51, 1)
seps = np.array([525])

rates = np.zeros(len(acts))
trues = np.zeros(len(acts))
srs = np.zeros(len(acts))

i = 0

for act in acts:
    for sep in seps:

        data = np.loadtxt('output/test/test_'+str(sep)+'mm_'+str(act)+'MBq_finalCoinc.dat', usecols=(0, 1, 2, 3, 5, 6, 7))
        #print(data_full, data_full.shape)
        z1 = data[:, 3]
        z2 = data[:, 6]
        y1 = data[:, 2]
        y2 = data[:, 5]

        data = data[(z1 < 380 / 2) & (z1 > -380 / 2) & (z2 < 380 / 2) & (z2 > -380 / 2) \
                & (y1 < 510 / 2) & (y1 > -510 / 2) & (y2 < 510 / 2) & (y2 > -510 / 2)]


        lines = pept.LineData(data)

        voxels = pept.Voxels.from_lines(lines, number_of_voxels=[sep,600,400], xlim=[-int(sep/2), int(sep/2)], ylim=[-300, 300], zlim=[-200, 200])

        voxels = voxels.voxels

        index = np.unravel_index(voxels.argmax(), voxels.shape)

        slice = voxels[index[0], :, :].T
        line = np.sum(slice, axis=1)
        line = line/np.max(line)
        peak = np.argmax(line)

        rate = len(data)/(data[-1, 0]-data[0, 0])/1000
        left = np.sum(line[0:peak-20])
        right = np.sum(line[peak+20::])
        mid = 40*(line[peak-20]+line[peak+20])/2
        sr = rate*(left+mid+right)/np.sum(line)
        true = rate*(1-(left+mid+right)/np.sum(line))
        
        rates[i] = rate
        trues[i] = true
        srs[i] = sr
        i += 1


plt.scatter(acts, rates, marker='o', label='Total')
plt.scatter(acts, trues, marker='^', label='True')
plt.scatter(acts, srs, marker='x', label='Scatter + Random')
plt.xlabel('Activity (MBq)', fontsize=20)
plt.ylabel('Count-Rate (kHz)', fontsize=20)
plt.xlim(left=0)
plt.ylim(bottom=0)
plt.legend(fontsize=14)
plt.savefig('Countrate_test_525mm.png', bbox_inches='tight', dpi=300)
plt.close()

np.savetxt('Countrate_test_525mm.txt', np.array([acts, rates, trues, srs]).T)


