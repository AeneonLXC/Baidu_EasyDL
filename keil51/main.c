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

unsigned char Counter,Compare;	//����ֵ�ͱȽ�ֵ���������PWM
unsigned char KeyNum,Speed;
unsigned char Brain; //ָ����

void control(unsigned char msg){
	unsigned char WARD = 0X0A;//ǰ��
	unsigned char BACK = 0XFF;//����
	
	unsigned char LEFT = 0XEF;//��ת
	unsigned char RIGHT = 0XFE;//��ת

	unsigned char STOP = 0XFD;// ֹͣ
	
//	unsigned char WARD = 61;//ǰ��
//	unsigned char BACK = 62;//����
//	
//	unsigned char LEFT = 63;//��ת
//	unsigned char RIGHT = 64;//��ת

//	unsigned char STOP = 65;// ֹͣ

	Compare=50;
	if(msg==WARD)
		{
//			Speed++;                                                 
//			Speed%=4;
//			if(Speed==0){Compare=0;}	//���ñȽ�ֵ���ı�PWMռ�ձ�
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
	UART_Init();		//���ڳ�ʼ��
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
	TL0 = 0x9C;		//���ö�ʱ��ֵ
	TH0 = 0xFF;		//���ö�ʱ��ֵ
	Counter++;
	Counter%=100;	//����ֵ�仯��Χ������0~99
	if(Counter<Compare)	//����ֵС�ڱȽ�ֵ
	{
		if(Brain==1)	//����ֵС�ڱȽ�ֵ
	{
		MotorL=1;		//ǰ��
		MotorR=1;	
		L_LN4=0;
		L_LN3=1;
		R_LN1=0;
		R_LN2=1;

	}
	else if(Brain==2){
		MotorL=1;		//����
		MotorR=1;	
		L_LN4=1;
		L_LN3=0;
		R_LN1=1;
		R_LN2=0;
	}
		else if(Brain==3){
		MotorL=1;		//��ת
		MotorR=1;	
		L_LN4=0;
		L_LN3=0;
		R_LN1=1;
		R_LN2=0;
	}
		else if(Brain==4){
		MotorL=1;		//��ת
		MotorR=1;	
		L_LN4=1;
		L_LN3=0;
		R_LN1=0;
		R_LN2=0;
	}
		else if(Brain==0){
		MotorL=0;		//ֹͣ
		MotorR=0;	
		L_LN4=0;
		L_LN3=0;
		R_LN1=0;
		R_LN2=0;
	}
}
	else{
		MotorL=0;		//ֹͣ
		MotorR=0;	
	}
	
}
void UART_Routine() interrupt 4
{
	if(RI==1)					//������ձ�־λΪ1�����յ�������
	{
		P2=SBUF;				//��ȡ����
		UART_SendByte(SBUF);	//���ܵ������ݷ��ش���
		RI=0;					//���ձ�־λ��0
		
	}
}
