"""
[Part 2]
PCA part. 

Show that for each country, which five sports 
are the most important for them. I am using 
first simple comparison (already done) then 
PCA and grey analysis. Note that we need:

    importance * number_of_award 

to judge the final effect.

"""

import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\weiyi\Desktop\country_event_scores_promoted.csv", encoding='latin1')

# PCA
data_without_noc = data.drop(columns=['NOC'])  # 假设列名为 'noc'

# 确保数据只有数值列，如果有非数值列，则删除它们
data_numeric = data_without_noc.select_dtypes(include=[float, int])

# 如果有缺失值，可以选择填充或删除（这里用均值填充）
data_numeric = data_numeric.fillna(data_numeric.mean())

# 初始化 PCA 模型
pca = PCA()

# 对数据进行 PCA 拟合
pca.fit(data_numeric)

# 获取主成分解释方差比例
explained_variance_ratio = pca.explained_variance_ratio_

# 计算累计解释方差
cumulative_explained_variance = explained_variance_ratio.cumsum()

# 获取主成分负载（特征向量）
components = pca.components_

# 输出主成分1、2的百分比和累计解释方差
print(f"The proportion of variance explained by the principal component 1: {explained_variance_ratio[0] * 100:.2f}%")
print(f"The proportion of variance explained by the principal component 2: {explained_variance_ratio[1] * 100:.2f}%")
print(f"The proportion of variance explained by the principal component 3: {explained_variance_ratio[2] * 100:.2f}%")
print(f"The proportion of variance explained by the principal component 4: {explained_variance_ratio[3] * 100:.2f}%")
print(f"The proportion of variance explained by the principal component 5: {explained_variance_ratio[4] * 100:.2f}%")
print(f"Cumulative proportion of variance explained: {cumulative_explained_variance[5] * 100:.2f}%")

# 输出主成分负载（特征向量）
print("\n主成分负载（特征向量）:")
for i, component in enumerate(components[:5], start=1):
    print(f"主成分{i}: {component}")



# 绘制解释方差比例
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 5))
plt.bar(range(1, len(explained_variance_ratio) + 1), explained_variance_ratio * 100, alpha=0.7, label='Individual Principal Components', color='#FF7029')
plt.step(range(1, len(cumulative_explained_variance) + 1), cumulative_explained_variance * 100, where='mid', label='Cumulative Explained Variance', color='#373BF1')
plt.xlabel('Principal Component Number')
plt.ylabel('Explained Variance Ratio (%)')
plt.title('PCA Explained Variance Ratio')
plt.legend()
plt.show()

"""
Here are the eigenvector. find the max ones (*4)
[0.19497447] 0.09755302 0.11352208 0.12804369 0.13548627 [0.20933777]
0.11218112 0.09643371 0.16814264 0.15262316 0.17468533 [0.18299946]
0.11006412 0.12880526 0.14534361 0.17400696 0.12653643 0.16936166
0.18094389 0.16545179 0.16750774 0.0706089   0.10545005 0.15974746
0.08540464 0.07784959 0.13503949 [0.18551017] 0.17509528 0.10009698
0.16483959 0.13282575 0.1342888  0.1746402  0.12346536 0.1403935
0.17725507 0.17257852 0.16781777 0.14102036 0.09304768 0.1121504
0.15855367 0.17741872 0.1438774  0.16175131

'''1, 6, 12, 28'''


-0.01970657 -0.20740673  [0.18867354]  0.07711139  0.0866602  -0.01272848
 -0.23492864  0.1632446   0.10064752  0.00541485 -0.16528485 -0.20656293
  [0.24355516]  0.15042786  0.01349413 -0.20843924 -0.10125868  0.1049963
 -0.04963975 -0.14525791 -0.20908427  0.00575194  0.25473176  0.16576149
  [0.23156112]  0.13547184 -0.15925129  0.0781678  -0.04461159 -0.10873899
 -0.01744103 -0.00722547 -0.02639494  0.16895042  0.16135041 -0.24925902
 -0.04265913 -0.01070677  0.06046893 -0.19340738  0.1397388   [0.20947122]
 -0.23381362  0.15590953  0.11293555  0.07553277

'''3, 13, 25, 42'''


-0.13289967  0.19413383 -0.23648182 -0.15141597  0.01978489 -0.08248962
  0.12693991  0.18432035  0.00901146 -0.20190168  0.01256089  0.01012584
  0.00140821 -0.01024449 -0.14393765  0.10199372 -0.12641153 -0.11833807
 -0.00912969 -0.0185902   0.05445604 -0.08448044  [0.29717045] -0.19405543
  [0.3690875]  -0.01471872 -0.07770845 -0.18798617 -0.1050134   0.094759
  0.11786452 -0.23278194 -0.19242335  0.17199139  0.15097418  0.1366933
  0.16252199 -0.11171976 -0.04510397  0.08891229 -0.05316776  [0.26728981]
  [0.20655607] -0.05936213  0.07745369  0.14287571


  
 0.0303659  -0.01717336 -0.08416767 -0.05719099  0.04906234  0.12140269
 -0.0060402  -0.07572078 -0.16298597  0.03803504  0.00552781 -0.06514311
 -0.20880248  0.05863614 -0.30271405  0.02099271 -0.30627404 -0.15936882
  0.05271174 -0.09555833 -0.12305048 -0.23414782 -0.11396841  0.0387358
 -0.12400731  0.03244835 -0.08531335  0.14773899  [0.18545479]  0.11260523
  0.0674892  -0.13095958 -0.29840497 -0.08608505 -0.10214176  0.07520623
  0.09208758  0.29493711  [0.31969203] -0.02852702  [0.13649779] -0.04116292
 -0.06012618  [0.30616927]  0.18219248  0.04823266


 
vec_no._|__________________________importance:_max->min___________________________________
1       | Swimming          Athletics           Basketball          Equestrian
2       | Weightlifting     Badminton           Artistic swimming   Wrestling         
3       | Badminton         Table Tennis        Artistic swimming   Cycling Track
4       | Skateboarding     Softball            Baseball            Beach Vollyball            


"""