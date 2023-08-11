"""
04版本将网址改为天津市旅游局网站进行数据收集。未成功！
"""

import time

"""以下部分引用用于爬虫部分"""
import requests
import openpyxl
from bs4 import BeautifulSoup

"""爬虫部分代码"""

def spyder(uil, header):
    """
    此函数属于爬虫主体代码，用于获取网站资料
    :param uil:
    :param header:
    :return:
    """
    try:
        actions = requests.get(uil, headers=header)
        print(actions.status_code)
        actions.encoding = 'utf-8'
        response_action = BeautifulSoup(actions.text, 'html.parser')
        allmovie = response_action.find('div', class_='content-text')  # 所有的景点集
        masage = allmovie.find('tbody')
        movies = masage.find_all('tr')
        for movie in movies:
            spot = movie.find_all('td')
            p = spot[2].text  # 景点名称
            t = spot[5].text  # 评定时间
            n = spot[3].text  # 地址
            m = spot[1].text  # 等级
            h = [p, n, m, t]
            sheet.append(h)
    except Exception as a:
        print(a)


"""协程部分代码"""
try:
    start = time.time()
    uil = 'http://whly.tj.gov.cn/WSBSYZXBS4230/WMFW8706/QYML408/202008/t20200817_3486782.html'  # 需要请求的网站
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}  # 请求头
    url_list = []
    url_list.append(uil)

    # 保存文件准备
    wb = openpyxl.Workbook()  # 打开一个工作文件，用于记录数据
    sheet = wb.active  # 活动表
    sheet.title = "天津市景点"
    t = ['景点名称', '地址', '等级', '评定时间']
    sheet.append(t)

    for url in url_list:
        spyder(url, header)

    wb.save('天津市A级景点信息.xlsx')
    wb.close()
    end = time.time()
    print(end - start)
except BaseException as err:
    print("协程程序出现错误\n{}".format(err))
