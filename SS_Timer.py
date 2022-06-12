from tkinter import *
import os
import time
import datetime

timelimit = 15#분단위
rootPath = 'C:\\ss_studio\\'

#SS_STUDIO_2022_01_30_0175 파일명
root = Tk()

root.title("SS TIMER. [ Enjoy this time:) ]")
root.attributes('-fullscreen', True)
root.resizable(False, False)

lebel_time = Label(root, text="", font=('Helvetica', 200), fg='gray')
lebel_time.pack()
#label_tag.place(x = 0, y = 0)

btn_quit = Button(root, text='Quit', command = root.quit)
btn_quit.pack()

now =  datetime.datetime.now()
timeset = now + datetime.timedelta(minutes = time)
print('timeset = ' + time)

def UpdateTimer():
    now = time.strftime("%H:%M:%S")
    lebel_time.configure(text=now)
    root.after(1000, UpdateTimer)
    
UpdateTimer()
root.mainloop()



