# -*- coding: utf-8 -*-
# Python 3.6
import json

import requests

import pandas as pd

# left_bottom = [112.303081,34.568036];  # 设置区域左下角坐标（百度坐标系）
# right_top = [112.665278,34.75616]; # 设置区域右上角坐标（百度坐标系）
part_n = 5  # 设置区域网格（5*5）

left_bottom = [111.128069, 34.749855]  # 设置区域左下角坐标（百度坐标系）
right_top = [111.2557, 34.806307]  # 设置区域右上角坐标（百度坐标系）
url0 = 'http://api.map.baidu.com/place/v2/search?'
x_item = (right_top[0] - left_bottom[0]) / part_n
y_item = (right_top[1] - left_bottom[1]) / part_n
query = '球馆'  # 搜索关键词设置
ak = '9OYSVVrd1oczyEVFAN********'  # 百度地图api信令
n = 0  # 切片计数器
feature_data = []
for i in range(part_n):
    for j in range(part_n):
        left_bottom_part = [left_bottom[0] + i * x_item,
                            left_bottom[1] + j * y_item]  # 切片的左下角坐标
        right_top_part = [right_top[0] + i * x_item,
                          right_top[1] + j * y_item]  # 切片的右上角坐标
        for k in range(20):
            url = url0 + 'query=' + query + '&coord_type=1' + '&page_size=20&page_num=' + str(k) + '&scope=2&bounds=' + str(
                left_bottom_part[1]) + ',' + str(left_bottom_part[0]) + ',' + str(right_top_part[1]) + ',' + str(right_top_part[0]) + '&output=json&ak=' + ak
            print(url)

            data = requests.get(url).text

            print(data)

            hjson = json.loads(data)

            if hjson['message'] == 'ok':
                datalist = hjson['results']

                for each in datalist:
                    feature_data.append(each)
            # feature=pd.DataFrame(feature_data)
            # else:break

        n += 1
        print('第', str(n), '个切片入库成功')
feature = pd.DataFrame(feature_data)
feature.to_csv('/Users/Data_science/basketball/baskeball_detail_sanmenxia.csv')
