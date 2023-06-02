#!/bin/bash
#SBATCH --account=def-jacquesp
#SBATCH --job-name=avg_median_100kb_pearson
#SBATCH --output=%x-%j.out
#SBATCH --time=48:00:00
#SBATCH --cpus-per-task=24
#SBATCH --mem=30G

source /lustre06/project/6007017/frosig/EpiClass/correlation_matrix_epigeec/env/bin/activate

echo "Starting script..."

python /lustre06/project/6007017/frosig/EpiClass/correlation_matrix_epigeec/filter_corr_matrix.py -d /lustre06/project/6007017/frosig/EpiClass/correlation_matrix_epigeec/data/Histones_43k_all_C-A_merged_pred_36kpred_manuscript_29-03-2023.tsv -m /lustre06/project/6007017/frosig/EpiClass/correlation_matrix_epigeec/data/100kb_all_none_pearson.mat -e /lustre06/project/6007017/frosig/EpiClass/correlation_matrix_epigeec/data/dfreeze_NN_merged_results.tsv -o /lustre06/project/6007017/frosig/EpiClass/correlation_matrix_epigeec/output/

echo "Script ended!"
