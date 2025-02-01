import matplotlib.pyplot as plt
import pandas as pd

# Load the medal counts data
medal_counts_data = pd.read_csv(r"C:\Users\weiyi\Desktop\summerOly_athletes.csv", encoding='latin1')

# Data processing: group by Year to calculate the number of countries and total medals
dataset = medal_counts_data[['NOC', 'Year', 'Sport', 'Medal']]
# 存储最终结果
results = []

# 记录每个国家每个项目的首次获奖状态和参与信息
recorded = {}

# 按国家和年份排序数据
dataset = dataset.sort_values(by=["NOC", "Year"])

# 遍历数据集
for i in range(len(dataset)):
    noc = dataset.iloc[i]['NOC']
    year = dataset.iloc[i]['Year']
    sport = dataset.iloc[i]['Sport']
    medal = dataset.iloc[i]['Medal']
    
    # 初始化记录
    if noc not in recorded:
        recorded[noc] = {}
    
    if sport not in recorded[noc]:
        recorded[noc][sport] = {"first_medal_year": 0, "record": {}, "year": []}
    
    # 如果该年已记录过，跳过
    #if year in recorded[noc][sport]["recorded_years"]:
    #    recorded[noc][sport]["participants"][year] += 1
    #    continue    
    
    # 如果是首次获奖年份，记录获奖信息
    if recorded[noc][sport]["first_medal_year"] != 0 and int(year) > int(recorded[noc][sport]["first_medal_year"]):
        continue

    if medal != "No medal" and recorded[noc][sport]["first_medal_year"] == 0:
        recorded[noc][sport]["first_medal_year"] = year

    if year not in recorded[noc][sport]["year"]:
        recorded[noc][sport]["record"][year] = 0

    # 添加到结果列表
        results.append({
            "NOC": noc,
            "Year": year,
            "Sport": sport,
            "Medal": medal,
            "Participants": recorded[noc][sport]["record"][year]
        })
    for i in range(len(results)):
        if results[i]["NOC"] == noc and results[i]["Year"] == year and results[i]["Sport"] == sport:
            results[i]["Participants"] += 1
            if results[i]["Medal"] == "No medal":
                results[i]["Medal"] = medal
    
    # 标记该年已记录
    recorded[noc][sport]["year"].append(year)

    # 一旦获得奖牌，跳过后续年份
  

# 转换结果为 DataFrame
result_df = pd.DataFrame(results)

# 保存为 CSV 文件
result_df.to_csv("C:/Users/weiyi/Desktop/annual_medal_participants.csv", index=False)







"""
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
"""
