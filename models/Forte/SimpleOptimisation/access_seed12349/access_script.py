#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File   : async_access_template.py
# License: GNU v3.0


'''Run a user-defined simulation script with a given set of free parameter
values, then save the `error` value to disk.

ACCES takes an arbitrary simulation script that defines its set of free
parameters between two `# ACCESS PARAMETERS START / END` directives and
substitutes them with an ACCESS-predicted solution. After the simulation, it
saves the `error` variable to disk.

This simulation setup is achieved via a form of metaprogramming: the user's
code is modified to change the `parameters` to what is predicted at each run,
then code is injected to save the `error` variable. This generated script is
called in a massively parallel environment with two command-line arguments:

    1. The path to this run's `parameters`, as predicted by ACCESS.
    2. A path to save the user-defined `error` variable to.

You can find them in the `access_seed<seed>/results` directory.
'''


import os
import sys
import pickle


###############################################################################
# ACCESS INJECT USER CODE START ###############################################
#### ACCESS PARAMETERS START

# Unpickle `parameters` from this script's first command-line argument and set
# `access_id` to a unique simulation ID

import coexist
import os
from scipy.interpolate import interp1d
import sys
import numpy as np
import pept
with open(sys.argv[1], 'rb') as f:
    parameters = pickle.load(f)
access_id = 0

access_id = int(sys.argv[1].split(".")[-2])
#### ACCESS PARAMETERS END

var1, var2, = parameters["value"]

sep = np.array([525])
act = np.array([[2, 10, 20, 30, 45]])

times = 0.5/np.sqrt(act)+0.01

rates = []
trues = []
srs = []


for i in range(1):
    for j in range(5):
        print('submitting')

        os.system('Gate -a [Time,'+str(times[i][j])+'][Sep,'+str(sep[i])+'][Act,'+str(act[i][j])+'][dt1,'+str(var1)+'][tres,'+str(var2)+'][ID,'+str(access_id)+'] runForteAccess.mac')
        
        #os.system('Gate -a [time,'+str(times[j])+'][activity,'+str(act[j])+'][dt1,'+str(var1)+'][pileup,'+str(var3)+'][lld,'+str(var4)+'][uld,'+str(var5)+'][eres,'+str(var6)+'][tres,'+str(var7)+'][ID,'+str(access_id)+'] Camera_ACCES.mac')




        data = np.loadtxt('output/simple/Mouse_'+str(sep[i])+'mm_'+str(act[i][j])+'MBq_'+str(access_id)+'_finalCoinc.dat', usecols=(0, 1, 2, 3, 5, 6, 7))
        
        os.system('rm /rds/projects/w/windowcr-pept-as-a-service/Forte_Rechar/ForteTest/output/simple/Mouse_'+str(sep[i])+'mm_'+str(act[i][j])+'MBq_'+str(access_id)+'_finalCoinc.dat')
        os.system('rm /rds/projects/w/windowcr-pept-as-a-service/Forte_Rechar/ForteTest/output/simple/Mouse_'+str(sep[i])+'mm_'+str(act[i][j])+'MBq_'+str(access_id)+'_Coincidences.dat')
        os.system('rm /rds/projects/w/windowcr-pept-as-a-service/Forte_Rechar/ForteTest/output/simple/Mouse_'+str(sep[i])+'mm_'+str(act[i][j])+'MBq_'+str(access_id)+'_delay.dat')
        os.system('rm /rds/projects/w/windowcr-pept-as-a-service/Forte_Rechar/ForteTest/output/simple/Mouse_'+str(sep[i])+'mm_'+str(act[i][j])+'MBq_'+str(access_id)+'_Run.dat')

        os.system('rm /rds/projects/w/windowcr-pept-as-a-service/Forte_Rechar/ForteTest/logs/sim_slurm_'+str(access_id)+'.out')
        os.system('rm /rds/projects/w/windowcr-pept-as-a-service/Forte_Rechar/ForteTest/logs/sim_slurm_'+str(access_id)+'.stats')


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

# ACCESS INJECT USER CODE END   ###############################################
###############################################################################


# Save the user-defined `error` and `extra` variables to disk.
with open(sys.argv[2], "wb") as f:
    pickle.dump(error, f)

if "extra" in locals() or "extra" in globals():
    path = os.path.split(sys.argv[2])
    path = os.path.join(path[0], path[1].replace("result", "extra"))
    with open(path, "wb") as f:
        pickle.dump(extra, f)
