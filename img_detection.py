# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 08:21:07 2022

@TwinkelStar: 一直闪闪发光的李星辰
@Email: xingchenziyi@163.com   
 
# ----------------------------------------------
#
#               img_detecion
#               Coding By lxc
#                  图像检测
#
#          LAST_UPDATE: Sat Aug 13 08:21:07 2022
#
# ----------------------------------------------

"""
import numpy as np
import cv2 as cv
import pandas as pd
import base64
import time
from baidu_api import BaiduApi
# cap = cv.VideoCapture("E:/MysteriousKnight/keil51/vision_car/resp_ke51_car/car.mp4")
cap = cv.VideoCapture(0)
_, src = cap.read()

def img_confirm(response_dict, img):
    """
    图像检测确认函数

    Parameters
    ----------
    response_dict : dict
        服务器返回的数据.
    img : mat
        待检测的图像.
    Returns
    -------
    None.

    """
    #   判断检测列表是否为空
    if len(response_dict["results"]) != 0:
        for i in range(len(response_dict["results"])):
                       name = response_dict["results"][i]["name"]
                       score = round(response_dict["results"][0]["score"] * 100,2)
                       height = response_dict["results"][i]["location"]["height"]
                       left = response_dict["results"][i]["location"]["left"]
                       top = response_dict["results"][i]["location"]["top"]
                       width = response_dict["results"][i]["location"]["width"]
                       cv.rectangle(img, (left, top), (left +  width,top + height), (25, 200, 20), 3)
                       
                       cv.putText(img, str(name), (left, top), 
                                    cv.FONT_HERSHEY_SIMPLEX, 0.75, (20, 125, 80), 2)
                       cv.putText(img, str(score), (left + 50, top), 
                                    cv.FONT_HERSHEY_SIMPLEX, 0.75, (125, 25, 125), 2)

if __name__ == "__main__":
    #   模型配置
    PARAMS = {"top_num": 6}
    #   读取本地的private key
    key = pd.read_excel(r"E:\MysteriousKnight\github_repository\VOC2007\apiKey.xls")
    key = np.array(key)
    MODEL_API_URL = key[0,3]
    ACCESS_TOKEN = key[1,3]
    API_KEY = key[2,3]
    SECRET_KEY = key[3,3]
    
    app = BaiduApi(PARAMS, MODEL_API_URL,
                   ACCESS_TOKEN,
                   API_KEY,SECRET_KEY)
    
    img_path = "E:/MysteriousKnight/github_repository/VOC2007/Image/mvi_4531_000008.jpg"
    
    while 1:
        _, src = cap.read()
        frame = cv.resize(src, (640,360))
        
        if 1==1:
            if cv.waitKey(12) & 0xFF == ord('d'):
                #   图片需要转码菜才能实现网络传输
                imgbytes = cv.imencode('.jpg', frame)[1]
                #   调用api进行训练
                response_dict = app.camera_video_deticion(imgbytes)
                img_confirm(response_dict,frame)
            
        if cv.waitKey(60) & 0xFF == ord('q'):
            break
        cv.imshow("frame", frame)
        
    cv.waitKey(0)
    cv.destroyAllWindows()
