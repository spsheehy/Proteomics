#-------------------------------------------------------------------------------
# Name:        Exosome_Protective_Correlation_Map
# Purpose:     Generate Pearson correlation map for "protective" groups of 
#              proteins illustrated in Fig 2 expression heatmaps
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

data = pd.read_csv('Exosome_Run2_Protective_Corr_Input2.csv', header=0, index_col=0)


# Compute the correlation matrix
corr = data.corr()

# Visualize data in a heatmap
# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr, annot=True, cmap="RdBu_r", vmax=1.0, vmin=-1.0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5}, ax=ax)
plt.show()