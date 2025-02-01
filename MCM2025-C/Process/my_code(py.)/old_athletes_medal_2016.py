import pandas as pd

# 读取原始数据
df = pd.read_csv(r"C:\Users\weiyi\Desktop\athlete_2000.csv")

# 筛选2012年和2016年的数据
df_2012 = df[df['Year'] == 2012][['NOC', 'Name']]  # 2012年参赛运动员
df_2016 = df[df['Year'] == 2016][['NOC', 'Name', 'Medal']]  # 2016年参赛运动员及奖牌信息

# 找出2016年的老运动员（即在2012年也参赛的运动员）
df_2012_athletes = df_2012.drop_duplicates(subset=['NOC', 'Name'])  # 去重
df_2016_athletes = df_2016.drop_duplicates(subset=['NOC', 'Name'])  # 去重

# 合并2012年和2016年的数据，找出老运动员
old_athletes = pd.merge(
    df_2016_athletes,
    df_2012_athletes,
    on=['NOC', 'Name'],
    how='inner',  # 只保留2012年和2016年都参赛的运动员
    suffixes=('', '_2012')
)

# 筛选出获奖的老运动员
old_athletes_medals = old_athletes.dropna(subset=['Medal'])

# 统计每个国家的奖牌数量
medal_counts = old_athletes_medals.groupby(['NOC', 'Medal']).size().unstack(fill_value=0)

# 重命名列
medal_counts = medal_counts.rename(columns={'Gold': 'Gold', 'Silver': 'Silver', 'Bronze': 'Bronze'})

# 填充缺失的奖牌列为0
if 'Gold' not in medal_counts.columns:
    medal_counts['Gold'] = 0
if 'Silver' not in medal_counts.columns:
    medal_counts['Silver'] = 0
if 'Bronze' not in medal_counts.columns:
    medal_counts['Bronze'] = 0

# 选择需要的列
medal_counts = medal_counts[['Gold', 'Silver', 'Bronze']].reset_index()

# 按金牌、银牌、铜牌的顺序对国家进行排序
medal_counts = medal_counts.sort_values(by=['Gold', 'Silver', 'Bronze'], ascending=[False, False, False])

# 保存到CSV文件
medal_counts.to_csv(r"C:\Users\weiyi\Desktop\old_athletes_medals_2016_sorted.csv", index=False)

# 打印结果
print(medal_counts)