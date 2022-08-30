#include <REGX52.H>
#include "Delay.h"
#include "Key.h"
#include "Nixie.h"
#include "Timer0.h"
#include "UART.h"
sbit MotorL=P1^7;
sbit L_LN4=P1^6;
sbit L_LN3=P1^5;

sbit MotorR=P1^0;
sbit R_LN1=P1^1;
sbit R_LN2=P1^2;

unsigned char Counter,Compare;	//计数值和比较值，用于输出PWM
unsigned char KeyNum,Speed;
unsigned char Brain; //指令器

void control(unsigned char msg){
	unsigned char WARD = 0X0A;//前进
	unsigned char BACK = 0XFF;//后退
	
	unsigned char LEFT = 0XEF;//左转
	unsigned char RIGHT = 0XFE;//右转

	unsigned char STOP = 0XFD;// 停止
	
//	unsigned char WARD = 61;//前进
//	unsigned char BACK = 62;//后退
//	
//	unsigned char LEFT = 63;//左转
//	unsigned char RIGHT = 64;//右转

//	unsigned char STOP = 65;// 停止

	Compare=50;
	if(msg==WARD)
		{
//			Speed++;                                                 
//			Speed%=4;
//			if(Speed==0){Compare=0;}	//设置比较值，改变PWM占空比
//			if(Speed==1){Compare=50;}
//			if(Speed==2){Compare=75;}
//			if(Speed==3){Compare=100;}
			Brain=1;
		}
		else if(msg==BACK){
			Brain=2;
		}
		else if(msg==LEFT){
			Brain=3;
		}
		else if(msg==RIGHT){
			Brain=4;
		}
		else if(msg==STOP){
			Brain=0;
		}
//		else{
//		Brain=1;
//		}

}
void main()
{
	UART_Init();		//串口初始化
	Timer0_Init();

	
	while(1)
	{
		KeyNum=Key();
//		if(KeyNum == 1){
//			control(SBUF);
//		}
		control(SBUF);
		

		
//		Nixie(1,Speed);
	}
}

void Timer0_Routine() interrupt 1
{
	TL0 = 0x9C;		//设置定时初值
	TH0 = 0xFF;		//设置定时初值
	Counter++;
	Counter%=100;	//计数值变化范围限制在0~99
	if(Counter<Compare)	//计数值小于比较值
	{
		if(Brain==1)	//计数值小于比较值
	{
		MotorL=1;		//前进
		MotorR=1;	
		L_LN4=0;
		L_LN3=1;
		R_LN1=0;
		R_LN2=1;

	}
	else if(Brain==2){
		MotorL=1;		//后退
		MotorR=1;	
		L_LN4=1;
		L_LN3=0;
		R_LN1=1;
		R_LN2=0;
	}
		else if(Brain==3){
		MotorL=1;		//左转
		MotorR=1;	
		L_LN4=0;
		L_LN3=0;
		R_LN1=1;
		R_LN2=0;
	}
		else if(Brain==4){
		MotorL=1;		//右转
		MotorR=1;	
		L_LN4=1;
		L_LN3=0;
		R_LN1=0;
		R_LN2=0;
	}
		else if(Brain==0){
		MotorL=0;		//停止
		MotorR=0;	
		L_LN4=0;
		L_LN3=0;
		R_LN1=0;
		R_LN2=0;
	}
}
	else{
		MotorL=0;		//停止
		MotorR=0;	
	}
	
}
void UART_Routine() interrupt 4
{
	if(RI==1)					//如果接收标志位为1，接收到了数据
	{
		P2=SBUF;				//读取数据
		UART_SendByte(SBUF);	//将受到的数据发回串口
		RI=0;					//接收标志位清0
		
	}
}
