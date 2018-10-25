#-------------------------------------------------------------------------------
# Name:        Exosome_Marker_Graph
# Purpose:     Generate heatmap of mass spec expression values for exosome
#              marker proteins
# Author:      spsheehy
#
# Created:     1/12/2017
#-------------------------------------------------------------------------------
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

sns.set(style="white")

data = pd.read_csv('Exosome_Markers.csv', header=0, index_col=0)

# Log2 transform data 
data = data.applymap(np.log2)
# Visualize data in a heatmap
cg = sns.heatmap(data, cmap = "Blues")
plt.setp(cg.ax_heatmap.yaxis.get_majorticklabels(), rotation=0)
plt.show()