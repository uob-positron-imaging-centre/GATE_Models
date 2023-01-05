#!/bin/bash
#SBATCH --qos bbshort
#SBATCH --ntasks=1
#SBATCH --account=mangers-positron-imaging-centre
#SBATCH --time 0:10:00
#SBATCH --mem=10G
#SBATCH --mail-type FAIL

set -e

module purge; module load bluebear

module load bear-apps/2020a
module load foss/2020a
module load CMake/3.16.4-GCCcore-9.3.0
module load GCC/9.3.0
module load ROOT/6.20.00-foss-2019b-Python-3.7.4


source /rds/projects/m/mangers-positron-imaging-centre/root/install/bin/thisroot.sh
source /rds/projects/m/mangers-positron-imaging-centre/geant4/install/bin/geant4.sh
export PATH=$PATH:/rds/projects/m/mangers-positron-imaging-centre/gate/install/bin


Gate Camera.mac

