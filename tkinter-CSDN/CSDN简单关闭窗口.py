from tkinter import *

def click_button():
    """点击按钮的事件函数"""
    
    root.destroy() # 调用root的析构函数

root = Tk()
root.title('最简单的桌面应用程序')
root.geometry('640x320')
#root.iconbitmap('res/Tk.ico')

label = Label(root, text='Hello World', font=("Arial Bold", 50))
label.pack(side='top', expand='yes', fill='both')
btn = Button(root, text='关闭窗口', bg='#C0C0C0', command=click_button) # 用command参数绑定事件函数
btn.pack(side='top', fill='x', padx=5, pady=5)

root.mainloop()
