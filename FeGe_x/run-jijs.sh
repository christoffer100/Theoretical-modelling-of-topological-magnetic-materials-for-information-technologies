#!/bin/bash -l
# The -l above is required to get the full environment with modules
# Set the allocation to be charged for this job
# not required if you have set a default allocation
#SBATCH -A naiss2024-5-665
# The name of the script is myjob
#SBATCH -J run-jijs
# partition
#SBATCH -p main
# 10 hours wall-clock time will be given to this job
#SBATCH -t 01:00:00
# Number of nodes
#SBATCH -N 1
# Number of MPI processes
#SBATCH -n 60
ml PDC/24.11
ml rspt/20250228-cpeGNU-24.11

export RSPT_SCRATCH=$SNIC_TMP

for i in 1 2 3 4 ; do

cp green.inp-$i green.inp
runs "srun -n 60 rspt" 10e-9 100
cp out out-jij-$i

echo "DONE" $i

done

echo "Job finished at `date` on `hostname`"
