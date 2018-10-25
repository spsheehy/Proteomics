#-------------------------------------------------------------------------------
# Name:        Exosome_Correlation_Map
# Purpose:     Generate heatmap of Pearson correlation analysis on mass spec
#              data 
# Author:      spsheehy
#
# Created:     1/16/2017
#-------------------------------------------------------------------------------
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

sns.set(style="white")

data = pd.read_csv('Exosome_Run2_Filtered_Corr.csv', header=0, index_col=0)


# Compute the correlation matrix
corr = data.corr()

# Visualize data in a heatmap
# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr, annot=True, cmap="RdBu_r", vmax=1.0, vmin=-1.0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5}, ax=ax)
plt.show()