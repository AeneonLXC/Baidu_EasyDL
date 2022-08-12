# 2022人工智能挑战赛项目代码



说明：本项目的数据集未开源，是我本科的Mentor自己标注的数据集，原数据集总量有10450张，数据集的标签有cargo（包裹），tray（货架）以及forklift（叉车），因参赛需要上传数据集的原因，经过Mentor授权，我可使用2000张数据集作为训练学习使用。本项目代码仅供学习交流使用。

有问题请联系我的邮箱：xingchenziyi@163.com

# 一、项目简介

基于仓储物流识别的人工智能挑战项目，本仓库仅仅有训练代码及相关文档，不包含项目本身的所有程序。



# 二、项目结构

项目分为图像分类以及图像检测两个板块

```python
project
│  baidu_api.py 									#封装好的百度API实例
│  getdata.py									    #数据清洗（伪）
│  img_deticion.py									#视频流的图像分类
│  README.md									    #说明文档
│  基于百度EasyDL的仓储物流识别技术文档V1.0-李星辰.docx  #技术文档
```

# 三、项目环境



|    Software    | Version | Hardware | Version |
| :------------: | :-----: | :------: | :-----: |
|     Python     | 3.7.10  |          |         |
| 百度EasyDL平台 |         |          |         |
|                |         |          |         |

