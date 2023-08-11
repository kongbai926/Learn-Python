import tkinter
import tkinter.filedialog
import tkinter.messagebox
import tkinter.scrolledtext
import tkinter.simpledialog

# 创建应用程序窗口
app = tkinter.Tk()
app.title("简单文本编辑器")
app['width'] = 800
app['height'] = 600
textChanged = tkinter.IntVar(value=0)

# 当前文件名
fileName = ''

# 创建菜单
menu = tkinter.Menu(app)
# 子菜单
subMenu = tkinter.Menu(menu, tearoff=0)


# 打开文件函数
def open_diy():
    global fileName
    # 如果内容已改变，先保存
    if textChanged.get():
        yesNo = tkinter.messagebox.askyesno(title='保存文件', message='文件未保存，是否保存文件更改？')
        if yesNo == tkinter.YES:
            save()  # 需要定义函数Save()用来保存文件
        fileName = tkinter.filedialog.askopenfilename(title='打开文件', filetypes=[('Text files', '*.txt')])
        if fileName:
            # 清空内容，位置0.0是lineNumber.Colum的表示方法，表示行号和列号
            txtContent.delete(0.0, tkinter.END)
            fp = open(fileName, 'r')  # 可根据需要改变编码格式
            txtContent.insert(tkinter.INSERT, ''.join(fp.readlines()))
            fp.close()
            #             标记为尚未修改
            textChanged.set(0)


# 创建“打开”菜单并绑定菜单事件处理函数
subMenu.add_command(label='打开文件', command=open_diy)


# 保存函数
def save():
    global fileName
    #     如果是第一次保存新建文件，则打开“另存为”窗口
    if not fileName:
        saveAs()  # 需要编写“另存为”函数
    #     如果内容发生改变，保存，可使用with关键字改写文件操作的代码
    elif textChanged.get():
        fp = open(fileName, 'w')
        fp.write(txtContent.get(0.0, tkinter.END))
        fp.close()
        textChanged.set(0)


# 创建“保存”按钮并绑定处理函数
subMenu.add_command(label='保存', command=save)


# 另存为函数
def saveAs():
    global fileName
    #     打开另存为窗口
    newFileName = tkinter.filedialog.askopenfilename(title='另存为', initialdir=r'd:\\', initialfile='new.txt')
    #     如果指定了文件名，则保存文件，可使用with改写
    if newFileName:
        fp = open(newFileName, 'w')
        fp.write(txtContent.get(0.0, tkinter.END))
        fp.close()
        textChanged.set(0)


# 创建另存为按钮并绑定事件
subMenu.add_command(label='另存为', command=saveAs)

# 添加分割线
subMenu.add_separator()


# 关闭函数
def close():
    global fileName
    save()
    txtContent.delete(0.0, tkinter.END)
    #     置空文件名
    fileName = ''


# 创建关闭按钮并绑定事件
subMenu.add_command(label='关闭', command=close)

# 将子菜单关联到主菜单上
menu.add_cascade(label='文件', menu=subMenu)

# 编辑子菜单
subMenu = tkinter.Menu(menu, tearoff=0)


# 撤销最后一次操作
def unDo():
    #     启用撤销标志
    txtContent[' undo'] = True
    try:
        txtContent.edit_undo()
    except Exception as e:
        pass


# 创建撤销按钮并绑定事件
subMenu.add_command(label='撤销', command=unDo)


# 重做函数
def reDo():
    txtContent['undo'] = True
    try:
        txtContent.edit_redo()
    except Exception as e:
        pass


# 创建重做按钮并绑定事件
subMenu.add_command(label='重做', command=reDo)
subMenu.add_separator()


# 复制函数
def Copy():
    txtContent.clipboard_clear()
    txtContent.clipboard_append(txtContent.selection_get())


subMenu.add_command(label='复制', command=Copy)


# 剪切函数
def Cut():
    Copy()
    txtContent.delete(tkinter.SEL_FIRST, tkinter.SEL_LAST)  # 删除所选内容


subMenu.add_command(label='剪切', command=Cut)


# 粘贴函数
def Paste():
    #     如果没有选中内容，则粘贴到鼠标位置
    # 如果有选中内容，则先删除在粘贴
    try:
        txtContent.insert(tkinter.SEL_FIRST, txtContent.clipboard_get())
        txtContent.delete(tkinter.SEL_FIRST, tkinter.SEL_LAST)
        #         如果粘贴成功就结束该函数，以免异常出来结构执行完成之后再次粘贴
        return
    except Exception as err:
        pass
    txtContent.insert(tkinter.INSERT, txtContent.clipboard_get())


subMenu.add_command(label='粘贴', command=Paste)
subMenu.add_separator()


def Search():
    #     获取想要的内容
    textToSearch = tkinter.simpledialog.askstring(title='搜索', prompt='想要搜索什么？')
    start = txtContent.search(textToSearch, 0.0, tkinter.END)
    if start:
        tkinter.messagebox.showinfo(title='找到', message='OK')


subMenu.add_command(label='搜索', command=Search)
menu.add_cascade(label='编辑', menu=subMenu)

# Help子菜单
subMenu = tkinter.Menu(menu, tearoff=0)


def About():
    tkinter.messagebox.showinfo(title='关于',
                                message='{: <10}\n{: ^10}\n{: ^10}'.format('自创文本编辑器', '作者：奇幻时空',
                                                                           '版本号：0.0.1'))


subMenu.add_command(label='关于', command=Search)
menu.add_cascade(label='帮助', menu=subMenu)

# 将创建的菜单关联到应用程序窗口
app.config(menu=menu)

# 创建文本编辑器组件，并自动适应窗口大小
txtContent = tkinter.scrolledtext.ScrolledText(app, wrap=tkinter.WORD)
txtContent.pack(fill=tkinter.BOTH, expand=tkinter.YES)


def KeyPress(event):
    textChanged.set(1)


txtContent.bind('<KeyPress>', KeyPress)

app.mainloop()
