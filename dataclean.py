import numpy as np
import os
import pandas as pd

list_of_data = ['Athleticism', 'ClinicianReport']
for folder in list_of_data:
    df_list = []
    for file in os.listdir('data/' + folder):
        if '.csv' in file:
            single_df = pd.read_csv('data/' + folder + '/' + file)
            df_list.append(single_df)
        
    df = pd.concat(df_list)
    df.to_csv('data/' + folder + '.csv',  index=False )  


    