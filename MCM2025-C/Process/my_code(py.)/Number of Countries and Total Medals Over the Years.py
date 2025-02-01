"""
Showing the number of countries and total 
medals over the years. Discovering the 
growing trend.
"""

import matplotlib.pyplot as plt
import pandas as pd

# Load the medal counts data
medal_counts_data = pd.read_csv(r"C:\Users\weiyi\Downloads\dts\summerOly_medal_counts.csv", encoding='latin1')

# Data processing: group by Year to calculate the number of countries and total medals
dataset = medal_counts_data[['Rank', 'Total', 'Year']]
medal_sum = 0
country_count = 0
country_set = set()  # 用来统计唯一的国家
medal_y = []  # 用来存储奖牌总数
country_y = []  # 用来存储国家数量
year_x = []  # 用来存储年份

current_year = dataset.iloc[0]['Year']  # 初始化当前年份

for i in range(dataset.shape[0]):
    row = dataset.iloc[i]
    
    # 如果当前行的年份和当前年份相同，继续累加
    if row['Year'] == current_year:
        medal_sum += row['Total']  # 累加奖牌数量
        country_set.add(row['Rank'])  # 统计唯一国家
    else:
        # 当前年份结束，记录奖牌总数和国家数量
        medal_y.append(medal_sum)
        country_y.append(len(country_set))
        year_x.append(current_year)
        
        # 重置为新的年份
        current_year = row['Year']
        medal_sum = row['Total']  # 奖牌总数从当前行开始
        country_set = {row['Rank']}  # 当前行是新国家的开始

# 最后将最后一年的数据添加到列表中
medal_y.append(medal_sum)
country_y.append(len(country_set))
year_x.append(current_year)

# 打印结果
print("Years:", year_x)
print("Medal Totals:", medal_y)
print("Country Counts:", country_y)





# Plotting
fig, ax1 = plt.subplots(figsize=(12, 6))

# Plot country count on the primary y-axis
ax1.plot(year_x, country_y, label='Number of Countries Winning Medal', color='royalblue', marker='o')
ax1.set_xlabel('Year')
ax1.set_ylabel('Number of Countries Winning Medal', color='royalblue')
ax1.tick_params(axis='y', labelcolor='royalblue')

# Create a secondary y-axis for total medals
ax2 = ax1.twinx()
ax2.plot(year_x, medal_y, label='Total Medals', color='orange', marker='x')
ax2.set_ylabel('Total Medals', color='orange')
ax2.tick_params(axis='y', labelcolor='orange')

# Title and grid
plt.title('Number of Countries and Total Medals Over the Years')
ax1.grid(axis='x', linestyle='--', alpha=0.7)
fig.tight_layout()

# Show plot
plt.show()
