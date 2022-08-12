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
# cap = cv.VideoCapture("E:/MysteriousKnight/keil51/vision_car/resp_ke51_car/car.mp4")
cap = cv.VideoCapture(0)
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
    
    #   接口返回的数据类型
    response_str = {'log_id': 0,
     'results': [{'name': 'NULL', 'score': 0.0},
      {'name': 'NULL', 'score': 0.0},
      {'name': 'NULL', 'score': 0.0}]}
    
    while 1:
        _, src = cap.read()
        frame = cv.resize(src, (640,360))
        
        if cv.waitKey(12) & 0xFF == ord('d'):
            #   图片需要转码菜才能实现网络传输
            imgbytes = cv.imencode('.jpg', frame)[1]
            #   调用api进行训练
            response_str = app.camera_video_deticion(imgbytes)
            
        if cv.waitKey(12) & 0xFF == ord('q'):
            break
        
        cv.putText(frame, str("detection object:" + response_str["results"][0]["name"]), (50,30), 
                    cv.FONT_HERSHEY_SIMPLEX, 0.75, (20, 125, 80), 2)
        cv.putText(frame, str(response_str["results"][0]["score"]), (50,70), 
                    cv.FONT_HERSHEY_SIMPLEX, 0.75, (125, 25, 125), 2)
        cv.imshow("frame", frame)
        
    cv.waitKey(0)
    cv.destroyAllWindows()