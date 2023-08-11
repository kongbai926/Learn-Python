import numpy as np
import matplotlib.pyplot as plt

# 设置种子数，使得每次运行程序时生成同样的随机数
np.random.seed(20221216)
data = np.random.randint(1, 10, (5, 8))
for index, row in enumerate(data):
    # 为每行数据绘制柱状图，设置底面位置，形成堆叠效果
    # 每个柱状中相同颜色的一段的高度表示数值大小
    plt.bar(range(len(row)), row, bottom=data[:index].sum(axis=0),
            label = 'row{}'.format(index))

# 设置坐标轴标签、图形标题、图例
plt.xlabel('position')
plt.ylabel('values')
plt.title('stack bars', fontsize = 18)

# 显示图形
plt.show()