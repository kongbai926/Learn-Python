import matplotlib.pyplot as plt
import numpy as np

angle = np.arange(0, np.pi, 0.01)

r1 = np.sin(angle) * np.cos(angle * 3)
r2 = np.sin(angle * 3) * np.cos(angle)

# 创建极坐标系
coorSys = plt.subplot(polar=True)
# 设置最大角度和最小角度
coorSys.set_thetamin(0)
coorSys.set_thetamax(180)
# 在坐标系中绘制折线图
coorSys.plot(angle, r1)  # 在坐标系中画的第一个图形
coorSys.plot(angle, r2)  # 在坐标系中画的第二个图形
# 设置半径方向的刻度
coorSys.set_yticks([-1, -0.5, 0, 0.5, 1])
# 设置角度方向的刻度
coorSys.set_xticks([0, np.pi / 4, np.pi / 2, np.pi * 3 / 4, np.pi])

plt.show()
