#### ACCESS PARAMETERS START
import coexist
import os
from scipy.interpolate import interp1d
import sys
import numpy as np
import pept
import sys


parameters = coexist.create_parameters(
    variables = ["dt1", "tres"],
    minimums = [0.0, 10],
    maximums = [3, 20],
    values = [1.5, 15],      # Optional, initial guess
)

access_id = 0
#### ACCESS PARAMETERS END

var1, var2, = parameters["value"]

sep = np.array([525])
act = np.array([[2, 10, 20, 30, 45]])

times = 1

rates = []
trues = []
srs = []


for i in range(1):
    for j in range(5):
        print('submitting')

        os.system('Gate -a [Time,'+str(times[i][j])+'][Sep,'+str(sep[i])+'][Act,'+str(act[i][j])+'][dt1,'+str(var1)+'][tres,'+str(var2)+'][ID,'+str(access_id)+'] runForteAccess.mac')

        data = np.loadtxt('output/simple/Mouse_'+str(sep[i])+'mm_'+str(act[i][j])+'MBq_'+str(access_id)+'_finalCoinc.dat', usecols=(0, 1, 2, 3, 5, 6, 7))
        
        z1 = data[:, 3]
        z2 = data[:, 6]
        y1 = data[:, 2]
        y2 = data[:, 5]

        data = data[(z1 < 380 / 2) & (z1 > -380 / 2) & (z2 < 380 / 2) & (z2 > -380 / 2) \
                & (y1 < 510 / 2) & (y1 > -510 / 2) & (y2 < 510 / 2) & (y2 > -510 / 2)]
        
        
        lines = pept.LineData(data)

        voxels = pept.Voxels.from_lines(lines, number_of_voxels=[sep[i], 600,400], xlim=[-int(sep[i]/2), int(sep[i]/2)], ylim=[-300, 300], zlim=[-200, 200])

        voxels = voxels.voxels

        index = np.unravel_index(voxels.argmax(), voxels.shape)

        slice = voxels[index[0], :, :].T
        line = np.sum(slice, axis=1)
        line = line/np.max(line)
        peak = np.argmax(line)
        rate = len(data)/data[-1, 0]/1000
        left = np.sum(line[0:peak-20])
        right = np.sum(line[peak+20::])
        mid = 40*(line[peak-20]+line[peak+20])/2
        sr = rate*(left+mid+right)/np.sum(line)
        true = rate*(1-(left+mid+right)/np.sum(line))

        rates.append(rate)
        trues.append(true)
        srs.append(sr)


gate_total = np.array(rates)
gate_true = np.array(trues)
gate_sr = np.array(srs)

gate_act = act[0][:]

exp = np.loadtxt('Countrate_test_525mm.txt')
activity = exp[:, 0]
rates = exp[:, 1]
trues = exp[:, 2]
SR = exp[:, 3]

f_total = interp1d(activity, rates)
f_true = interp1d(activity, trues)
f_sr = interp1d(activity, SR)

diff_total = f_total(gate_act)-gate_total
diff_true = f_true(gate_act)-gate_true
diff_sr = f_sr(gate_act)-gate_sr

error_total = np.sum(abs(diff_total)/f_total(gate_act))
error_true = np.sum(abs(diff_true)/f_true(gate_act))
error_sr = np.sum(abs(diff_sr)/f_sr(gate_act))

error = [error_total, error_true, error_sr]

