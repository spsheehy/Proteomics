#-------------------------------------------------------------------------------
# Name:        Proteomics_PCA_Scatterplots
# Purpose:     Generate scatterplots of mass spec PCA
#
# Author:      spsheehy
#
# Created:     5/17/2017
# Copyright:   (c) spsheehy 2017
#-------------------------------------------------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


def MergeDataFrames(DF1, DF2, join_type='outer'):
    Combined = pd.concat([DF1,DF2], join=join_type)
    Combined = Combined.groupby(Combined.index).first().dropna()
    return Combined


def PCA_Graph(csv_input_filename, fig_output_filename):
    # Read in mass spec data from samples of interest
    input_data = pd.read_csv(csv_input_filename)
    # Get the numerical values to perform PCA on
    num_data = np.array(input_data._get_numeric_data())
    # Create a list of the unique bioprocess IDs present in the data set
    input_bioprocess = pd.unique(input_data.Bioprocess.ravel())
    # Perform PCA on the numerical data
    data_pca = PCA(n_components=2)
    pca_results = data_pca.fit(num_data).transform(num_data)
    # Add the eigenvalues from the PCA to the input data set and output to a
    # new csv file
    input_data['PCA 1st PC'] = pca_results[:,0]
    input_data['PCA 2nd PC'] = pca_results[:,1]
    
    # Graph the results of the PCA on a scatter plot, labeling each point
    # according to its corresponding bioprocess ID
    # Color marker lables for the scatterplot (one for each unique bioprocess ID)
    color_markers = ['gv', 'bd', 'm^', 'ks', 'y<', 'rh', 'c>', 'gp', 'bs', 'rd', 'k^', 'yo', 'gh','bv', 'rv', 'gd', 'y^', 'cs', 'go', 'b^', 'mo', 'ko', 'yv', 'ro', 'cv']
    color_marker_dict = dict(zip(input_bioprocess, color_markers))
    # To keep the legend legible, only add bioprocess ID label the first time
    # it is encountered
    first_time = dict(zip(input_bioprocess, np.repeat([True], len(input_bioprocess))))
    # Create a font object to control the font parameters for the plot axis labels
    font = {'family' : 'arial',
            'weight' : 'bold',
            'size'   : 28}
    plt.rc('font', **font)
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    #sub = fig.add_subplot(1,1,1)
    for i in range(len(pca_results)):
        if(first_time[input_data['Bioprocess'][i]]):
            ax.scatter(pca_results[i, 0], pca_results[i, 1], s=70, c=color_marker_dict[input_data['Bioprocess'][i]][0], marker=color_marker_dict[input_data['Bioprocess'][i]][1],label=input_data['Bioprocess'][i])
            first_time[input_data['Bioprocess'][i]] = False
        else:
            ax.scatter(pca_results[i, 0], pca_results[i, 1], s=70, c=color_marker_dict[input_data['Bioprocess'][i]][0], marker=color_marker_dict[input_data['Bioprocess'][i]][1])
    # Label scatterplot axes and add bioprocess ID legend to figure
    ax.set_xlabel('First Principle Component', fontsize=18, weight='bold')
    ax.set_xlim([-2,8])
    ax.set_ylabel('Second Principle Component', fontsize=18, weight='bold')
    ax.set_ylim([-2,4])
    ax.tick_params(axis='both', which='major', labelsize=18)
    lgd = ax.legend(bbox_to_anchor=(1.05, 1), loc=2, ncol=1, borderaxespad=0.)
    fig.savefig(fig_output_filename, bbox_extra_artists=(lgd,), bbox_inches='tight')
    plt.show()

    return input_data


def main():
    pass

if __name__ == '__main__':
    main()

    # List of mass spec data input file names, and PCA graph output file names
    # for each data set to be analyzed
    filenames = [['PCA_Input_Data_1.csv','PCA_Scatterplot_Image_1.png','PCA_Results_Output_File_1.csv'],
                 ['PCA_Input_Data_2.csv','PCA_Scatterplot_Image_2.png','PCA_Results_Output_File_2.csv']]

    # Run PCA on each input file in the filenames list and save the output
    # PCA graph to an image file
    for in_file, out_file, pca_out_file in filenames:
        analysis_results = PCA_Graph(in_file, out_file)
        analysis_results.to_csv(pca_out_file)