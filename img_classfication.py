# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 22:11:01 2022

@TwinkelStar: 李星辰
@Email: xingchenziyi@163.com   
 
# ----------------------------------------------
#
#              img_classfication
#               Coding By lxc
#                  图像分类
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
from SerialTool import Serial_Tool

#串口配置 
port = "com4" #设置串口端口
bps = 4800 #设置波特率
timex = 1 #设置

k51 = Serial_Tool(port,bps,timex)
ser = k51.setSerial()

# cap = cv.VideoCapture("E:/MysteriousKnight/keil51/vision_car/resp_ke51_car/car.mp4")
cap = cv.VideoCapture("rtsp://admin:123456789...@169.254.38.154/h264/ch1/main/av_stream")
_, src = cap.read()

if __name__ == "__main__":
    #   模型配置
    PARAMS = {"top_num": 3}
    #   读取本地的private key
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
    
    #计数器
    count = 0
    
    while 1:
        _, src = cap.read()
        frame = cv.resize(src, (1280,640))
        
        if cv.waitKey(12) & 0xFF == ord('d'):
            #   图片需要转码才能实现网络传输
            imgbytes = cv.imencode('.jpg', frame)[1]
            #   调用api进行训练
            response_str = app.camera_video_deticion(imgbytes)
            cv.putText(frame, str("detection object:" + response_str["results"][0]["name"]), (50,130), 
                        cv.FONT_HERSHEY_SIMPLEX, 0.75, (20, 125, 80), 2)
            cv.putText(frame, str(response_str["results"][0]["score"]), (50,170), 
                        cv.FONT_HERSHEY_SIMPLEX, 0.75, (125, 25, 125), 2)
            #   保存结果
            cv.imwrite("../output/classfi"+ str(count) + ".jpg", frame)
            count += 1
            
            
        if cv.waitKey(12) & 0xFF == ord('q'):
            break
        
        cv.putText(frame, str("detection object:" + response_str["results"][0]["name"]), (50,130), 
                    cv.FONT_HERSHEY_SIMPLEX, 0.75, (20, 125, 80), 2)
        cv.putText(frame, str(response_str["results"][0]["score"]), (50,170), 
                    cv.FONT_HERSHEY_SIMPLEX, 0.75, (125, 25, 125), 2)
        
        
        cv.imshow("frame", frame)
        
    cv.waitKey(0)
    cv.destroyAllWindows()