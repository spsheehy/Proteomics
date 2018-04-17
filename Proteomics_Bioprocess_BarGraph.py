#-------------------------------------------------------------------------------
# Name:        Proteomics_Bioprocess_BarGraph
# Purpose:     Generate bar graphs illustrating break down of bioprocess  
#              composition of mass spec protein expression data
# Author:      spsheehy
#
# Created:     08/03/2017
# Copyright:   (c) spsheehy 2017
#-------------------------------------------------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':

    # List of input file names
    filenames = [  
                 'BOC_Linked_Proteomap_Input.csv','BOC_Solo_Proteomap_Input.csv',
                 'AP_Out_Proteomap_Input.csv', 'AP_In_Proteomap_Input.csv',
                 'Endo_Out_Proteomap_Input.csv','Endo_In_Proteomap_Input.csv',
                ]
    conditions = ['Neuronal C. Linked', 'Neuronal C. Unlinked', 'Peri/Astro Linked', 'Peri/Astro Unlinked', 'Endo Linked', 'Endo Unlinked']
    sample_info = zip(filenames,conditions)
    processed_samples = pd.DataFrame()
    for filename, condition in sample_info:
        data = pd.DataFrame.from_csv(filename)
        total_abundance = data['Abundance'].sum()
        bioprocess = pd.Series(data['Level 2'].values.ravel()).unique()
        columns = ['Process Abundance','Percent of Dataset']
        processed_data = pd.DataFrame(index=bioprocess, columns=columns)
        for process in bioprocess:
            process_abundance = data.loc[data['Level 2'] == process]['Abundance'].sum()
            processed_data.set_value(process,columns[0],process_abundance)
            percent_abundance = (process_abundance/total_abundance)*100
            processed_data.set_value(process,columns[1],percent_abundance)
        sample_data = pd.Series(data = processed_data['Percent of Dataset'], index = processed_data.index)
        processed_samples = processed_samples.append(sample_data, ignore_index=True)
        #output_file = "%s_%s.csv" % (condition, 'Output')
        #processed_data.to_csv(output_file)
    
    processed_samples = processed_samples.transpose()
    processed_samples.columns = conditions
    processed_samples.to_csv('Processed_Samples.csv')
    
    colors = {'Biosynthesis':'sienna',
              'Cell Growth and Death':'green', 
              'Cellular Community':'gold',
              'Central Carbon Metabolism':'sandybrown',
              'Cytoskeleton':'crimson',
              'DNA Maintenance':'lightskyblue',
              'Development':'palevioletred', 
              'Energy Metabolism':'saddlebrown',
              'Folding, Sorting, and Degradation':'midnightblue',
              'Immune System':'plum',
              'Membrane Transport':'turquoise',
              'Metabolism':'darkorange', 
              'Neurodegenerative Diseases':'black', 
              'Signal Transduction':'teal',
              'Signaling Molecules and Interaction':'lightseagreen', 
              'Transcription':'navy',
              'Translation':'indigo',
              'Vesicular transport':'maroon', 
              'Nervous System':'grey',
              'Immune Diseases':'silver'
             }    
            
    processed_samples = processed_samples.transpose()
    processed_samples.plot(kind='barh', color=map(colors.get,processed_samples.columns), stacked=True)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.xlabel('Percent of Dataset (%)', fontsize=20, weight='bold')
    #plt.ylim(0,3)
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., fontsize=14)
    plt.show()