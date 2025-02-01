import matplotlib.pyplot as plt
import pandas as pd

# Load the medal counts data
medal_counts_data = pd.read_csv(r"C:\Users\weiyi\Desktop\summerOly_athletes.csv", encoding='latin1')

dataset = medal_counts_data[['Name', 'NOC', 'Year']]
dataset = dataset.sort_values(by=['Name', "NOC", "Year"])

out = []

for i in range(len(dataset)):
    if i == 0:
        name = dataset.iloc[i]['Name']
        fyear = dataset.iloc[i]['Year']
        noc = dataset.iloc[i]['NOC']
    if dataset.iloc[i]['Name'] != name or dataset.iloc[i]['NOC'] != noc:
        name = dataset.iloc[i]['Name']
        fyear = dataset.iloc[i]['Year']
        noc = dataset.iloc[i]['NOC']
    times = 1 + (dataset.iloc[i]['Year'] - fyear) // 4
    out.append({
            "NOC": noc,
            "Year": dataset.iloc[i]['Year'],
            "Name": name, 
            "Times": times if times < 7 else 1
            
        })
    

result_df = pd.DataFrame(out)

# 保存为 CSV 文件
result_df.to_csv("C:/Users/weiyi/Desktop/attending_times.csv", index=False)
    
