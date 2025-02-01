"""
athlete after certain year.
csv. generator.
"""

import pandas as pd

# 读取原始数据
file_path = r"C:\Users\weiyi\Desktop\summerOly_athletes(3).csv"
athletes_data = pd.read_csv(file_path)

# 筛选年份大于1990年的数据
filtered_data = athletes_data[athletes_data['Year'] > 1999]

# 选择需要的列
filtered_data = filtered_data[['Name','Sex','Team','NOC','Year','City','Sport','Event','Medal','Division']]

# 保存筛选后的数据到新的CSV文件
output_path = r"C:\Users\weiyi\Desktop\summerOly_athletes_filtered.csv"
filtered_data.to_csv(output_path, index=False)

# 打印筛选后的数据（可选）
print('Done')