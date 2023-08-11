def reinpu():
    try:
        s = int(input('输入数字：'))
        print(s)
    except Exception as error:
        print('出现错误：', error, '\n请重试')
        reinpu()

'''程序出错重试代码'''
reinpu()
