import pygame
from pygame.locals import *
import multiprocessing
from multiprocessing import Pipe 
import subprocess
import time
import numpy as np

class API:
    breathe=["b'\\x02'"]

    def UDP_server(self,pipe):
        with subprocess.Popen(["breathe.py","server"], shell=True,stdout=subprocess.PIPE, universal_newlines=True) as process:
            while True:
                # print("doing server")
                output = process.stdout.readline()
                # print(type(output))
                if output == '' and process.poll() is not None:
                    break
                if output:
                    message=output.strip()
                    pipe.send(message)
            rc = process.poll()


    def pipe_begin(self):#建立pipe
        parent_conn, child_conn=Pipe()

        fa= multiprocessing.Process(target=self.UDP_server,  kwargs={'self':self,'pipe':child_conn})#开启管道的发端，为UDP_test_server函数，管道的接收端就默认为自己了
        fa.start()
        while True:
            temp = parent_conn.recv()
            temp=temp.split()
            
            self.breathe=temp
            time.sleep(0.5)
            # print(self.breathe)

    def get_color(self):
        color=[155,234,199]
        for i in range(len(color)):
            color[i]+=int(np.random.randint(-25,25))
            if color[i]>255:
                color[i]=255
        return(tuple(color))


class BALL:
    x=0
    y=0
    r=0
    distance=0#到
    if_move=1

    def __init__(self,r,x,y):

        x=int(np.random.normal(x,150))
        y=int(np.random.normal(y,150))


        self.r=r
        self.x=x
        self.y=y

        self.dis_x=1200+np.random.randint(-100,100)
        self.dis_y=700+np.random.randint(-100,100)


        self.Stride_x=abs(self.dis_x-x)
        self.Stride_y=abs(self.dis_y-y)
        self.distance=np.sqrt(np.square(self.Stride_x)+np.square(self.Stride_y))
        # print(self.distance)

        self.dis_x_2=np.random.randint(-100,100)
        self.dis_y_2=700+np.random.randint(-100,100)


        self.Stride_x_2=abs(self.dis_x_2-x)
        self.Stride_y_2=abs(self.dis_y_2-y)



    def move(self,end):

        temp_x=600-self.x
        temp_y=350-self.y

        self.distance=np.sqrt(np.square(temp_x)+np.square(temp_y))
        if self.distance>end:
            self.x+=abs(int(self.Stride_x/300))
            self.y+=abs(int(self.Stride_y/300))
        else:
            self.r=1

        if abs(int(self.Stride_x/300))==0:
            self.if_move=0
    def move_2(self,end):

        temp_x=self.x-600
        temp_y=self.y-350
        self.distance=np.sqrt(np.square(temp_x)+np.square(temp_y))
        if self.distance>end:
            self.x-=abs(int(self.Stride_x_2/300))
            self.y-=abs(int(self.Stride_y_2/300))
        else:
            self.r=1

