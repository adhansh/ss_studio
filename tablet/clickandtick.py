#from glob import glob
from tkinter import *
import tkinter.ttk

import threading

import socket
from _thread import *

import pygame


#import re

# 타이머 클라이언트'
# 타이머 기능을 수행한다.
#   타이머 버튼을 누를때마다상태를 서버로 알린다
#   타이머 Start 버튼이 촬영 1주기로 수행된다.


# 흑백/컬러 전환을 할 수 있다.
#   서버와 연결이 안되면 해당 버튼을 비활성한다.

# 별도의 통신 thread는 불필요 할듯 하다.
# 통신 소켓은 전역으로 관리된다.

# socket 관련 전역 변수

# 서버 아이피 주소
HOST = '192.168.0.13'
PORT = 9999
bIsConnected = True

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    client_socket.connect((HOST, PORT))
except:
    print('>> connection error\n')
    bIsConnected = False   

if (True == bIsConnected):
    print('>> Connect server\n')

arrTimeSetStr = [
                "15 min",
                "5 min",
                "30 min",
                "1 min"]

arrTimeSetVal = [15, 5, 30, 1]

nMin = 0
nSec = 0
bStop = True
strTime = '00:{0:02d}:{1:02d}'.format(nMin, nSec)

pygame.mixer.init()
ring = pygame.mixer.Sound('[효과음]정각알림.mp3')

###### socket 관련 함수정의
def Send(msg):
    global client_socket
    
    if (bIsConnected):
        client_socket.send(msg.encode())
    
###### UI관련 함수 정의
def Beep():
    print('RRrrrRrRrrRrrRrRrrr')
    msg ='>> ------ TIMES UP!!!!! RRrrrRrRrrRrrRrRrrr --------'
    Send(msg)
    ring.play(-1)
    
def TickingTime():
    global nSec
    global nMin
    global bStop
    
    if (0 == nSec) and (0 == nMin):
        bStop = True
        Beep()
    
    if False == bStop:    
        print('ticking')
                    
        if nSec == 0:
            print('nsec = 0')
            nSec = 59
            nMin -= 1
        else:
            print('--nSec')
            nSec -= 1
        
        UpdateTime()        
        
        timer = threading.Timer(1, TickingTime)
        timer.start()     

def UpdateTime():
    global strTime
    global labelTime
    global nSec
    global nMin
    
    if nMin == 0:
        labelTime.config(fg="deep pink")
        if 59 == nSec:
            msg ='>> ------ 1 MIN LEFT --------'
            Send(msg)
        elif 30 == nSec:
            msg ='>> ------ 30 SEC LEFT --------'
            Send(msg)
        elif 10 == nSec:
            msg ='>> ------ 10 SEC LEFT --------'
            Send(msg)
        elif 4 > nSec:
            msg ='>> ------ {0:02d} LEFT --------'.format(nSec)
            Send(msg)
        
    else:
        labelTime.config(fg="grey30")
        
    
    strTime = '00:{0:02d}:{1:02d}'.format(nMin, nSec)
    labelTime.config(text=strTime)
    
def InitTime():
    global nSec
    global nMin
    
    nMin = arrTimeSetVal[cmbTime.current()]
    nSec = 0
    
    UpdateTime()


def Start():
    global bStop
    
    if bStop == True:
        bStop = False
        TickingTime()
        
    msg ='>> Click Start'
    Send(msg)
    
def Pause():
    global bStop
    global ring
    
    bStop = True
    msg ='>> Click Pause'
    Send(msg)
    
    ring.stop()
    
def Reset():
    global bStop
    global ring
    
    bStop = True
    InitTime()
    
    msg ='>> Click Reset'
    Send(msg)
    
    ring.stop()


    

def ComboSelected(event):
    global bStop
    global nSec
    
    if (bStop == True) and (nSec == 0):
        InitTime()
    
    msg ='>> Set Combo' +  arrTimeSetStr[cmbTime.current()]
    Send(msg)
    
def SetMono():
    msg ='cmd:mono'
    Send(msg)
    msg ='>> Set Mono'
    Send(msg)

