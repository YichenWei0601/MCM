"""
xiangchuyang needed.
"""

import random
import math
import pandas as pd

# 读取txt文件
with open(r"C:\Users\weiyi\Desktop\gamma_loss(2).txt", "r") as file:
    numbers = [float(line.strip()) for line in file.readlines()]

# 打乱数字顺序
random.shuffle(numbers)

# 计算每个数字的数量级
def get_order(number):
    if number != 0:
        return math.log10(abs(number))
    else:
        return math.log10(abs(number))

# 生成表格数据
data = {
    "序号": [i + 1 for i in range(len(numbers))],  # 序号从1开始
    "数量级": [get_order(number) for number in numbers]
}

# 创建DataFrame并显示
df = pd.DataFrame(data)

# 打印表格
print(df)

# 如果需要，可以将表格保存为CSV文件
df.to_csv(r"C:\Users\weiyi\Desktop\shuffled_numbers_with_order.csv", index=False)