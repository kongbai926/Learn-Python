import tkinter
import tkinter.messagebox
import tkinter.ttk

root = tkinter.Tk()
root.title('选择文本框')  # 窗口标题
# 定义窗口大小
root['height'] = 400
root['width'] = 320

# 创建标签
lableName = tkinter.Label(root, text='姓名：', justify=tkinter.RIGHT, width=50)
lableName.place(x=10, y=5, width=50, height=20)

# 创建变量，并将其与标签关联
varName = tkinter.StringVar('')
entryName = tkinter.Entry(root, width=120, textvariable=varName)  # 创建文本框并设置关联的变量
entryName.place(x=70, y=5, width=120, height=20)

labelGrade = tkinter.Label(root, text='年级：', justify=tkinter.RIGHT, width=50)
labelGrade.place(x=10, y=40, width=50, height=20)

studentClass = {
    '1': ['1', '2', '3', '4'],
    '2': ['1', '2'],
    '3': ['1', '2', '3']}  # 模拟年级，键为年级，值为班级
comboGrade = tkinter.ttk.Combobox(root, values=tuple(studentClass.keys()), width=50)
comboGrade.place(x=70, y=40, width=50, height=20)


def comboChange(event):
    grade = comboGrade.get()
    if grade:
        comboClass['values'] = studentClass.get(grade)
    else:
        comboClass.set([])


# 绑定事件处理函数
comboGrade.bind('<<ComboboxSelected>>', comboChange)
lableClass = tkinter.Label(root, text='班级：', justify=tkinter.RIGHT, width=50)
lableClass.place(x=130, y=40, width=50, height=20)

# 学生年级组合框
comboClass = tkinter.ttk.Combobox(root, width=50)
comboClass.place(x=190, y=40, width=50, height=20)
# 性别单选按钮
labelSex = tkinter.Label(root, text='性别', justify=tkinter.RIGHT, width=50)
labelSex.place(x=10, y=70, width=50, height=20)
sex = tkinter.IntVar(value=1)  # 性别关联变量，1表示男性，0表示女性，默认男性
radioMan = tkinter.Radiobutton(root, variable=sex, value=1, text='男')
radioWoman = tkinter.Radiobutton(root, variable=sex, value=0, text='女')
radioMan.place(x=70, y=70, width=50, height=20)
radioWoman.place(x=130, y=70, width=70, height=20)

# 班长变量
monitor = tkinter.IntVar(value=0)  # 默认不是班长
checkMonitor = tkinter.Checkbutton(root, text='是班长', variable=monitor, onvalue=1, offvalue=0)
checkMonitor.place(x=20, y=100, width=100, height=20)


# 按钮处理事件
def addInformation():
    result = '姓名：' + entryName.get()
    result = result + '；年级：' + comboGrade.get() + '；班级：' + comboClass.get() + '；性别：' + ('男性' if sex.get() else '女性')
    result = result + '；班长：' + ("是" if monitor.get() else "不是")
    listBoxStudents.insert(0, result)


butttonAdd = tkinter.Button(root, text='添加', width=40, command=addInformation)
butttonAdd.place(x=130, y=100, width=40, height=20)


def deleteSelect():
    select = listBoxStudents.curselection()
    if not select:
        tkinter.messagebox.showinfo(title='信息', message='没有选择')
    else:
        listBoxStudents.delete(select)


buttonDelete = tkinter.Button(root, text='删除', width=100, command=deleteSelect)
buttonDelete.place(x=180, y=100, width=100, height=20)

# 创建列表框组件
listBoxStudents = tkinter.Listbox(root, width=300)
listBoxStudents.place(x=10, y=130, width=300, height=200)

root.mainloop()
