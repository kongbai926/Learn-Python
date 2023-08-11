# 循环嵌套
def texts1():
    sc = ["adscd", "asqdds", "dadfwfc", "ouohcgaf", "pouiibx", "popiiuiuc", "oioucccpop"]
    x = 0  # 匹配字数计数
    c = input("请输入匹配字母：")
    for i in sc:
        for a in i:
            if a == c:
                x = x + 1
                break
    print("含有字母%s的字符串个数是：%d" % (c, x))


# 实现键盘输入列表+time模块的使用
def texts2():
    import time
    ls = list(map(int, input("请输入空格间隔的数字：").split()))  # map函数实现某个函数的批次调用，int函数负责强制转换，split负责将输入的内容以某个符号分隔开此处使用空格分隔
    for i in ls:
        time_know = time.strftime("%Y-%m-%d  %H:%M:%S", time.localtime(time.time()))
        time.sleep(i)
        print(time_know)


def texts2_1():
    txt_list = list(map(str, input("请输入水果：").split()))
    d = {}
    for item in txt_list:
        d[item] = d.get(item, 0) + 1
    ls = list(d.items())
    ls.sort(key=lambda x: x[1], reverse=True)
    print(ls)


# 邮件发送
def texts3():
    from email.mime.text import MIMEText  # 构造文本内容
    from email.mime.multipart import MIMEMultipart  # 用于构造带图片的邮件
    from email.mime.application import MIMEApplication  # 用于封装附件
    import smtplib
    from_addr = '3199065524@qq.com'  # 发件人邮箱
    from_password = 'yyqhdvcygxxedeac'  # 发件人密码（授权码）
    smtp_server = 'smtp.qq.com'  # 邮箱服务器地址
    smtp_port = 465  # smtp协议默认端口是25，默认安全端口是465
    to_addr = '3190595475@qq.com'  # 收件人邮箱
    # 编写邮件内容：正文+附件
    msg = MIMEMultipart()
    msg['from'] = from_addr  # 邮件发件人
    msg['to'] = to_addr  # 邮件收件人
    msg['subject'] = 'python发送文本+附件邮件测试'  # 邮件主题
    part1 = MIMEText("带附件发送测试的邮件，不必在意！", 'plain', 'utf-8')  # 文本正文
    part2 = MIMEApplication(open(r'练习使用图片/python发送邮件需要的模块.jpg', 'rb').read())  # 附件
    msg.attach(part1)
    msg.attach(part2)
    #     发送邮件模块
    server = smtplib.SMTP_SSL(smtp_server, smtp_port)
    server.login(from_addr, from_password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()  # 关闭邮箱服务器连接


# 格式化输出：左对齐右对齐，中间用空格填充
def texts4():
    words = {"左对齐1": "右对齐1", "左对齐2": "右对齐2", "11": "22", "156": "289"}
    words_list = list(words.items())
    print(words_list)
    for i in range(4):
        word1, word2 = words_list[i]
        print("{0:<10} {1:>1}".format(word1, word2))


def texts4_1():
    import time
    length = 1000
    for i in range(1, length + 1):
        percent = i / length
        bar = '▉' * int(i // (length / 50))
        time.sleep(0.1)
        print('\r进度条：|{:<50}|{:>7.1%}'.format(bar, percent), end='')


# 斐波那契夫数列
def texts5():
    a, b = 0, 1
    for i in range(10):
        print(a, end=",")
        a, b = b, a + b


# 中文分词jieba
def texts6():
    import jieba
    tex = input("请输入文本：")
    tex_list = jieba.lcut(tex)  # lcut()切片后并将结果添加到一个列表中，返回列表
    for i in tex_list[:: -1]:  # 倒序输出列表内容
        print(i, end="\t")


# jieba的使用以及中文词频统计
def texts6_1():
    import jieba
    txts = input("请输入文本：")
    fuhaos = ",.;'/\\，。、‘’、；：:“”？《》<>-_()（） ~·%￥#@！……&*+-=\0\'\""
    for fuhao in fuhaos:
        txts = txts.replace(fuhao, "")
    words = jieba.lcut(txts)
    counts = {}
    for i in words:
        counts[i] = counts.get(i, 0) + 1
    for item in counts.items():
        print("文字：{:-<20}词频：{:<10}".format(item[0], item[1]))


# turtle库的使用
def texts7():
    import turtle
    for i in range(3):
        turtle.seth(-(i * 120))  # 方向
        turtle.fd(100)  # 移动距离


# 二级考试测试
def texts8():
    with open("名单.txt", "r", encoding="utf-8") as file:
        files = file.read()
        fuhao = "：，:,\n"
        for i in fuhao:
            files = files.replace(i, " ")
        files_list = files.split(" ")
        word_list = []
        for i in range(5):
            words = files_list[3 * i: 3 * (i + 1)]
            word_list.append(words)
        for i, j, k in word_list:
            print("{: <10}：{: ^10}地点{:->5}".format(i, j, k))



# 阶乘函数
def texts9(n):
    s = 1.0
    if n == 1 or n == 0:
        s = 1
    else:
        while n >= 1:
            s = s * n
            n -= 1
    print('{:e}'.format(s))


def py4():
    import turtle
    for i in range(3):
        turtle.seth(120 * i)
        turtle.fd(100)

# 创建窗口使画的图停留
def texts10():
    import tkinter
    root = tkinter.Tk()
    root['height'] = 1080
    root['width'] = 990
    lc = tkinter.Button(root, text = '三角形', command = py4, width = 150, height = 120)
    lc.place(x = 200, y = 110, height = 120, width = 150)
    root.mainloop()

# 随机选择
def texts11():
    import random


    list_m = [1, 10, 5, 8, 6]
    m = random.choice(list_m) #  随机选择一个
    print(m)
    
    n = random.sample(list_m, 2)  # 随机选择n个
    print(n)


# 学习测试
def texts():
    x = ["健康", "和平", "法治", "工作"]
    # y = "".join(x)
    # y = ""
    # for i in x:
    #     y += str(i)
    y = 0
    for i in x:
        y += 1
    for i in range(int(y / 2)):
        print(i)


# 测试调用
try:
    texts8()
except BaseException:
    print("程序错了！回炉重造800年再来吧！")
