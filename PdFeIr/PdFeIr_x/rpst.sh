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
#SBATCH -t 24:00:00
# Number of nodes
#SBATCH -N 1
# Number of MPI processes
#SBATCH -n 124
start_time=$(date +%s)
echo "Job started at $(date) on $(hostname)"

ml PDC/24.11
ml rspt/20250228-cpeGNU-24.11

export RSPT_SCRATCH=$SNIC_TMP

runs "srun -n 124 rspt" 1e-10 500

end_time=$(date +%s)
runtime=$((end_time - start_time))

# Convert seconds to H:M:S
hours=$((runtime / 3600))
minutes=$(((runtime % 3600) / 60))
seconds=$((runtime % 60))
echo "Job finished at `date` on `hostname`"
echo "Total runtime: ${hours}h ${minutes}m ${seconds}s"
