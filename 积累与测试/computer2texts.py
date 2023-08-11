def py1():
    s = input()
    print('{:*^30}'.format(s))


def py2():
    a, b = 0, 1
    while a <= 50:
        print(a)
        a, b = b, a+b


def py3():
    import jieba
    s = input()
    lis = jieba.lcut(s)
    print(''.join(lis[::-1]))


def py4():
    import turtle
    for i in range(3):
        turtle.fd(100)
        turtle.seth(120 * (i + 1 ))
        


def py5():
    fuilts = input('输入水果并以空格分隔：')
    fulit_l = fuilts.split(' ')
    d_fulit = {}
    for i in fulit_l:
        d_fulit[i] = d_fulit.get(i, 0) + 1
    lis = d_fulit.items()
    for i in lis:
        print('{0}：{1}'.format(i[0], i[1]))


py5()
