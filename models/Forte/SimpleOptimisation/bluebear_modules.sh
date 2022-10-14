set -e
module purge; module load bluebear


source /rds/bear-apps/2019b/EL8-has/software/ROOT/6.20.00-foss-2019b-Python-3.7.4/bin/thisroot.sh
source /rds/bear-apps/2019b/EL8-has/software/Geant4/10.06.p03-foss-2019b/bin/geant4.sh
export PATH=$PATH:/rds/bear-apps/2019b/EL8-has/software/GATE/9.0-foss-2019b-Python-3.7.4/bin
#export PATH=$PATH:/rds/bear-apps/2020a/EL8-has/software/GATE/9.1-foss-2020a-Python-3.8.2/bin

#module load Geant4/10.06.p03-foss-2019b
#module load GATE/9.0-foss-2019b-Python-3.7.4
module load GATE/9.1-foss-2020a-Python-3.8.2
#module load BEAR-Python-DataScience/2020a-foss-2020a-Python-3.8.2
module load Geant4/10.7.3-GCC-9.3.0
module unload SciPy-bundle/2020.03-foss-2020a-Python-3.8.2
module load Python/3.8.2-GCCcore-9.3.0


G4DATA=/rds/projects/m/mangers-positron-imaging-centre/Geant4-Data/data
G4NEUTRONHPDATA=/rds/projects/m/mangers-positron-imaging-centre/Geant4-Data/G4NDL4.6
G4RADIOACTIVEDECAYDATA=/rds/projects/m/mangers-positron-imaging-centre/Geant4-Data/RadioactiveDecay5.6
G4LEVELGAMMADATA=/rds/projects/m/mangers-positron-imaging-centre/Geant4-Data/PhotonEvaporation5.7
G4ENSDFSTATEDATA=/rds/projects/m/mangers-positron-imaging-centre/Geant4-Data/G4ENSDFSTATE2.3
G4LEDATA=/rds/projects/m/mangers-positron-imaging-centre/Geant4-Data/G4EMLOW7.13
# Create virtual environment for installing Coexist
export VENV_DIR="${HOME}/virtual-environments"
export VENV_PATH="${VENV_DIR}/coexist-${BB_CPU}"

# Create a master venv directory if necessary
mkdir -p ${VENV_DIR}

# Check if virtual environment exists and create it if not
if [[ ! -d ${VENV_PATH} ]]; then
    echo "Virtual environment did not exist. Installing it now would create a race condition. Install coexist for all architectures first."
    exit 1
else
    source ${VENV_PATH}/bin/activate
fi



export PMIX_MCA_gds=hash

# Print the command line arguments to the terminal
echo $*
