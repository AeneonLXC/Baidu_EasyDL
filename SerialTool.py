# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 11:18:02 2021

@MysteriousKnight: 23608
@Email: xingchenziyi@163.com   
 
# ----------------------------------------------
#
#           Katyusha_Vision_ModuleName_model
#               Coding By lxc
#                  Serial_Tool
#
#          LAST_UPDATE: Wed Nov 10 11:18:02 2021
#
# ----------------------------------------------

"""

"""
目前serial_Tools只有配置串口，发送数据这些功能，还有设置起始位，校验位，停止位，接收数据等功能未完善

安装方法 pip install serial
导入方法 from serial_test import Serial_Tool
"""
import serial
import numpy as np
# 串口对象 
class Serial_Tool:

    def __init__(self, port, bps, timex):
        self.port = port
        self.bps = bps
        self.timex = timex

    def setSerial(self):
        """
        配置串口函数
        Returns 返回串口对象 
        -------
        ser : 串口类 Serial_Tool 
            设置好comx端口，波特率，校验位停止位后返回的对象 .

        """
        try:
            ser = serial.Serial(self.port, self.bps, bytesize=8, parity='N', stopbits=1, timeout=self.timex)
            return ser

        except IOError:  
            print("=======The port is not identified or is occupied !!!=======")
            
        except Exception:
            print("=======setSerial Exception!!!=======")
            
    def getSerialName(self,ser):
        try:
            return  ser.port
        except Exception as e:
            print("=======Not Get Serial Name!!!",e)

    # def sendSerial(self ,ser, message):
    #     """
    #       串口数据发送
    #     Parameters
    #     ----------
    #     ser : serialwin32 
    #         serialwin32.
    #     message : str
    #         字符串数据.

    #     Returns 自定义的串口协议，需要与电控进行沟通定义
    #     可以给定一组特殊数据看看send_total的结果是什么
    #     -------
    #     None.

    #     """
    #     yaw_l_r = np.array([0, 360]) # 设置yaw轴的角度范围
    #     yaw_l_r_m = np.array([0, 8000]) # 设置yaw轴的电机转动范围
        
    #     pitch_l_r = np.array([135, 175])# 设置pitch轴的角度范围
    #     pitch_l_r_m = np.array([3000, 3900])# 设置pitch轴的电机转动范围
        
    #     pitch = np.round((message[0] + pitch_l_r[0]) * (pitch_l_r_m[1] / pitch_l_r[1]), 4) #比例转换np.round保留四位小数
    #     yaw = np.round(message[1] * (yaw_l_r_m[1] / yaw_l_r[1]), 4)#比例转换np.round保留四位小数
        
    #     #限位
    #     if pitch >= pitch_l_r_m[0] and  pitch <= pitch_l_r_m[1] and  yaw >= yaw_l_r_m[0] and yaw <= yaw_l_r_m[1]:
    #         #转化为字符串
    #         list_ptich_yaw = str(pitch) + "." + str(yaw)
    #         split_ptich_yaw = list_ptich_yaw.split(".")
    #         #对字符串进行填充操作 如果值为12.9527 使用zfill后应该为 0012.9527 与电控的协议
    #         ptich1 = split_ptich_yaw[0].zfill(4)
    #         ptich2 = split_ptich_yaw[1].zfill(4)
            
    #         yaw1 = split_ptich_yaw[2].zfill(4)
    #         yaw2 = split_ptich_yaw[3].zfill(4)
    #         #最终的输出结果应该为1234.1234a5678.5678a   与电控的协议
    #         send_total = ptich1 + "." + ptich2 + "a" + yaw1 + "." + yaw2 + "a"
    #         print(send_total)
    #         try:
    #             if type(send_total) == str: 
    #                 #串口数据发送
    #                 ser.write(send_total.encode("gbk"))
    #                 print("Successful Send Message")
    #             else:
    #                 print("Not Send Message")
                    
    #         except Exception as e:
    #             print("=======Send Serial Exception!!!",e)
                
    
    def openSerial(self ,ser):

        try:
            return ser.open()    
        except Exception as e:
            print("=======Send Serial Exception!!!",e)
            
    
    
    def sendSerial(self ,ser, message):
        """
          串口数据发送
        Parameters
        ----------=
        ser : serialwin32 
            serialwin32.
        message : str
            字符串数据.

        Returns 自定义的串口协议，需要与电控进行沟通定义
        可以给定一组特殊数据看看send_total的结果是什么
        -------
        None.

        """
        try:
            if message == 1:
                ser.write(b'\xEE')
                ser.readline()
            elif message == 2:
                ser.write(b'\xFF')
                ser.readline()
            elif message == 3:
                ser.write(b'\xEF')
                ser.readline()
            elif message == 4:
                ser.write(b'\xFE')
                ser.readline()
            elif message == 5:
                ser.write(b'\xFD')
                ser.readline()
            print("Successful Send Message")

        except Exception as e:
            print("=======Send Serial Exception!!!",e)
    
    def readSerialTotal(self, ser):
        """
        Parameters
        ----------
        ser : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        try:
            
            if ser.in_waiting != None:  #判断缓冲区的剩余字节数是否为空
                # str_total = ser.readlines()
                return ser.readline()
            else:
                print("=======Serial Data is None!!!=======")
                
        except Exception as e:
            print("=======Read SerialTotal Exception!!!", e)
        
    def closeSerial(self, ser):
        """
        关闭串口，防止端口被重复占用 

        Parameters
        ----------
        ser : serialwin32
            serialwin32.

        Returns 
        -------

        """        
        try:
            return ser.close()
        except Exception as e:
            print("=======Flase Close Serial !!!", e)
        
# if __name__ == "__main__":
#     port = "com4" #设置串口端口
#     bps = 4800 #设置波特率
#     timex = 1 #设置
    
#     xx = Serial_Tool(port,bps,timex)
#     ser = xx.setSerial()




# ser.write(b'\xfd')
# ser.readline()