# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 22:11:01 2022

@TwinkelStar: 一直闪闪发光的李星辰
@Email: xingchenziyi@163.com   
 
# ----------------------------------------------
#
#               图像分类代码示例
#               Coding By lxc
#                  基于EasyDL
#
#          LAST_UPDATE: Fri Aug 12 22:11:01 2022
#
# ----------------------------------------------

"""

import numpy as np
import cv2 as cv
import pandas as pd
import base64
from baidu_api import BaiduApi
cap = cv.VideoCapture("E:/MysteriousKnight/keil51/vision_car/resp_ke51_car/car.mp4")
_, src = cap.read()

if __name__ == "__main__":
    #   模型配置
    PARAMS = {"top_num": 3}
    key = pd.read_excel(r"E:\MysteriousKnight\github_repository\VOC2007\apiKey.xls")
    key = np.array(key)
    MODEL_API_URL = key[0,1]
    ACCESS_TOKEN = key[1,1]
    API_KEY = key[2,1]
    SECRET_KEY = key[3,1]
    
    app = BaiduApi(PARAMS, MODEL_API_URL,
                   ACCESS_TOKEN,
                   API_KEY,SECRET_KEY)
    
    img_path = "E:/MysteriousKnight/github_repository/VOC2007/Image/mvi_4531_000008.jpg"
    while 1:
        _, src = cap.read()

        frame = cv.resize(src, (640,360))
        cv.imshow("frame", frame)
        # cv.imshow("hsv", hsv)
        if cv.waitKey(12) & 0xFF == ord('d'):
            imgbytes = cv.imencode('.jpg', frame)[1]
            app.camera_video_deticion(imgbytes)
        if cv.waitKey(12) & 0xFF == ord('q'):
            break

    cv.waitKey(0)
    cv.destroyAllWindows()