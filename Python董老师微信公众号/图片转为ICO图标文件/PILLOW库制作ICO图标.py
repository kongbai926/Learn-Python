from PIL import Image

# 创建不同尺寸，最大支持256×256
size = (256, 144, 128, 108, 100, 88, 72, 48)
sizes = tuple(zip(size, size))

#im = Image.open(input('输入原始图像文件：'))
im = Image.open('Huawei Tubiao.jpg')

# ICO图标为RGBA格式，原始图像不一定符合要求，所以进行转换
im.convert('RGBA').save('自创ICO图标文件/xiaowu.ico', sizes = sizes)