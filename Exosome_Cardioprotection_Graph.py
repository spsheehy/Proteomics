#-------------------------------------------------------------------------------
# Name:        Exosome_Cardioprotection_Graph
# Purpose:     Generate heatmap of mass spec expression values for exosome
#              cardioprotection proteins
# Author:      spsheehy
#
# Created:     1/17/2017
#-------------------------------------------------------------------------------
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

sns.set(style="white")

data_file = 'Exosome_Run2_Class_Heatmap.xlsx'
input_data = pd.read_excel(data_file, sheetname=None, index_col=0)

for prot_class in input_data.keys():
    # Log2 transform data 
    prot_class = prot_class.applymap(np.log2)
    # Visualize data in a heatmap
    cg = sns.heatmap(prot_class, cmap="Blues")
    plt.setp(cg.yaxis.get_majorticklabels(), rotation=0)
    plt.rc('font',weight='bold', size=16)
    #cg = sns.clustermap(data, method="average", metric="correlation", cmap = "Blues")
    #plt.setp(cg.ax_heatmap.yaxis.get_majorticklabels(), rotation=0)
    sns.plt.show()