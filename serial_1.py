import serial
import time
from collections import deque
# import matplotlib.pyplot as plt

#连接串口
serial = serial.Serial('COM3',57600,timeout=2) #连接COM14,波特率位115200
if serial.isOpen():
    print ('串口已打开')
else:
    print ('串口未打开')

a=deque([])
b=[]
while True :

    data=serial.read(1)
    text=bytes.decode(data)
    # print(text)
    if text != '\r' and text != '\n':
        a.append(text)
    if text == '\r':
        temp=''
        b.append(int(temp.join(a)))
        a=deque([])



    print(b)
    # plt.plot(b)
    # plt.draw()
    time.sleep(0.05)
# data=serial.read(2)
# text=bytes.decode(data)
# print(text)




# #关闭串口
# serial.close()
 
# if serial.isOpen():
#     print ('串口未关闭')
# else:
#     print ('串口已关闭')