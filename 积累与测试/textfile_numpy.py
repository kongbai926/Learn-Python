import numpy as np

# 练习1 列表的创建
def texts1():
	a = np.array((1, 2, 3, 4, 5))
	b = np.array(([1, 2, 3], [4, 5, 6], [7, 8, 9]))
	x = np.linspace(0, 5, 10)
	y = np.logspace(0, 100, 10)
	print(a,'\n',b,'\n',x,'\n',y)
	
# 练习2 列表与数值的算术运算
def texts2():
	a = np.array((1, 2, 3, 4))
	print(a)
	print(a * 2)
	print(a // 2)
	print(a / 2.0)
	print(a ** 2)
	print(2 ** a)
	
# 练习3 列表与列表的算术运算
def texts3():
	a = np.array((1, 2, 3))
	b = np.array(([1, 2, 3], [4, 5, 6], [7, 8, 9]))
	print(a * b)
	print(a * b / b)
	b = np.array((1, 2, 3))
	print(a * b)
	print(a + b)
	print(b.shape)

# 练习四 列表切片
def texts4():
	c = np.array([[[j * 10 + i for i in range(3)] for i in range(10)] for j in range(7)])
	print(c[2 : 8, 3 : 7, 1 : 3]) # 列表切片，第一个表示一维范围，第二个表示二维范围，再多一组数据，就再加一维

# 布尔运算
def texts5():
	m = np.random.rand(10) # 10指元素个数；rand得到的是随机小数
	print(m[m > 0.3])
	print(np.array([3, 7 ,2]) == np.array([7, 3, 1]))

texts3()