def SetColor():
    msg ='cmd:color'
    Send(msg)
    msg ='>> Set Color'
    Send(msg)
    

root = Tk()

def Quit():
    global root
    global client_socket
    
    msg ='>> Quit'
    Send(msg)
    
    client_socket.close()
    root.quit()
    
def DoCmdJob(cmd):
    global nSec
    global nMin
    
    if 'cmd:start' == cmd:
        print('run cmd(start)')
        Start()
    elif 'cmd:pause' == cmd:
        print('run cmd(pause)')
        Pause()
    elif 'cmd:reset' == cmd:
        print('run cmd(reset)')
        Reset()
    elif 'cmd:time' == cmd:
        print('run cmd(time)')
        
        msg = '>> re>>time : 00:{0:02d}:{1:02d}'.format(nMin, nSec)
        Send(msg)
        
    elif 'cmd:mono' == cmd:
        print('run cmd(mono)')
        #SetMono()
        
    elif 'cmd:color' == cmd:
        print('run cmd(color)')
        #SetColor()
        
    elif 'cmd:coloruser' == cmd:
        print('run cmd(coloruser)')
        btnColor['text'] = '컬러촬영'
        btnColor['state'] = 'normal'
        #SetColor()
    elif 'cmd:monouser' == cmd:
        print('run cmd(monouser)')
        btnColor['text'] = '컬러촬영\n(사용불가)'
        btnColor['state'] = 'disabled'
        #SetColor()

def recv_data(client_socket) :
    while True :
        data = client_socket.recv(1024)
        #recv_msg = repr(data.decode())
        recv_msg = str(data.decode())

        if 'cmd:' in recv_msg:
            print(recv_msg)
            DoCmdJob(recv_msg)
        else:
            print('msg : ', recv_msg)
        #if (None != regex):
        #    regex = re.split(r'[ :]', recv_msg)
        #    print(regex)
        

root.title("SS TIMER. [ Enjoy this time:) ]")
root.attributes('-fullscreen', True)
root.resizable(False, False)

# 상단 프레임 (Pack 사용)
frame_top = Frame(root)
frame_top.pack(side="top")

labelTime = Label(frame_top, text=strTime, font=('Helvetica', 200), fg='grey30')
labelTime.pack(side='top')

# 하단 프레임 (Grid 사용)
frame_bot = Frame(root)
frame_bot.pack(side="top")

#now = time.strftime("%H:%M:%S")
#cmbTime = ComboBox(root, arrTimeSetStr)

cmbTime = tkinter.ttk.Combobox(frame_bot, font=('Helvetica', 20), height=40, width=15, values=arrTimeSetStr)
cmbTime.current(0)
cmbTime.bind("<<ComboboxSelected>>", ComboSelected)
#cmbTime.pack()


btnStart = Button(frame_bot, text = 'start', font=('Helvetica', 20), background='DarkSeaGreen1', command = Start, width=20, height=1)
#btnStart.pack()
btnPause = Button(frame_bot, text = 'pause', font=('Helvetica', 20), background='coral', command = Pause, width=20, height=1)
#btnPause.pack()
btnReset = Button(frame_bot, text = 'reset', font=('Helvetica', 20), background='pink', command = Reset, width=20, height=1)
#btnReset.pack()
btn_quit = Button(frame_bot, text='Quit', background='white', font=('Helvetica', 20), command = Quit, width=20, height=1)
#btn_quit.pack()

cmbTime.grid(row=1, column=1)
btn_quit.grid(row=1, column=3)
btnStart.grid(row=2, column=1)
btnPause.grid(row=2, column=2)
btnReset.grid(row=2, column=3)

if (True == bIsConnected):
    btnMono = Button(frame_bot, text = '흑백촬영', font=('MALGUN', 40), background='Gray', command = SetMono, width=10, height=3)
    btnColor = Button(frame_bot, text = '컬러촬영', font=('MALGUN', 40), background='magenta', command = SetColor, width=10, height=3)
    btnMono.grid(row=3, column=1)
    btnColor.grid(row=3, column=3)
    
    start_new_thread(recv_data, (client_socket,))
    print ('>> Connect Server')
    

InitTime() 
    
root.mainloop()