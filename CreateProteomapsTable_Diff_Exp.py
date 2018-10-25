#-------------------------------------------------------------------------------
# Name:        Create_Proteomaps_Table_Diff_Exp
# Purpose:     Generate association table of Uniprot IDs to KEGG orthology terms
#              for differentially expressed proteins in exosome proteomics data
# Author:      spsheehy
#
# Created:     06/06/2017
# Copyright:   (c) spsheehy 2017
#-------------------------------------------------------------------------------
import pandas as pd


def MergeDataFrames(DF1, DF2, join_type='outer'):
    Combined = pd.concat([DF1,DF2], join=join_type)
    Combined = Combined.groupby(Combined.Gene).first().dropna()
    return Combined
             

filenames = [['Diff_Exp_Proteomaps_Input.csv','Human_Proteomaps_Simple2.csv', 
              'Exosome_Run2_Diff_Exp_Proteomap_Table.csv']
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