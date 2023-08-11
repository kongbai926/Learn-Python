from tkinter import *
from tkinter import ttk


class MyApp(Tk):
    """继承Tk，创建自己的桌面应用程序类"""

    def __init__(self):
        """构造函数"""

        super().__init__()

        self.title('主题控件')
        # self.iconbitmap('res/Tk.ico')
        self.init_ui()

    def init_ui(self):
        """初始化界面"""

        self.style = ttk.Style()

        self.theme = StringVar()
        self.theme.set(self.style.theme_use())

        ttk.Button(self, text='切换主题按钮', command=self.on_style).pack(padx=30, pady=20)
        ttk.Entry(self, textvariable=self.theme, justify=CENTER, width=20).pack(padx=30, pady=0)
        ttk.Combobox(self, value=('Tkinter', 'wxPython', 'PyQt5')).pack(padx=30, pady=20)

    def on_style(self):
        """更换主题"""

        items = self.style.theme_names()
        new_theme = items[(items.index(self.theme.get()) + 1) % len(items)]
        self.theme.set(new_theme)
        self.style.theme_use(new_theme)


if __name__ == '__main__':
    app = MyApp()
    app.mainloop()
