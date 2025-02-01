import pandas as pd

# 读取CSV文件
df = pd.read_csv(r"C:\Users\weiyi\Desktop\summerOly_medal_counts.csv")

# 初始化一个集合，用于存储曾经获奖的国家
awarded_countries = set()

# 初始化一个字典，用于存储每年新获奖的国家数量
new_awarded_counts = {}

# 按年份排序
df = df.sort_values(by='Year')

# 遍历每一行数据
for year, group in df.groupby('Year'):
    # 获取当前年份获奖的国家
    current_awarded = set(group[group['Total'] > 0]['NOC'])
    
    # 计算新获奖的国家
    new_awarded = current_awarded - awarded_countries
    
    # 更新曾经获奖的国家集合
    awarded_countries.update(new_awarded)
    
    # 记录新获奖的国家数量
    new_awarded_counts[year] = len(new_awarded)

# 将结果转换为DataFrame
result_df = pd.DataFrame(list(new_awarded_counts.items()), columns=['Year', 'New_Awarded_Count'])

# 输出到CSV文件
result_df.to_csv(r"C:\Users\weiyi\Desktop\new_award_country0.csv", index=False)