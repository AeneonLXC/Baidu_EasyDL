# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 18:39:52 2022

@TwinkelStar: 一直闪闪发光的李星辰
@Email: xingchenziyi@163.com   
 
# ----------------------------------------------
#
#                   baidu_api
#               Coding By lxc
#            部署模型示例，可支持图片、视频流检测
#
#
#          LAST_UPDATE: Fri Aug 12 18:39:52 2022
#
# ----------------------------------------------

"""


"""
EasyDL 图像分类 调用模型公有云API Python3实现
"""

import json
import base64
import requests
import pandas as pd
import numpy as np

"""
使用 requests 库发送请求
使用 pip（或者 pip3）检查我的 python3 环境是否安装了该库，执行命令
  pip freeze | grep requests
若返回值为空，则安装该库
  pip install requests
"""
class BaiduApi:
    def __init__(self,PARAMS,MODEL_API_URL,ACCESS_TOKEN,API_KEY,SECRET_KEY):
        # 可选的请求参数
        # top_num: 返回的分类数量，不声明的话默认为 6 个
        self.PARAMS = PARAMS
        # 服务详情 中的 接口地址
        self.MODEL_API_URL = MODEL_API_URL
        #token
        self.ACCESS_TOKEN = ACCESS_TOKEN
        #apikey
        self.API_KEY = API_KEY
        #secret key
        self.SECRET_KEY = SECRET_KEY

    def img_deticion(self,img_path):
        # 目标图片的 本地文件路径，支持jpg/png/bmp格式
        IMAGE_FILEPATH = img_path
        print("1. 读取目标图片 '{}'".format(IMAGE_FILEPATH))
        with open(IMAGE_FILEPATH, 'rb') as f:
            base64_data = base64.b64encode(f.read())
            base64_str = base64_data.decode('UTF8')
        print("将 BASE64 编码后图片的字符串填入 PARAMS 的 'image' 字段")
        self.PARAMS["image"] = base64_str

        if not self.ACCESS_TOKEN:
            print("2. ACCESS_TOKEN 为空，调用鉴权接口获取TOKEN")
            auth_url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials"\
               "&client_id={}&client_secret={}".format(self.API_KEY, self.SECRET_KEY)
            auth_resp = requests.get(auth_url)
            auth_resp_json = auth_resp.json()
            ACCESS_TOKEN = auth_resp_json["access_token"]
            print("新 ACCESS_TOKEN: {}".format(ACCESS_TOKEN))
        else:
            print("2. 使用已有 ACCESS_TOKEN")
        
        print("3. 向模型接口 'MODEL_API_URL' 发送请求")
        request_url = "{}?access_token={}".format(self.MODEL_API_URL, self.ACCESS_TOKEN)
        response = requests.post(url=request_url, json=self.PARAMS)
        response_json = response.json()
        response_str = json.dumps(response_json, indent=4, ensure_ascii=False)
        print("结果:{}".format(response_str))
        return response_str
        
    def camera_video_deticion(self,img_bytes):
        # 目标图片的 本地文件路径，支持jpg/png/bmp格式

        # print("1. 图片维度 '{}', '{}'".format(img.shape[0],img.shape[0]))
        base64_data = base64.b64encode(img_bytes)
        base64_str = base64_data.decode('UTF8')
        print("将 BASE64 编码后图片的字符串填入 PARAMS 的 'image' 字段")
        self.PARAMS["image"] = base64_str

        if not self.ACCESS_TOKEN:
            print("2. ACCESS_TOKEN 为空，调用鉴权接口获取TOKEN")
            auth_url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials"\
               "&client_id={}&client_secret={}".format(self.API_KEY, self.SECRET_KEY)
            auth_resp = requests.get(auth_url)
            auth_resp_json = auth_resp.json()
            ACCESS_TOKEN = auth_resp_json["access_token"]
            print("新 ACCESS_TOKEN: {}".format(ACCESS_TOKEN))
        else:
            print("2. 使用已有 ACCESS_TOKEN")
        
        print("3. 向模型接口 'MODEL_API_URL' 发送请求")
        request_url = "{}?access_token={}".format(self.MODEL_API_URL, self.ACCESS_TOKEN)
        response = requests.post(url=request_url, json=self.PARAMS)
        response_json = response.json()
        response_str = json.dumps(response_json, indent=4, ensure_ascii=False)
        print("结果:{}".format(response_str))
        return response_json
        
# if __name__ == "__main__":
#     PARAMS = {"top_num": 3}
#     key = pd.read_excel(r"E:\MysteriousKnight\github_repository\VOC2007\apiKey.xls")
#     key = np.array(key)
#     MODEL_API_URL = key[0,1]
#     ACCESS_TOKEN = key[1,1]
#     API_KEY = key[2,1]
#     SECRET_KEY = key[3,1]
#     app = BaiduApi(PARAMS, MODEL_API_URL,
#                    ACCESS_TOKEN,
#                    API_KEY,SECRET_KEY)

#     img_path = "E:/MysteriousKnight/github_repository/VOC2007/Image/mvi_4531_000008.jpg"
#     app.img_deticion(img_path)
    

