#-*- coding:UTF-8 -*-
url = "https://okjx.cc/?url="
import sys
import webbrowser
sys.path.append("libs")
urls = input("请输入电影链接")#输入电影链接在线观看影片
print(url+urls)
webbrowser.open(url+urls)
print(webbrowser.get())
