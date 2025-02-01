"""
Creating the heatmap of the project.

The row is NOC, the column is the sports category, 
the numbers are the scores each country achieved in 
different sports. The map will be used in PCA, analyzing
the importance of sports for different country and
how well the countries perform.

The score is updated as:
(score - avg_score) / variation

"""


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Load the medal counts data
medal_counts_data = pd.read_csv(r"C:\Users\weiyi\Desktop\MCM2025\summerOly_athletes_sorted2.csv", encoding='latin1')

dataset = medal_counts_data[['Name','Sex','Team','NOC','Year','City','Sport','Event','Medal']]

medal_mapping = {
    'Gold': 8,
    'Silver': 4,
    'Bronze': 2,
    'No medal': 1
}

inter = {}
out = [[]]


noc_list = []
sport_list = []

sport_map = {}
noc_map = {}
for i in range(len(dataset)):    
    noc = dataset.iloc[i]['NOC'] 
    sport = dataset.iloc[i]['Sport']  
    if sport not in sport_list:
        sport_list.append(sport)
        sport_map[sport] = len(sport_list) - 1
    if noc not in noc_list:
        noc_list.append(noc)
        noc_map[noc] = len(noc_list) - 1


scores = np.zeros((len(noc_list), len(sport_list)), dtype=int)

# 累加分数
for i in range(len(dataset)):
    noc = noc_map[dataset.iloc[i]['NOC']]
    sport = sport_map[dataset.iloc[i]['Sport']]
    award = medal_mapping[dataset.iloc[i]['Medal']]
    scores[noc][sport] += award

# 创建 DataFrame
df = pd.DataFrame(scores, columns=sport_list)
df.insert(0, "NOC", noc_list)

# 计算按项目的平均值和标准化
# Step 1: 按列（体育项目）标准化
scaler = StandardScaler()
standardized_data = scaler.fit_transform(df.iloc[:, 1:])  # 跳过 NOC 列
standardized_df = pd.DataFrame(standardized_data, columns=sport_list)

# Step 2: 插入 NOC 列，构建完整的 DataFrame
standardized_df.insert(0, "NOC", noc_list)

# 边界处理：将标准化后的 NaN 值替换为 0（如得分全为 0 的项目）
standardized_df.fillna(0, inplace=True)

# save as csv
output_file = "C:/Users/weiyi/Desktop/country_event_scores.csv"
standardized_df.to_csv(output_file, index=False)

print(f"The file has been saved as {output_file}")

    