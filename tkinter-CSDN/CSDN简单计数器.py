from tkinter import *

class MyApp(Tk):
    """继承Tk，创建自己的桌面应用程序类"""
    
    def __init__(self):
        """构造函数"""
        
        super().__init__()
        
        self.title('按钮点击计数器')
        self.geometry('320x160')
#        self.iconbitmap('res/Tk.ico')
        
        self.counter = IntVar() # 创建一个整型变量对象
        self.counter.set(0) # 置其初值为0
        
        label = Label(self, textvariable=self.counter, font=("Arial Bold", 50)) # 将Label和整型变量对象关联
        label.pack(side='left', expand='yes', fill='both', padx=5, pady=5)
        
        btn = Button(self, text='点我试试看', bg='#90F0F0')
        btn.pack(side='right', anchor='center', fill='y', padx=5, pady=5)
        
        btn.bind(sequence='<Button-1>', func=self.on_button) # 绑定事件和事件函数
    
    def on_button(self, evt):
        """点击按钮事件的响应函数, evt是事件对象"""
        
        self.counter.set(self.counter.get()+1)

if __name__ == '__main__':
    app = MyApp()
    app.mainloop()
