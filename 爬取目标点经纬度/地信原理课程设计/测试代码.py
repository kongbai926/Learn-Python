import requests
from bs4 import BeautifulSoup

uil = 'http://whly.tj.gov.cn/WSBSYZXBS4230/WMFW8706/QYML408/202008/t20200817_3486782.html'  # 需要请求的网站
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}  # 请求头

try:
    params = {'show_ram': 1}
    actions = requests.get(uil, headers=header, params=params)
    print(actions.status_code)
    actions.encoding = 'utf-8'
    response_action = BeautifulSoup(actions.text, 'html.parser')
    # print(response_action)
    allmovie = response_action.find('div', class_='content-text')  # 所有的景点集
    table = allmovie.find('table', id = 'gjajlyjqml')
    masage = response_action.find('table', id = 'gjajlyjqml')
    movies = masage.find_all('tr')
    for movie in movies:
        spot = movie.find_all('td')
        p = spot[2].get_text().strip()  # 景点名称
        t = spot[5].get_text().strip()  # 评定时间
        n = spot[3].get_text().strip()  # 地址
        m = spot[1].get_text().strip()  # 等级
        h = [p, n, m, t]
        print(h)
except Exception as a:
    print(a)
