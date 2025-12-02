#!/bin/bash -l
# The -l above is required to get the full environment with modules
# Set the allocation to be charged for this job
# not required if you have set a default allocation
#SBATCH -A naiss2024-5-665
# The name of the script is myjob
#SBATCH -J rspt
# partition
#SBATCH -p main
# 5 hours wall-clock time will be given to this job
#SBATCH -t 05:00:00
# Number of nodes
#SBATCH -N 1
# Number of MPI processes
#SBATCH -n 124
ml PDC/24.11
ml rspt/20250228-cpeGNU-24.11

export RSPT_SCRATCH=$SNIC_TMP

runs "srun -n 124 rspt" 1e-09 100

echo "Job finished at `date` on `hostname`"