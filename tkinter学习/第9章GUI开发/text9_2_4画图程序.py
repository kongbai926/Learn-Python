import tkinter
import tkinter.colorchooser
import tkinter.filedialog
import tkinter.simpledialog

from PIL import ImageGrab, ImageTk

root = tkinter.Tk()
root.title('画板')
root['width'] = 800
root['height'] = 600

# 控制是否允许画图的变量，1为允许，0为不允许
canDraw = tkinter.IntVar(value=0)
# 控制画图类型的变量，1为曲线，2为直线，3为矩形，4为文本，5为橡皮擦
what = tkinter.IntVar(value=1)
text = ''

# 记录鼠标位置变量
x = tkinter.IntVar(value=0)
y = tkinter.IntVar(value=0)

# 设置前景色、背景色
foreColor = "#000000"
backColor = "#FFFFFF"

# 创建画布，设置尺寸和颜色
image = tkinter.PhotoImage()
canvas = tkinter.Canvas(root, bg='white', width=800, height=600)
canvas.create_image(800, 600, image=image)


# 按下鼠标左键，允许画图，记录鼠标按下的位置
def onLeftButtonDown(event):
    global text
    canDraw.set(1)
    x.set(event.x)
    y.set(event.y)
    if what.get() == 4:
        canvas.create_text(event.x, event.y, text=text)


canvas.bind('<Button-1>', onLeftButtonDown)

# 记录最后绘制图形的id
lastDraw = 0


# 按住鼠标左键移动，画图
def onLeftButtonMove(event):
    global lastDraw
    if canDraw.get() == 0:
        return
    if what.get() == 1:
        #         使用当前选择的前景色绘制曲线
        canvas.create_line(x.get(), y.get(), event.x, event.y, fill=foreColor)
        x.set(event.x)
        y.set(event.y)
    elif what.get() == 2:
        #         绘制直线，先删除刚刚划过的直线，再画一条新的直线
        try:
            canvas.delete(lastDraw)
        except Exception:
            pass
        lastDraw = canvas.create_line(x.get(), y.get(), event.x, event.y, fill=foreColor)
    elif what.get() == 3:
        #         绘制矩形， 先删除刚刚划过的矩形，再画一个新的矩形
        try:
            canvas.delete(lastDraw)
        except Exception:
            pass
        lastDraw = canvas.create_rectangle(x.get(), y.get(), event.x, event.y, fill=backColor, outline=foreColor)
    elif what.get() == 5:
        #         橡皮，使用背景色填充10*10的矩形区域，相当于擦除图像
        canvas.create_rectangle(event.x - 5, event.y - 5, event.x + 5, event.y + 5, outline=backColor, fill=backColor)


canvas.bind('<B1-Motion>', onLeftButtonMove)


# 鼠标左键抬起，不允许画圆
def onLeftButtonUp(event):
    if what.get() == 2:
        #         多绘制一条直线
        canvas.create_line(x.get(), y.get(), event.x, event.y, fill=foreColor)
    elif what.get() == 3:
        #         多绘制一个矩形
        canvas.create_rectangle(x.get(), y.get(), event.x, event.y, fill=backColor, outline=foreColor)
    canDraw.set(0)
    global lastDraw
    #     防止切换图形时误删除上次绘制的图形
    lastDraw = 0


canvas.bind('<ButtonRelease-1>', onLeftButtonUp)

# 创建菜单
menu = tkinter.Menu(root, tearoff=0)


# 打开图像文件
def Open():
    fileName = tkinter.filedialog.askopenfilename(title='打开文件', filetypes=[('image', '*.png'), ('image', '*.gif'), ('image', '*.jpg')])
    if fileName:
        global image
        image = ImageTk.PhotoImage(file=fileName)
        canvas.create_image(80, 80, image=image)


menu.add_command(label='打开', command=Open)


# 保存文件
def Save():
    #     获取客户区域位置和尺寸，并截图保存
    left = int(root.winfo_rootx())
    top = int(root.winfo_rooty())
    wid = root.winfo_width()
    heig = root.winfo_height()
    im = ImageGrab.grab((left, top, left + wid, top + heig))
    # 保存绘制的图片
    fileName = tkinter.filedialog.askopenfilename(title='保存', filetypes=[('图片文件', '*.png')])
    if not fileName:
        return
    if not fileName.endswith('.png'):
        fileName += '.png'
    im.save(fileName)


menu.add_command(label='保存', command=Save)


# 添加菜单，清楚所有图像
def Clear():
    for ite in canvas.find_all():
        canvas.delete(ite)


menu.add_command(label='清除', command=Clear)

# 添加分割线
menu.add_separator()

# 创建子菜单，用来选择绘图类型
menuType = tkinter.Menu(menu, tearoff=0)


# 选择曲线
def drawCurve():
    what.set(1)


menuType.add_command(label='曲线', command=drawCurve)


# 选择直线
def drawLine():
    what.set(2)


menuType.add_command(label='直线', command=drawLine)


# 选择矩形
def drawRectangle():
    what.set(3)


menuType.add_command(label='矩形', command=drawRectangle)


# 选择文本
def drawText():
    global text
    text = tkinter.simpledialog.askstring(title='输入需要绘制的文本', prompt='')
    what.set(4)


menuType.add_command(label='文本', command=drawText)

# 添加分割线
menuType.add_separator()


# 选择前景色
def ChooseBcakColor():
    global foreColor
    foreColor = tkinter.colorchooser.askcolor()[1]


menuType.add_command(label='前景色', command=ChooseBcakColor)


# 选择背景色
def ChooseBackColor():
    global backColor
    backColor = tkinter.colorchooser.askcolor()[1]


menuType.add_command(label='背景色', command=ChooseBackColor)


# 选择橡皮擦
def onErase():
    what.set(5)


menuType.add_command(label='橡皮擦', command=onErase)

menu.add_cascade(label='格式', menu=menuType)


# 鼠标右键抬起，弹出菜单
def onRightButtonUp(event):
    menu.post(event.x_root, event.y_root)


canvas.bind('<ButtonRelease-3>', onRightButtonUp)

canvas.pack(fill=tkinter.BOTH, expand=tkinter.YES)

# 启动应用程序
root.mainloop()
