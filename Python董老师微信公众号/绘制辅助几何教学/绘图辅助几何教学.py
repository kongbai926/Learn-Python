import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['STSong']

k = 1  # 反比例函数 xy = k 的常数 k
m, n = 6, 3  # 矩形右上角坐标（ m , n )
x = np.arange(0.1, m + 0.5, 0.02)  # 第一象限中反比例函数曲线上顶点的 x 坐标
y = k / x  # 根据反比例函数 xy = k 计算顶点 y 坐标
is_dragging = False  # 是否处于拖动模式，即鼠标左键是否按下
is_close = False  # 鼠标当前位置是否与 B 点足够接近
circle = None  # 在 B 点绘制的实心圆对象


def draw():
    global m, n, circle
    plt.cla()  # 删除当前坐标系中所有图形
    plt.plot(x, y, 'b')  # 绘制第一象限指定区间内的反比例函数图像绘
    plt.plot([0, m, m, 0, 0], [0, 0, n, n, 0], 'r')  # 制矩形，从左下角出发，向右、上、左、下
    plt.plot([0, m], [n, 0], 'g')  # 矩形对角线
    if k / n < m:  # 只在矩形与反比例函数确实有交点时才绘制
        plt.plot([k / n, m], [n, k / m], 'g')  # 矩形与反比例函数的交点连线
    if is_close:  # 鼠标距离 B 点足够近时绘制一个紫色实心圆
        circle = plt.Circle((m, n), 0.1, color='purple')
        plt.gca().add_artist(circle)
    elif circle:  # 鼠标远离 B 点时不绘制紫色实心圆
        circle.remove()
        circle = None
    for xx, yy, ch in zip([0, m, m, 0, k / n, m], [0, 0, n, n, n, k / m], ' OABCDE '):
        if k / n > m and ch in 'DE':  # 矩形与反比例函数无交点时不显示 DE
            continue
        plt.text(xx, yy + 0.02, ch)  # 绘制顶点与交点的符号
        plt.gca().set_aspect(True)  # 设置图形纵横比相等
        plt.xlim(-0.1, 7)  # 设置坐标轴跨度
        plt.ylim(-0.1, 4)
        plt.title(f'反比例常数k ={k} , 矩形右上脚坐标：m = {round(m, 3)}, n = {round(n, 3)}', fontsize=20)


draw()


def on_mouse_down(event):
    global is_dragging
    if event.button == 1 and is_close:
        is_dragging = True


def on_mouse_up(event):
    global is_dragging
    is_dragging = False  # 鼠标抬起后不再可以拖动 B 点


def on_mouse_move(event):
    global m, n, is_close
    if not (event.xdata and event.ydata):  # 鼠标在坐标系之外运动时不做任何操作
        return
    if (m - event.xdata) ** 2 + (n - event.ydata) ** 2 <= 0.03:
        is_close = True  # 鼠标距离 B 点足够近
    else:
        is_close = False
    if is_dragging:  # 拖动状态下修改 B 点位置
        m, n = event.xdata, event.ydata
    draw()  # 重新绘制图形
    event.canvas.draw()


# 绑定鼠标事件，响应鼠标按下、抬起、移动操作
cfc = plt.gcf().canvas
cfc.mpl_connect('button_press_event', on_mouse_down)
cfc.mpl_connect('button_release_event', on_mouse_up)
cfc.mpl_connect('motion_notify_event', on_mouse_move)
plt.show()
