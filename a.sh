#! /bin/bash
#SBATCH --partition=gpu
#SBATCH --output=slurm_logs/slurm-%A-%a.out
#SBATCH --error=slurm_logs/slurm-%A-%a.err
#SBATCH --job-name=jz-glue
#SBATCH --gres=gpu:a40:1
#SBATCH --mem=30g
#SBATCH --cpus-per-task=4
#SBATCH --time=48:00:00
#SBATCH --array=0

python fastrun.py --data=XsumFaith
python fastrun.py --data=Xsum-Sota
python fastrun.py --data=SummEval