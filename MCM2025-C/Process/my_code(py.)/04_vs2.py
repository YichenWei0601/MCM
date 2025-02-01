'''
多人,考虑了关键词+项目名
'''

import pandas as pd

# 读取CSV文件
df = pd.read_csv(r"C:\Users\weiyi\Desktop\summerOly_athletes_2000y.csv")

# 强制转换Year列为int类型
df['Year'] = df['Year'].astype(int)

# 定义多人项目的关键词列表
team_keywords = ['team', 'doubles', 'three', 'fours', 'group', 'duet']

# 定义多人项目的Event列表
team_events = [
    "Athletics Men's 4 x 100 metres Relay",
    "Athletics Men's 4 x 400 metres Relay",
    "Athletics Women's 4 x 100 metres Relay",
    "Athletics Women's 4 x 400 metres Relay",
    "Basketball Men's Basketball",
    "Basketball Women's Basketball",
    "Beach Volleyball Men's Beach Volleyball",
    "Beach Volleyball Women's Beach Volleyball",
    "Cycling Men's Team Pursuit, 4,000 metres",
    "Cycling Women's Team Pursuit",
    "Equestrian Mixed Three-Day Event, Team",
    "Equestrian Mixed Jumping, Team",
    "Fencing Men's Foil, Team",
    "Fencing Men's epee, Team",
    "Fencing Women's Foil, Team",
    "Fencing Women's Sabre, Team",
    "Football Men's Football",
    "Football Women's Football",
    "Gymnastics Men's Team All-Around",
    "Gymnastics Women's Team All-Around",
    "Handball Men's Handball",
    "Handball Women's Handball",
    "Hockey Men's Hockey",
    "Hockey Women's Hockey",
    "Rowing Men's Coxed Eights",
    "Rowing Men's Coxed Fours",
    "Rowing Men's Coxless Fours",
    "Rowing Men's Coxless Pairs",
    "Rowing Men's Double Sculls",
    "Rowing Men's Lightweight Double Sculls",
    "Rowing Men's Quadruple Sculls",
    "Rowing Women's Coxed Eights",
    "Rowing Women's Coxed Fours",
    "Rowing Women's Coxless Fours",
    "Rowing Women's Coxless Pairs",
    "Rowing Women's Double Sculls",
    "Rowing Women's Lightweight Double Sculls",
    "Rowing Women's Quadruple Sculls",
    "Rugby Men's Rugby",
    "Rugby Women's Rugby",
    "Sailing Men's Two Person Dinghy - 470 Team",
    "Sailing Women's Two Person Dinghy - 470 Team",
    "Swimming Men's 4 x 100 metres Freestyle Relay",
    "Swimming Men's 4 x 200 metres Freestyle Relay",
    "Swimming Men's 4 x 100 metres Medley Relay",
    "Swimming Women's 4 x 100 metres Freestyle Relay",
    "Swimming Women's 4 x 200 metres Freestyle Relay",
    "Swimming Women's 4 x 100 metres Medley Relay",
    "Synchronized Swimming Women's Duet",
    "Synchronized Swimming Women's Team",
    "Table Tennis Men's Doubles",
    "Table Tennis Women's Doubles",
    "Table Tennis Men's Team",
    "Table Tennis Women's Team",
    "Volleyball Men's Volleyball",
    "Volleyball Women's Volleyball",
    "Water Polo Men's Water Polo",
    "Water Polo Women's Water Polo"
]

# 初始化Division列，默认值为1
df['Division'] = 1

# 筛选出需要处理的多人项目行
team_df = df[
    df['Event'].isin(team_events) |  # Event在列表中
    df['Event'].str.lower().str.contains('|'.join(team_keywords))  # Event包含关键词
]

# 对team_df进行处理
for _, group in team_df.groupby(['Sex', 'Team', 'NOC', 'Year', 'City', 'Sport', 'Event', 'Medal']):
    division_size = len(group)  # 计算每组的人数
    df.loc[group.index, 'Division'] = division_size  # 更新Division列

# 导出到out.csv
df.to_csv(r"C:\Users\weiyi\Desktop\athlete_2000.csv", index=False)