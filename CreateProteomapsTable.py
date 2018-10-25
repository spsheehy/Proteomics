#-------------------------------------------------------------------------------
# Name:        CreateProteomapsTable
# Purpose:     Generate input files for downstream analysis from raw data files
#              
# Author:      spsheehy
#
# Created:     12/27/2016
#-------------------------------------------------------------------------------
import pandas as pd


def MergeDataFrames(DF1, DF2, join_type='outer'):
    Combined = pd.concat([DF1,DF2], join=join_type)
    #Combined = Combined.groupby(Combined.Accession).first().dropna()
    Combined = Combined.groupby(Combined.Accession).first()
    return Combined
             
filenames = [['Exosome_Data_1.csv','Exosome_Data_2.csv', 'Exosome_Data_Combined_2.csv']
            ]

            
for data_file, bio_file, out_file in filenames:
    data = pd.read_csv(data_file)
    bio = pd.read_csv(bio_file)
    combined_files = MergeDataFrames(data, bio)
    combined_files.to_csv(out_file)
    
    
    # This code was used one time to create the 'Human_Proteomaps_Simple2.csv' file
    #gene_info = bio['Level 4'].str.rsplit(':', expand=True, n=1)
    #bio['Gene Symbol'] = gene_info[0]
    #bio['Gene'] = gene_info[1]