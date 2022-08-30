# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 08:21:07 2022

@TwinkelStar: 李星辰
@Email: xingchenziyi@163.com   
 
# ----------------------------------------------
#
#               img_detecion
#               Coding By lxc
#                  图像检测
#
#      LAST_UPDATE: Sat Aug 13 08:21:07 2022
#
# ----------------------------------------------

"""
import numpy as np
import cv2 as cv
import pandas as pd
import base64
import time
from baidu_api import BaiduApi
from SerialTool import Serial_Tool

#串口配置 
port = "com4" #设置串口端口
bps = 4800 #设置波特率
timex = 1 #设置

k51 = Serial_Tool(port,bps,timex)
ser = k51.setSerial()


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
    leftx = img.shape[0]/2 / 2
    widthx = img.shape[0]/2 / 2
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
                       cv.putText(img, str(score) + "%", (left + 70, top), 
                                    cv.FONT_HERSHEY_SIMPLEX, 0.75, (125, 25, 125), 2)
                       leftx = left
                       widthx = width
    return leftx +  widthx/2
def control(point,img):
    
    if point <= img.shape[0]/2 - 100:
        k51.sendSerial(ser, 3)
    elif point >= img.shape[0]/2 + 100:
        k51.sendSerial(ser, 4)
    elif point <= img.shape[0]/2 - 50:
        k51.sendSerial(ser, 1)
    elif point >= img.shape[0]/2 + 50:
        k51.sendSerial(ser, 2)
    elif point >= img.shape[0]/2 + 30 or point <= img.shape[0]/2 - 30:
        k51.sendSerial(ser, 5)
    else:
        k51.sendSerial(ser, 5)
      
def getpos(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        if x < 100 :
            k51.sendSerial(ser, 1)
            print(x)
        if x > 100 and x < 200:
            k51.sendSerial(ser, 2)
            print(x)
        if x > 200 and x < 300:
            k51.sendSerial(ser, 3)
            print(x)
        if x > 300 and x < 400 :
            k51.sendSerial(ser, 4)
            print(x)
        if x > 400 and x < 500 :
            k51.sendSerial(ser, 5)
            print(x)
    
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
    
    # cap = cv.VideoCapture("E:/MysteriousKnight/keil51/vision_car/resp_ke51_car/car.mp4")
    cap = cv.VideoCapture("rtsp://admin:123456789...@169.254.38.154/h264/ch1/main/av_stream")
    _, src = cap.read()
    
    #   计数器
    count = 0
    while 1:
        _, src = cap.read()
        frame = cv.resize(src, (1280,640))
        
        if 1==1:
            #鼠标控制显示区域 点击方框内的像素
            cv.line(frame, (100,0), (100,100), (125, 25, 125),3)
            cv.line(frame, (200,0), (200,100), (125, 25, 125),3)
            cv.line(frame, (300,0), (300,100), (125, 25, 125),3)
            cv.line(frame, (400,0), (400,100), (125, 25, 125),3)
            cv.line(frame, (500,0), (500,100), (125, 25, 125),3)
            cv.line(frame, (0,100), (500,100), (125, 25, 125),3)
            if cv.waitKey(1) & 0xFF == ord('d'):
          # 图片需要转码才能实现网络传输
                imgbytes = cv.imencode('.jpg', frame)[1]
                #   调用api进行检测
                response_dict = app.camera_video_deticion(imgbytes)
                pointx = img_confirm(response_dict,frame)
                control(pointx,frame)
                #   保存结果
                cv.imwrite("../output/detection"+ str(count) + ".jpg", frame)
                count += 1
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
        cv.imshow("frame", frame)
        cv.setMouseCallback("frame", getpos)
        
    cv.waitKey(0)
    cv.destroyAllWindows()
