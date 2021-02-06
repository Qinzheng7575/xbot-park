import pygame
from pygame.locals import *
import time, os
from items_1 import API,BALL
import threading
from threading import Lock, Thread
import numpy as np
import copy

if __name__ == "__main__":
    pygame.init()
    
    circle_init=pygame.image.load(r'D:\\ForStudy\Desktop\\Xbot\\1.png')
    MAX_r=200
    MIN_r=100
    r=MIN_r
    r_last=MIN_r
    flag=0
    SUSPEND=0#暂停信号
    small_ball=[]
    small_ball_2=[]
    color=[]
    color_2=[]
    small_ball_num=20
    divider=0#分频器
    divider_text=0

    ttf_abs ='C:\Windows\Fonts\simhei.ttf'
    myfront  = pygame.font.Font(ttf_abs, 22)
    screen = pygame.display.set_mode((1200, 700), 0, 32)
    pygame.display.set_caption("demo_1")
    api=API

    server=Thread(target=api.pipe_begin,args=(api,))
    server.start()
    
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

        # screen.blit(circle_init,(500,350))


        flag=int(api.breathe[0][5])
        # print(flag,type(flag))
        if flag==0:
            r_last=r
            r+=1
            if r>MAX_r:
                flag=1
        elif flag==1:
            r_last=r
            r-=1
            if r<MIN_r:
                flag=0

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

                color_2.append(api.get_color(api))
                temp_2=BALL(np.random.randint(6,9),900,400)
                small_ball_2.append(temp_2)




        for i in range(len(small_ball)):

            if small_ball[i].if_move!=0:
                small_ball[i].move(r)
                pygame.draw.circle(screen,color[i], (small_ball[i].x , small_ball[i].y), small_ball[i].r)
        # print(b.distance)
            if small_ball_2[i].if_move!=0:
                small_ball_2[i].move_2(r)
                pygame.draw.circle(screen,color_2[i], (small_ball_2[i].x , small_ball_2[i].y), small_ball_2[i].r)


        pygame.draw.circle(screen, (155,234,199), (600,350), r)
        # pygame.draw.circle(screen, (160,102,211), (600,350), r+20,6)


        if divider_text<100:
            text_big1 = myfront.render("放松", 1, (160,102,211))
            screen.blit(text_big1,(600+r+40,350))
        elif 250<divider_text<300:
            text_big1 = myfront.render("很好，就这样子", 1, (160,102,211))
            screen.blit(text_big1,(600+r+40,350))
        else:
            
            if r_last<r:
                text_big1 = myfront.render("请缓慢吸气", 1, (160,102,211))
                screen.blit(text_big1,(600+r+40,350))
            elif r_last>r:
                text_big1 = myfront.render("请缓慢呼气", 1, (160,102,211))
                screen.blit(text_big1,(600+r+40,350))


        #分频
        if divider<1:
            divider+=0.01
        else:
            divider=0

        if divider_text<300:
            divider_text+=1
        else:
            divider_text=0


        time.sleep(0.03)
        pygame.display.update()

