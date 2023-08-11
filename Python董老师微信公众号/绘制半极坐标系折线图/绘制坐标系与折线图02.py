"""
02版本在第7行有更改。更改了精度，使得画图看起来没有那么圆滑。
"""
import matplotlib.pyplot as plt
import numpy as np

angle = np.arange(0, np.pi, 0.2)  # 0.1改为0.2，图像不再圆滑，会看见折线。如果数字增加，图像更加曲折。

r1 = np.sin(angle) * np.cos(angle * 3)
r2 = np.sin(angle * 3) * np.cos(angle)
# 创建极坐标系
coorSys = plt.subplot(polar=True)
# 设置最大角度和最小角度
coorSys.set_thetamin(0)
coorSys.set_thetamax(180)
# 在坐标系中绘制折线图
coorSys.plot(angle, r1)
coorSys.plot(angle, r2)
# 设置半径方向的刻度
coorSys.set_yticks([-1, -0.5, 0, 0.5, 1])
# 设置角度方向的刻度
coorSys.set_xticks([0, np.pi / 4, np.pi / 2, np.pi * 3 / 4, np.pi])

plt.show()
