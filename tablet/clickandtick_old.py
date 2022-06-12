from glob import glob
from tkinter import *
import tkinter.ttk

import threading

arrTimeSetStr = [
                "15 min",
                "20 min",
                "30 min",
                "45 min",
                "60 min",
                "1 min"]

arrTimeSetVal = [15, 20, 30, 45, 60, 1]

nMin = 0
nSec = 0
bStop = True
strTime = '00:{0:02d}:{1:02d}'.format(nMin, nSec)


def Beep():
    print('RRrrrRrRrrRrrRrRrrr')
    
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
    
def Pause():
    global bStop
    
    bStop = True
    
def Reset():
    global bStop
    
    bStop = True
    InitTime()
    
def ComboSelected(event):
    global bStop
    global nSec
    
    if (bStop == True) and (nSec == 0):
        InitTime()
    
    
if __name__=='__main__':
    root = Tk()

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
    

    btnStart = Button(frame_bot, text = 'start', font=('Helvetica', 20), background='DarkSeaGreen1', command = Start, width=20, height=3)
    #btnStart.pack()
    btnPause = Button(frame_bot, text = 'pause', font=('Helvetica', 20), background='coral', command = Pause, width=20, height=3)
    #btnPause.pack()
    btnReset = Button(frame_bot, text = 'reset', font=('Helvetica', 20), background='pink', command = Reset, width=20, height=3)
    #btnReset.pack()
    btn_quit = Button(frame_bot, text='Quit', background='white', font=('Helvetica', 20), command = root.quit, width=20, height=1)
    #btn_quit.pack()

    cmbTime.grid(row=1, column=3)

    btnStart.grid(row=2, column=1)
    btnPause.grid(row=2, column=2)
    btnReset.grid(row=2, column=3)

    btn_quit.grid(row=3, column=2)

    InitTime() 
        
    root.mainloop()