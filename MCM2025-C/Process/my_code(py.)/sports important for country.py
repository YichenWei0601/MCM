"""
[Part 1]
Top 10 sports for each country.
Export an csv. 

Show that for each country, which five sports 
are the most important for them. I am using 
first simple comparison then PCA and grey ana
-lysis. Note that we need:

    importance * number_of_award 

to judge the final effect.

"""


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load the medal counts data
medal_counts_data = pd.read_csv(r"C:\Users\weiyi\Desktop\country_event_scores.csv", encoding='latin1')
df = pd.DataFrame(medal_counts_data)
result = []

# 遍历每一行（每个国家）
for index, row in df.iterrows():
    # 获取运动和得分
    sports_scores = row[1:]  # 忽略第一列 (NOC)
    # 按得分排序
    sorted_sports = sports_scores.sort_values(ascending=False).head(10)
    # 替换得分小于 -0.3 的运动名称为 'Null'
    top_sports = [10 if sports_scores[sport] >= 0.12 else -10 for sport in sorted_sports.index]
    result.append(top_sports)

# 将结果转为DataFrame格式
result_df = pd.DataFrame(result, columns=[f"Top {i+1}" for i in range(10)], index=df['NOC'])
transposed_df = result_df.T

transposed_df.to_csv(r'C:\Users\weiyi\Desktop\top_sports_by_country.csv', index=True)

print("CSV file has been saved as 'top_sports_by_country.csv'.")