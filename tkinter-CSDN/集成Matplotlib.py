import matplotlib
import numpy as np

matplotlib.use('TkAgg')
matplotlib.rcParams['font.sans-serif'] = ['FangSong']
matplotlib.rcParams['axes.unicode_minus'] = False

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *


class MyApp(Tk):
    """继承Tk，创建自己的桌面应用程序类"""

    def __init__(self):
        """构造函数"""

        Tk.__init__(self)

        self.title('集成Matplotlib')
        # self.iconbitmap('res/Tk.ico')
        self.init_ui()
        self.center()

    def init_ui(self):
        """初始化界面"""

        self.fig = Figure(dpi=150)
        self.cv = FigureCanvasTkAgg(self.fig, self)
        self.cv.get_tk_widget().pack(fill=BOTH, expand=1, padx=5, pady=5)

        f = Frame(self)
        f.pack(pady=10)
        Button(f, text='散点图', width=12, bg='#f0e0d0', command=self.on_scatter).pack(side=LEFT, padx=20)
        Button(f, text='等值线图', width=12, bg='#f0e0d0', command=self.on_contour).pack(side=LEFT, padx=20)

    def center(self):
        """窗口居中"""

        self.update()  # 更新显示以获取最新的窗口尺寸
        scr_w = self.winfo_screenwidth()  # 获取屏幕宽度
        scr_h = self.winfo_screenheight()  # 获取屏幕宽度

        w = self.winfo_width()  # 窗口宽度
        h = self.winfo_height()  # 窗口高度
        x = (scr_w - w) // 2  # 窗口左上角x坐标
        y = (scr_h - h) // 2  # 窗口左上角y坐标

        self.geometry('%dx%d+%d+%d' % (w, h, x, y))  # 设置窗口大小和位置

    def on_scatter(self):
        """散点图"""

        x = np.random.randn(50)  # 随机生成50个符合标准正态分布的点（x坐标）
        y = np.random.randn(50)  # 随机生成50个符合标准正态分布的点（y坐标）
        color = 10 * np.random.rand(50)  # 随即数，用于映射颜色
        area = np.square(30 * np.random.rand(50))  # 随机数表示点的面积

        self.fig.clear()
        ax = self.fig.add_subplot(111)
        ax.scatter(x, y, c=color, s=area, cmap='hsv', marker='v', edgecolor='r', alpha=0.5)
        self.cv.draw()

    def on_contour(self):
        """等值线图"""

        y, x = np.mgrid[-3:3:60j, -4:4:80j]
        z = (1 - y ** 5 + x ** 5) * np.exp(-x ** 2 - y ** 2)

        self.fig.clear()
        ax = self.fig.add_subplot(111)
        ax.set_title('有填充的等值线图')
        c = ax.contourf(x, y, z, levels=8, cmap='jet')
        self.fig.colorbar(c, ax=ax)
        self.cv.draw()


if __name__ == '__main__':
    app = MyApp()
    app.mainloop()
