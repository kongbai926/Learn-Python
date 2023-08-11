import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 1, 101)
f03 = (-t ** 3 + 3 * t ** 2 - 3 * t + 1) / 6
f13 = (3 * t ** 3 - 6 * t ** 2 + 4) / 6
f23 = (-3 * t ** 3 + 3 * t ** 2 + 3 * t + 1) / 6
f33 = t ** 3 / 6

lines = plt.plot(t, f03, t, f13, t, f23, t, f33)
plt.yticks([f03.min(), f03.max(), f23.min(), f23.max()])
plt.legend(lines, ['$F_{0, 3}=(-t^3 + 3 * t^2 - 3 * t + 1) / 6$', '$F_{1, 3}=(3 * t^3 - 6 * t^2 + 4) / 6$',
                   '$F_{2, 3}=(-3 * t^3 + 3 * t^2 + 3 * t + 1) / 6$', '$F_{3, 3}=t^3 / 6$'], ncol=1, fontsize=7)
plt.title('三次B样条曲线4个基本函数', fontproperties='STSong', fontsize=14)

plt.show()
