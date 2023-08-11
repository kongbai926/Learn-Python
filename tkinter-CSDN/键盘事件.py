from tkinter import *


class MyApp(Tk):
    """继承Tk，创建自己的桌面应用程序类"""

    def __init__(self):
        """构造函数"""

        super().__init__()

        self.title('键盘事件演示程序')
        self.geometry('480x200')
        # self.iconbitmap('res/Tk.ico')

        self.info = StringVar()
        self.info.set('')

        self.info = StringVar()
        self.info.set('')

        self.lab = Label(self, textvariable=self.info, font=("Arial Bold", 18))
        self.lab.pack(side='top', expand='yes', fill='both')
        self.lab.focus_set()
        self.lab.bind('<Key>', self.on_key)  # 任意键

        self.btn = Button(self, text='切换焦点', bg='#C0C0C0', command=self.set_label_focus)
        self.btn.pack(side='top', fill='x', padx=5, pady=5)

    def on_key(self, evt):
        """响应所有键盘事件的函数"""

        self.info.set('evt.char = %s\nevt.keycode = %s\nevt.keysym = %s' % (evt.char, evt.keycode, evt.keysym))

    def set_label_focus(self):
        """在Label和Button之间切换焦点"""

        self.info.set('')

        if isinstance(self.lab.focus_get(), Label):
            self.btn.focus_set()
        else:
            self.lab.focus_set()


if __name__ == '__main__':
    app = MyApp()
    app.mainloop()
