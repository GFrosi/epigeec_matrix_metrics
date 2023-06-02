import pandas as pd 
import sys
import os
from collections import Counter



def filter_raw_hist(epiatlas):
    """Receives epitlas pred.csv file.
    Returns three dictionaries associated
    to the raw samples."""

    df_epi = pd.read_csv(epiatlas, sep="\t", skiprows=1, low_memory=False)
    df_epi = df_epi.drop(df_epi.columns[0], axis=1).dropna(subset=['md5sum'])

    df_epi_slice = df_epi.loc[:,["md5sum","track_type","assay_epiclass","Predicted class assay_epiclass_1l_3000n"]]
    
    list_assay = ['h3k4me1','h3k4me3','h3k27me3',
                'h3k27ac','h3k9me3','h3k36me3',
                'input']

    #filter by RAW and TARGETS OF INTEREST
    df_epi_filter = df_epi_slice[df_epi_slice['assay_epiclass'].str.contains('|'.join(list_assay), na=False) & \
                                (df_epi_slice['track_type'].str.contains('raw'))] #6450 #add ctl_raw here to include the inputs and then generate the new matrix

    print(f'Your epiatlas df has {len(df_epi_filter)} associated to targets of interest and raw bigiwg.')



    #save dicts
    dict_epi = df_epi_filter.set_index('md5sum').to_dict()['assay_epiclass'] #6450
    dict_epi_pred = df_epi_filter.set_index('md5sum').to_dict()['Predicted class assay_epiclass_1l_3000n']# 6450
    dict_epi_count = Counter(dict_epi.values())


    return dict_epi, dict_epi_count, dict_epi_pred

   

    #==============================RUN THIS BLOCK IF YOU WANT TO SAVE THE .LIST FILE===================================================
    # list_md5 = df_epi_filter['md5sum'].tolist() #list to generate 100kb_filtered.list
    # res_epi = [os.path.join('/lustre07/scratch/frosig/local_ihec_data/EpiAtlas_dfreeze_100kb/',ele +'_100kb_all_none_value.hdf5') for ele in list_md5]
    # with open('/home/frosig/scratch/epigeec/epigeec_generator/output_100kb_ca/100kb_all_none_pearson_hist_epiatlas_raw_ctl.list', 'w') as f:
    #     f.write('\n'.join(res_epi))
    #==================================================================================================================================

