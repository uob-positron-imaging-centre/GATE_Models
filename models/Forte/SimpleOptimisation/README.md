
# Simple Optimisation of the GATE model

In this folder you will find all of the codes needed to generate test data and calibrate a GATE model of the ADAC Forte using the SLURM job manager with an HPC or your own machine which can run GATE and ACCES. 

In this example a GATE model of the ADAC Forte is prescribed a singles dead time of 1.5 us and time resolution of 15 ns. We want to use ACCES to find these values by comparing the simulated detector response with a guess of the correct parameters to the ground truth detector response using the prescribed parameters.

To generate ground truth detector response run 'python3 launch.py' or use the pregenerated data found in 'Countrate_test_525mm.txt'.

To analyse your own generated ground truth response and save the count-rate vs activity curve as 'Countrate_test_525mm.txt' run 'python3 analyzeTests.py'.

To begin the ACCES calibration of the singles dead-time and time resolution with an HPC that has a SLURM job manager, run 'sbatch run_access_gate.bash' or if you wish to run the optimisation on your own machine run 'python3 access_learn_single_gate.py'.

To generate the plots for analysing the results of the optimisation on an HPC with a SLURM job manager run 'sbatch run_access_plot.bash' or on your own machine run 'python3 plotConvergence.py'.

![](convergenceScatterSimple.png)
![](access_2d.png)

