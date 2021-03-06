#-------------------------------------------------------------------------------
# Name:        Exosome_Heatmap
# Purpose:     Generate expression heatmaps of cardioprotection-related
#              proteins for Fig.2, panels A and B
# Author:      spsheehy
#
# Created:     06/06/2017
# Copyright:   (c) spsheehy 2017
#-------------------------------------------------------------------------------
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

sns.set(style="white")

#data_file = 'Exosome_Run2_Class_Heatmap_No_Cardio3.csv'
data_file = 'Exosome_Run2_Preconditioning.csv'
input_data = pd.read_csv(data_file, index_col=0)
input_data = input_data.applymap(np.log2)
cg = sns.heatmap(input_data, vmax=20, cmap="Blues", linewidths=2.0, cbar=False)
plt.setp(cg.yaxis.tick_right())
plt.setp(cg.yaxis.get_majorticklabels(), rotation=0)
plt.rc('font',weight='bold', size=32)
plt.show()
#for prot_class in input_data.keys():
#    # Log2 transform data
#    class_data = input_data[prot_class] 
#    class_data = class_data.applymap(np.log2)
#    # Visualize data in a heatmap
#    cg = sns.heatmap(class_data, cmap="Blues")
#    plt.setp(cg.yaxis.get_majorticklabels(), rotation=0)
#    plt.rc('font',weight='bold', size=16)
#    #cg = sns.clustermap(data, method="average", metric="correlation", cmap = "Blues")
#    #plt.setp(cg.ax_heatmap.yaxis.get_majorticklabels(), rotation=0)
#    sns.plt.savefig('output.svg')