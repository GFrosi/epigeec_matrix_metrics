import pandas as pd 
import sys
import os
from collections import Counter



def filter_100kb_list(dict_ca_filter):
    """Receives a dict (e.g just histones and inputs).
    Retuns a txt file containing the path to the hdf5s
    associated to histones and inputs. This file can 
    be used to lauch the epigeec."""

    file_n = open('/home/frosig/scratch/epigeec/epigeec_generator/output_100kb_ca/100kb_all_none_pearson.list', 'r')
    samples_name = [os.path.basename(sample.strip()).split('_')[0] for sample in file_n] #get just the name to match to our keys

    res = [os.path.join('/lustre07/scratch/frosig/local_ihec_data/C-A_100kb/hg38/hdf5/100kb_all_none/',ele +'_100kb_all_none_value.hdf5') for ele in samples_name if ele in dict_ca_filter.keys()]
    #dict_ca_filter = 26238
    #res = 26238

    with open('/home/frosig/scratch/epigeec/epigeec_generator/output_100kb_ca/100kb_all_none_pearson_hist.list', 'w') as f:
        f.write('\n'.join(res))



def generate_dict_filter(dict_ca):
    """Receives a dict. Returns a
    filtered dict (targets of interest)
    using another function (filtering_dict_pair)."""

    return dict(filter(filtering_dict_pair, dict_ca.items()))
 


def filtering_dict_pair(pair):
    """Receives a pair (k,v) from a dict.
    Returns True or False if the v is part
    of the list of interest.
    """

    list_assay = ['h3k4me1','h3k4me3','h3k27me3',
                'h3k27ac','h3k9me3','h3k36me3',
                'input']

    k, v = pair

    if v in list_assay:
        return True  # keep pair in the filtered dictionary
    else:
        return False  # filter pair out of the dictionary
 


def write_dict_count(dict_ca_count):
    """Receives a dict_count
    and returns a txt."""

    df_ca_count = pd.DataFrame(dict_ca_count.items(), columns=['Assay','Count'])
    df_ca_count.to_csv('df_ca_count.tsv', sep='\t', index=False)
    

def create_dict_ca(df):
    """Receives a df (tsv) and returns
    a dictionary {srx:assay}"""

    df = pd.read_csv(df, sep="\t")
    pat = r'\w+' #to ignore '----' and NaN; just keep SRX/DRX/ERX samples
    df_pred = df[df['md5sum'].str.contains(pat)]
    df_pred['md5sum'] = df_pred['md5sum'].str.replace('-bw','') #removing -bw
    dict_ca = df_pred.set_index('md5sum').to_dict()['assay_epiclass']
    dict_ca_pred = df_pred.set_index('md5sum').to_dict()['Predicted class_assay11']
    dict_ca_count = Counter(dict_ca.values())  #count ca values



    return dict_ca, dict_ca_count, dict_ca_pred