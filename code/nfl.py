#python module containing the main data and functions for NFL data analysis

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import json
import requests
from bs4 import BeautifulSoup as soup

import matplotlib.pyplot as plt
# plt.style.use('classic')
# %matplotlib inline

# import seaborn as sns
# sns.set()



root = r'C:\Users\Chill\nfl'
YEAR = 2020
file_path = f'C:\\Users\\Chill\\nfl\\play_by_play_{YEAR}.csv.gz'
file_path



#download from 2015 to 2020 and save data to folder
def download_and_store_data(year):    
    data = pd.read_csv('https://github.com/nflverse/nflverse-data/releases/download/pbp/' \
                       'play_by_play_' + str(year) + '.csv.gz',
                       compression= 'gzip', low_memory= False)
    #save to disk
    path = r'C:\Users\Chill\nfl'
    file_path = f'C:\\Users\\Chill\\nfl\\play_by_play_{year}.csv.gz'

    data.to_csv(file_path, compression='gzip', index=False)

#load data from disk
def load_data(year):
    filepath = f'C:\\Users\\Chill\\nfl\\play_by_play_{year}.csv.gz'
    data = pd.read_csv(filepath, compression='gzip', low_memory=False)                
    return data

def load_multi_years(all_data=True):
    if all_data:
        #list all downloaded data
        data = [file for file in os.listdir(root) if 'play_by_play' in file]
    
        #for each year, read into a df
        df = pd.DataFrame()
        dfs = []
        for file in data:
            df_year = pd.read_csv(file, compression='gzip', low_memory=False)
            dfs.append(df_year)
#         dfs = [pd.read_csv(file, compression='gzip') for file in data]
        df = pd.concat(dfs)
        return df
        #concat all dfs in list using concat
        
#32 teams
#official team abbreviations
#Los Angeles Rams is LA, not LAR
teams = ['NYJ', 'LA', 'CAR', 'SEA', 'MIN', 
         'HOU', 'WAS', 'ARI', 'LAC', 'MIA', 
         'ATL', 'TEN', 'DET', 'CIN', 'CHI', 
         'DAL', 'LV', 'NYG', 'GB', 'DEN', 
         'JAX', 'KC', 'BAL', 'PHI', 'PIT', 
         'CLE', 'SF', 'NO', 'BUF', 'NE', 
         'TB', 'IND']
