import numpy as np
import time
import os


acts = np.arange(1, 51, 1)

for act in acts:
    time.sleep(0.1)
    os.system('sbatch runForte.bash '+str(10/np.sqrt(act))+' 525 '+str(act)+' test')




