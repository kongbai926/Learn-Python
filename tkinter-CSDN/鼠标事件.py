from tkinter import *


class MyApp(Tk):
    """继承Tk，创建自己的桌面应用程序类"""

    def __init__(self):
        """构造函数"""

        super().__init__()

        self.title('鼠标事件演示程序')
        self.geometry('480x200')
        # self.iconbitmap('res/Tk.ico')

        self.info = StringVar()
        self.info.set('')

        label = Label(self, textvariable=self.info, font=("Arial Bold", 18))
        label.pack(side='top', expand='yes', fill='both')

        btn = Button(self, text='确定', bg='#C0C0C0')
        btn.pack(side='top', fill='x', padx=5, pady=5)

        label.bind('<Enter>', self.on_mouse)  # 进入控件
        label.bind('<Leave>', self.on_mouse)  # 离开控件
        label.bind('<Motion>', self.on_mouse)  # 移动
        label.bind('<MouseWheel>', self.on_mouse)  # 滚轮
        btn.bind('<Button-1>', self.on_mouse)  # 左键单击
        btn.bind('<Button-2>', self.on_mouse)  # 中键单击
        btn.bind('<Button-3>', self.on_mouse)  # 右键单击
        btn.bind('<B1-Motion>', self.on_mouse)  # 左键拖动
        btn.bind('<Double-Button-1>', self.on_mouse)  # 左键双击
        btn.bind('<Double-Button-3>', self.on_mouse)  # 右键双击

    def on_mouse(self, evt):
        """响应所有鼠标事件的函数"""

        if isinstance(evt.num, int):
            self.info.set('事件类型：%s\n键码：%d\n鼠标位置：(%d, %d)\n时间：%d' % (evt.type, evt.num, evt.x, evt.y, evt.time))
        else:
            self.info.set('事件类型：%s\n鼠标位置：(%d, %d)\n时间：%d' % (evt.type, evt.x, evt.y, evt.time))


if __name__ == '__main__':
    app = MyApp()
    app.mainloop()
