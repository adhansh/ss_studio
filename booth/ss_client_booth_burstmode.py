import socket
#from _thread import *
import threading
from time import sleep
from tkinter import *
import tkinter.ttk
#from pyparsing import alphas

from camera_switch import *



HOST = '192.168.0.13' #서버주소
PORT = 9999
BURST_TERM = 10          # 각 찍을때마다의 텀
BURST_SHOT_MAX = 100     # 총 버스트모드가 사진찍는 횟수

gStopBurst = False
gCountDown = 0
thread_Burst = None



# 서버로부터 메세지를 받는 메소드
# 스레드로 구동 시켜, 메세지를 보내는 코드와 별개로 작동하도록 처리
def recv_data(client_socket) :
    while True :
        data = client_socket.recv(1024)
        # 픽쳐스타일 변경 명령인지 검토한다
        recv_msg = str(data.decode())
        if 'cmd:' in recv_msg:
            print('detect cmd : ', recv_msg)
            sndData = ''
            if DoCmdJob(recv_msg):
                sndData = 'res:ok'
            else:
                sndData = 'res:fail'
            client_socket.send(sndData.encode())
            
        else:
            print("recive : ",repr(data.decode()))


def StartClient():
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    
    #start_new_thread(recv_data, (client_socket,))
    thread_recv = threading.Thread(target=recv_data, args=(client_socket,))
    thread_recv.start()
    
    print ('>> Connect Server')

    while True:
        message = input('')
        if message == 'quit':
            close_data = message
            break
        #client_socket.send(message.encode())       
    client_socket.close()
    

root = Tk()

root.title("burst shot")
# root.attributes('-fullscreen', True)
#root.resizable(False, False)

strNum = '\n\n\n\n'
    
labelTime = Label(root, text=strNum, font=('Helvetica', 200), fg='red', bg='#4a7a8c', anchor=CENTER)
labelTime.pack()
    
def StartTransperancyWnd():
    global gCountDown
    global labelTime
    global root
    
    #ui 실행
    #root = Tk()

    #root.title("burst shot")
    # root.attributes('-fullscreen', True)
    #root.resizable(False, False)
    
    #strNum = '\n\n\n\n'
        
    #labelTime = Label(root, text=strNum, font=('Helvetica', 200), fg='red', bg='#4a7a8c', anchor=CENTER)
    #labelTime.pack()

    root.config(bg='#4a7a8c')
    root.wm_attributes('-transparentcolor','#4a7a8c')
    
    root.geometry('800x600')
    root.mainloop()
    
def BurstShot():
    print('>> burst shot start!!')
    
    
def updateCountDown():
    global gCountDown
    global labelTime
    
    strNum = ''
    count = (BURST_TERM - (gCountDown+1))
    if (0 == count):
        strNum = '\n\n\n\n shot!!'
    elif ( 5 >= count):
        strNum = '\n\n\n\n' + str(count)
    else:
        strNum = '\n\n\n\n'
        
    #labelTime.config(fg="grey30")    
    #strTime = '00:{0:02d}:{1:02d}'.format(nMin, nSec)
    labelTime.config(text=strNum)

    
def BurstShotThreadFunc(context):
    global gStopBurst
    global gCountDown
    
    loopCnt = BURST_TERM * BURST_SHOT_MAX
        
    while (0 < loopCnt):
        
        if ( True == gStopBurst ):
            break
        
        updateCountDown()
        
        if (BURST_TERM == (gCountDown+1)):
            TakePic()
        
        gCountDown += 1
        gCountDown %= BURST_TERM
        
        loopCnt -= 1
        sleep(1)  
        
def InitBurstMode():
    global thread_Burst
    thread_Burst = threading.Thread(target=BurstShotThreadFunc, args=(0,))
    thread_Burst.start()
    
    StartTransperancyWnd()
    
def StartBurstMode():
    global thread_Burst
    gStopBurst = False
    
    while True:
        if not thread_Burst.is_alive():
            break;
        print('Wait for Terminate burst thread\n')
        sleep(1)
        
    thread_Burst.run()
        
def StopBurstMode():     
    gStopBurst = True
    labelTime.config(text='')

def Test(val):
    for i in range(1, 6):
        print('test thread')
        sleep(1)
    print('end thread')
    
if __name__=='__main__':
    #StartClient()
    InitBurstMode()    