import random

import matplotlib.pyplot as plt
from numpy import reshape

# 每个月的销售额
month = random.sample(list(range(3, 21)), 12)
# 按季度分组求和
quarter = reshape(month, (4, 3)).sum(axis=1)
width = 0.3

# 外圈饼状图
plt.pie(month, radius=1, autopct='{:.1f}%'.format, pctdistance=0.85,
        labels=[f"{i}月" for i in range(1, 13)], wedgeprops={'width': width},
        textprops={'family': 'simhei'},
        labeldistance=1.01)
# 内存饼状图
patches, texts, autotes = plt.pie(quarter, radius=1 - width,
                                  autopct='{:.1f}%'.format, pctdistance=0.7,
                                  labels=['1季度', '2季度', '3季度', '4季度'],
                                  labeldistance=0.2, wedgeprops={'width': width},
                                  textprops={'family': 'STSong'},
                                  rotatelabels=True)

# 图形标题
plt.title('月份/季度销售额', fontproperties='STSong', fontsize=18)
plt.show()
