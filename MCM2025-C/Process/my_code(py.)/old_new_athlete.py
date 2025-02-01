"""
xiangchuyang needed.
"""
import pandas as pd

# 读取CSV文件
df = pd.read_csv(r"C:\Users\weiyi\Desktop\athlete_2000.csv")

# 按国家、运动、年份分组
grouped = df.groupby(['NOC', 'Sport', 'Year']).size().unstack(fill_value=0)

# 计算每年新老运动员的数量
old_new = pd.DataFrame()

for year in range(df['Year'].min() + 1, df['Year'].max() + 1):
    prev_year = year - 1
    current_athletes = df[df['Year'] == year].groupby(['NOC', 'Sport'])['Name'].apply(set)
    prev_athletes = df[df['Year'] == prev_year].groupby(['NOC', 'Sport'])['Name'].apply(set)
    
    merged = pd.merge(current_athletes, prev_athletes, on=['NOC', 'Sport'], how='outer', suffixes=('_current', '_prev'))
    
    merged['old'] = merged.apply(lambda x: len(x['Name_current'].intersection(x['Name_prev'])) if isinstance(x['Name_current'], set) and isinstance(x['Name_prev'], set) else 0, axis=1)
    merged['new'] = merged.apply(lambda x: len(x['Name_current'].difference(x['Name_prev'])) if isinstance(x['Name_current'], set) and isinstance(x['Name_prev'], set) else len(x['Name_current']) if isinstance(x['Name_current'], set) else 0, axis=1)
    
    merged['Year'] = year
    old_new = pd.concat([old_new, merged.reset_index()])

# 重新排列列
old_new = old_new[['NOC', 'Sport', 'Year', 'old', 'new']]

# 将 old 和 new 列转换为整数类型
old_new['old'] = old_new['old'].astype(int)
old_new['new'] = old_new['new'].astype(int)

# 保存到新的CSV文件
old_new.to_csv(r"C:\Users\weiyi\Desktop\old_new_athlete_2000.csv", index=False)
