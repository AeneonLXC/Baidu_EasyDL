# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 16:07:52 2022

@TwinkelStar: 一直闪闪发光的李星辰
@Email: xingchenziyi@163.com   
 
# ----------------------------------------------
#
#                 getdata
#               Coding By lxc
#            随机抽取2000张图片作为数据集
#
#          LAST_UPDATE: Fri Aug 12 16:07:52 2022
#
# ----------------------------------------------

"""
import os
import numpy as np
import cv2 as cv
import pandas as pd
import shutil
#本地数据集路径
path = "E:/VOC2007/Annotations/"
inputpath = "E:/VOC2007/JPEGImages"

#目标路径
img_outpath = "E:/MysteriousKnight/github_repository/VOC2007/JPEGImages"
xml_outpath = "E:/MysteriousKnight/github_repository/VOC2007/Annotations"

annotations = os.listdir(path)

rand_data = [i for i in range(len(annotations))]

for i in range(len(annotations)):
    annotations[i] = annotations[i].split(".")[0]

#打乱顺序随机抽取
np.random.seed(1)
index = np.random.permutation(len(annotations))
annotations = np.array(annotations)
annotations = annotations[index]

#取出2000张图片以及
img = annotations[:2000]

for i in range(img.shape[0]):
    #只需要运行一次
    if 1 == 0:
        temp_img = cv.imread(inputpath + "/" + img[i] + ".jpg")
        cv.imwrite(img_outpath + "/" + img[i] + ".jpg", temp_img)
    #将标签复制到目标文件夹
    shutil.copy(path + "/" + img[i]+ ".xml", xml_outpath + "/" + img[i]+ ".xml")
