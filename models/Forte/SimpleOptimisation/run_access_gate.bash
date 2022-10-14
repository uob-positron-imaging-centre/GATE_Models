#!/bin/bash
#SBATCH --qos bbdefault
#SBATCH --ntasks 1
#SBATCH --account=mangers-positron-imaging-centre
#SBATCH --time 144:0:0
#SBATCH --mail-type ALL
#SBATCH --constraint icelake


set -e
module purge; module load bluebear


# Contains pept and OpenCV
#module load BEAR-Python-DataScience/2020a-foss-2020a-Python-3.8.2
module load Python/3.8.2-GCCcore-9.3.0


#pip install --upgrade pip
# Create virtul environment for installing Coexist
export VENV_DIR="${HOME}/virtual-environments"
export VENV_PATH="${VENV_DIR}/coexist-${BB_CPU}"

# Create a master venv directory if necessary
mkdir -p ${VENV_DIR}

# Check if virtual environment exists and create it if not
if [[ ! -d ${VENV_PATH} ]]; then
    python -m venv --system-site-packages ${VENV_PATH}

    echo "Created venv, going to install coexist"

    source ${VENV_PATH}/bin/activate
    pip install git+https://github.com/uob-positron-imaging-centre/Coexist.git --no-use-pep517
    #pip install numpy --upgrade
    #pip install git+https://github.com/uob-positron-imaging-centre/pept.git --no-use-pep517
else
    echo "using venv"
    source ${VENV_PATH}/bin/activate
    #pip install --upgrade git+https://github.com/uob-positron-imaging-centre/Coexist.git --no-use-pep517
    #pip install git+https://github.com/uob-positron-imaging-centre/pept.git --no-use-pep517
    #pip install numpy --upgrade --no-use-pep517
    #pip install git+https://github.com/uob-positron-imaging-centre/pept.git --no-use-pep517
fi


python access_learn_slurm_gate.py
