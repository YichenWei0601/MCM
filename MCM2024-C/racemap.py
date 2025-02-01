"""
Creating the race map of the project.

In the former 5 Olympic games, how well do each
country rank and show the trend of it.

"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load the medal counts data
medal_counts_data = pd.read_csv(r"C:\Users\weiyi\Desktop\summerOly_medal_recent5y.csv", encoding='latin1')

dataset = medal_counts_data[['Rank','NOC','Year']]
noc_list = []
year_list = []

year_map = {}
noc_map = {}
for i in range(len(dataset)):    
    noc = dataset.iloc[i]['NOC'] 
    year = dataset.iloc[i]['Year']  
    if year not in year_list:
        year_list.append(year)
        year_map[year] = len(year_list) - 1
    if noc not in noc_list:
        noc_list.append(noc)
        noc_map[noc] = len(noc_list) - 1


ranklist = np.full((len(noc_list), len(year_list)), 0, dtype=int)

for i in range(len(dataset)):
    noc = noc_map[dataset.iloc[i]['NOC']]
    year = year_map[dataset.iloc[i]['Year']]
    rank = dataset.iloc[i]['Rank']
    ranklist[noc][year] = 16-rank

df = pd.DataFrame(ranklist, columns=year_list)
df.insert(0, "NOC", noc_list)

output_file = "C:/Users/weiyi/Desktop/country_medal_5y.csv"
df.to_csv(output_file, index=False)

print(f"The file has been saved as {output_file}")