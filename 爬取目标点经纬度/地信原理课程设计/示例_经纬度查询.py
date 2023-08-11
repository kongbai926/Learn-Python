"""
GIS开发语言实验中的某个小实验（有改动）；
通过传入单个地址名称查询地址经纬度。
"""

import json
import re

import requests


def get_get_location_m(name):  # 获取传入地址的经纬度
    url = "https://restapi.amap.com/v3/place/text?s=rsv3" \
          "&children=&key=2f6ff4a7b02e3ba9d54144affb4f1f0f&jscode=2e5bd0f01c4cabaf209cb9be81c24504&page=1" \
          "&offset=10&city=510100&language=zh_cn" \
          "&callback=jsonp_755735_" \
          "&platform=JS&logversion=2.0" \
          "&sdkversion=1.3" \
          "&appname=https%3A%2F%2Flbs.amap.com%2Fconsole%2Fshow%2Fpicker" \
          "&csid=F028E84F-6601-43AE-88A8-13425E3DE7C7" \
          "&keywords={}".format(name)  # 在线地图的网址
    res_text = requests.get(url).text  # 获取请求返回的response数据的文本数据
    if re.findall('"info":"OK"', res_text):  # 判断返回数据是否成功，成功便继续
        res_data = json.loads(res_text.replace(re.findall("jsonp_\d+_\(", res_text)[0], "")[0:-1])["pois"][0]
        item = {
            "name": res_data["name"], "type": res_data["type"], "location": res_data["location"],
            "pname": res_data["pname"], "cityname": res_data["cityname"],
            "adname": res_data["adname"]}  # 返回请求获得的数据，对其进行装饰，将name\localtion等数据进行赋值，便于后续应用与理解
        return item  # 返回
    else:  # 如果请求错误，则返回None
        return None


print(get_get_location_m("建设一路  武汉科技大学")['location'])  # 输出地址的经纬度
