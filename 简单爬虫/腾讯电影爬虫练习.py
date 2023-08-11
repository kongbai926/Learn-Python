import requests
import openpyxl
import json
from bs4 import BeautifulSoup

try:
    uil2 = 'https://v.qq.com/x/bu/pagesheet/list?append=1&channel=movie&itype=100061&listpage=2&offset='+'30'+'&pagesize=30'
    header2 = {
'referer': 'https://v.qq.com/channel/movie?listpage=1&channel=movie&itype=100061',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    }
    data= {
        'append': '1',
'channel': 'movie',
'itype': '100061',
'listpage':' 2',
'offset': '30',
'pagesize':' 30'}
    resques = requests.get(uil2,headers=header2,data=data)
    print(resques.status_code)
    resques.encoding ='utf-8'
    respon = BeautifulSoup(resques.text, 'html.parser')
    da = respon.find('div', class_="list_item")
    strs = da.find('a').find_all("div")
    print(strs)
    print(strs[1].text)

except Exception as a:
    print(a)