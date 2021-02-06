import pygame
from pygame.locals import *
import time, os
from items_1 import API,BALL
import threading
from threading import Lock, Thread
import numpy as np
import serial
from collections import deque
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation 





if __name__ == "__main__":
    pygame.init()

    serial = serial.Serial('COM3',57600,timeout=2) #连接COM14,波特率57600
    
    a=deque([])
    b=[]


    fig, ax = plt.subplots()          #生成轴和fig,  可迭代的对象
    x, y= [], []    #用于接受后更新的数据
    line, = plt.plot([], [], '.-')   #绘制线对象，plot返回值类型，要加逗号


    circle_init=pygame.image.load(r'D:\\ForStudy\Desktop\\Xbot\\1.png')
    MAX_r=200
    MIN_r=100
    r=MIN_r
    flag=0
    SUSPEND=0#暂停信号
    small_ball=[]
    color=[]
    small_ball_num=20
    divider=0#分频器

    screen = pygame.display.set_mode((1200, 700), 0, 32)
    pygame.display.set_caption("demo_1")
    api=API
      
    # server=Thread(target=api.pipe_begin,args=(api,))
    # server.start()
    while True:
        screen.fill((255,255,255)) 
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    print("click 3")
                    SUSPEND=1
                    api.breathe=['222222']
                if event.button == 1:
                    print("click 3")
                    SUSPEND=0


        if SUSPEND==1:
            api.breathe=['222222']
        else:
            pass


        data=serial.read(1)
        text=bytes.decode(data)
        # print(text)
        if text != '\r' and text != '\n':
            a.append(text)
        if text == '\r':
            temp=''
            r=(int(temp.join(a))-28000)/10
            a=deque([])




        # screen.blit(circle_init,(500,350))
        pygame.draw.circle(screen, (155,234,199), (600,350), r)
        print(r)

        # flag=int(api.breathe[0][5])
        # # print(flag,type(flag))
        # if flag==0:
        #     r+=2
        #     if r>MAX_r:
        #         flag=1
        # elif flag==1:
        #     r-=2
        #     if r<MIN_r:
        #         flag=0

        if divider==0:
            # small_ball=[]
            # color=[]


            # for i in range(np.random.randint(5,10)):
            #     small_ball.append(BALL(np.random.randint))
            #     b=BALL(10,0,0)
            #     print(b.Stride_x,b.Stride_y,b.distance)

            for i in range(20):

                color.append(api.get_color(api))
                temp=BALL(np.random.randint(6,9),300,300)
                small_ball.append(temp)




            

            #随机生成更多
            # for i in range(small_ball_num):
            #     small_ball.append([np.random.randint(10,1000),np.random.randint(10,600), np.random.randint(5,15)])
        
        # for i in small_ball:
        #     pygame.draw.circle(screen, (155,107,144), (i[0],i[1]), i[2])
       


        for i in range(len(small_ball)):

            small_ball[i].move(r)
            pygame.draw.circle(screen,color[i], (small_ball[i].x , small_ball[i].y), small_ball[i].r)
        # print(b.distance)




        #分频
        if divider<1:
            divider+=0.01
        else:
            divider=0


        time.sleep(0.002)
        pygame.display.update()

