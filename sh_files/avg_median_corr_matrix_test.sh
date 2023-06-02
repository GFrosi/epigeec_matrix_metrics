#!/bin/bash
#SBATCH --account=def-jacquesp
#SBATCH --job-name=avg_median_100kb_pearson_test
#SBATCH --output=%x-%j.out
#SBATCH --time=00:20:00
#SBATCH --cpus-per-task=2
#SBATCH --mem=8G

source /lustre06/project/6007017/frosig/EpiClass/correlation_matrix_epigeec/env/bin/activate

echo "Starting script..."

python /lustre06/project/6007017/frosig/EpiClass/correlation_matrix_epigeec/filter_corr_matrix.py -d /lustre06/project/6007017/frosig/EpiClass/correlation_matrix_epigeec/data/Histones_43k_all_C-A_merged_pred_36kpred_manuscript_29-03-2023.tsv -m /lustre06/project/6007017/frosig/EpiClass/correlation_matrix_epigeec/data/test_matrix_final.mat -e /lustre06/project/6007017/frosig/EpiClass/correlation_matrix_epigeec/data/dfreeze_NN_merged_results.tsv -o /lustre06/project/6007017/frosig/EpiClass/correlation_matrix_epigeec/output/

echo "Script ended!"
