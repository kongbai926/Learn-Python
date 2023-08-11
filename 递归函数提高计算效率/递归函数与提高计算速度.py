from functools import lru_cache


@lru_cache(100)  # 装饰器。递归在计算时间上可能会很慢，添加此装饰器有助于提高函数连续运行速度
def line(n):
    if n <= 1:
        return 1
    return line(n - 1) + line(n - 2)


for i in range(0, 500):
    print(line(i))
