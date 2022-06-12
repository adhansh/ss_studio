
from tkinter import *
import tkinter.messagebox

import os
import time
import shutil
#from threading import Thread

rootPath = 'C:\\ss_studio\\'
nasPath = 'Z:\\studio_bak\\'
lastDestPath = 'c:\\'

#SS_STUDIO_2022_01_30_0175 파일명
root = Tk()

root.title("Photo_Mover")
root.geometry("760x100")
root.resizable(False, False)

label_tag = Label(root, text='TAG :', font=('Helvetica', 20))
label_tag.grid(row=1, column=1)
#label_tag.place(x = 0, y = 0)

entry_prefix = Entry(root, width=15, font=('Helvetica', 20))
entry_prefix.grid(row=1, column=2)
#entry_prefix.place(x = 0, y = 0)

def CreateFolder(dir):
    print(dir)
    
    try:
        if not os.path.exists(dir):
            os.makedirs(dir)
    except OSError:
        print('Error : Can not create Folder :' + dir)
    
def MoveFileRAW():
    global lastDestPath
    
    targetFolder = entry_prefix.get() + time.strftime("%m%d_%H%M%S")
    print('target folder : ' + targetFolder)
    
    #22_01_30 폴더명
    srcPath = rootPath + time.strftime("%y_%m_%d")
    print('srcpath : ' + srcPath)
    
    destPath = rootPath +'select\\' + targetFolder
    print('destpath : '+ destPath)
    
    backupPath = nasPath + targetFolder
    print('backup path : '+ backupPath)
    
    #폴더생성
    CreateFolder(destPath)
    CreateFolder(backupPath)
    
    #파일 복사
    files = os.listdir(srcPath)
    
    for f in files:
        src = os.path.join(srcPath, f)
        src.upper()
        
        if (True == src.endswith('.JPG')):
            print('copy' + src +' to ' + destPath)
            shutil.copy2(src, destPath)
        
        print('move' + src +' to ' + backupPath)
        shutil.move(src, backupPath)   
        
    print('--------------------------------------------------\n')
    print('     FINISH!!! Move Photos!!\n')
    print('##################################################\n')
    
    lastDestPath = destPath    
        
def MoveFile():
    global lastDestPath
    
    targetFolder = entry_prefix.get() + time.strftime("%m%d_%H%M%S")
    print('target folder : ' + targetFolder)
    
    #22_01_30 폴더명
    srcPath = rootPath + time.strftime("%y_%m_%d")
    print('srcpath : ' + srcPath)
    
    destPath = rootPath +'select\\' + targetFolder
    print('destpath : '+ destPath)
    
    backupPath = nasPath + targetFolder
    print('backup path : '+ backupPath)
    
    #폴더생성
    CreateFolder(destPath)
    CreateFolder(backupPath)
    
    #파일 복사
    files = os.listdir(srcPath)
    
    for f in files:
        src = os.path.join(srcPath, f)
        src.upper()
        
        if (True == src.endswith('.JPG')):
            print('copy' + src +' to ' + destPath)
            shutil.copy2(src, destPath)        
            print('move' + src +' to ' + backupPath)
            shutil.move(src, backupPath)   
        
    print('--------------------------------------------------\n')
    print('     FINISH!!! Move Photos!!\n')
    print('##################################################\n')
    
    lastDestPath = destPath    
        
def MoveFile_stdalone():
    global lastDestPath
    
    targetFolder = entry_prefix.get() + time.strftime("%m%d_%H%M%S")
    print('target folder : ' + targetFolder)
    
    #22_01_30 폴더명
    srcPath = rootPath + time.strftime("%y_%m_%d")
    print('srcpath : ' + srcPath)
    
    destPath = rootPath +'select\\' + targetFolder
    print('destpath : '+ destPath)
    
    backupPath = nasPath + targetFolder
    print('backup path : '+ backupPath)
    
    #폴더생성
    CreateFolder(destPath)
    CreateFolder(backupPath)
    
    #파일 복사
    files = os.listdir(srcPath)
    
    for f in files:
        src = os.path.join(srcPath, f)
        src.upper()
        
        if (True == src.endswith('.JPG')):
            print('copy' + src +' to ' + destPath)
            shutil.copy2(src, destPath)
        
        print('move' + src +' to ' + backupPath)
        shutil.move(src, backupPath)   
        
    print('--------------------------------------------------\n')
    print('     FINISH!!! Move Photos!!\n')
    print('##################################################\n')
    
    lastDestPath = destPath    
    
def ClearPics():
    # 삭제확인 메시지박스
    retMsg = tkinter.messagebox.askyesno('Clear Photos', '촬영된 사진이 모두 제거됩니다. \n계속 하시겠습니까?')

    if retMsg == True:
        #22_01_30 폴더명
        srcPath = rootPath + time.strftime("%y_%m_%d")
        print('srcpath : ' + srcPath)
        
        if os.path.exists(srcPath):
            print('Remove All Files\n')
            for file in os.scandir(srcPath):
                os.remove(file.path)
                print(' - remove : '+file.path)
        else:
            print('Dir is not Found\n')
        print('--------------------------------------------------\n')
        print('     FINISH!!! Clear Photos!!\n')
        print('##################################################\n')
    
def RunBridge():
    # 저장 확인 메시지 박스
    retMsg = tkinter.messagebox.askyesno('Run Bridge!', '반드시 [촬영 사진 저장]을 먼저 수행해야 합니다. \n촬영사진 저장을 했습니까?')
    
    if retMsg == True:
        cmd = '\"C:\\Program Files\\Adobe\\Adobe Bridge 2020\\Bridge.exe\" ' + lastDestPath
        os.system(cmd)
    
    
    
btn_eos = Button(root, padx = 2, pady = 2, text = '촬영 사진 저장', font=('Helvetica', 20),  width=10, background='cyan', command = MoveFile)
btn_eos.grid(row=2, column=1)
#btn_eos.place(x = 0, y = 0)

btn_select = Button(root, padx = 2, pady = 2, text = '사진셀렉', font=('Helvetica', 20), width=14, background='yellow', command = RunBridge)
btn_select.grid(row=2, column=2)

btn_back = Button(root, padx = 2, pady = 2, text = '사진삭제', font=('Helvetica', 20), width=10, background='red', command = ClearPics)
btn_back.grid(row=2, column=3)

btn_raw = Button(root, padx = 2, pady = 2, text = 'RAW원본 저장', font=('Helvetica', 20), width=10, background='cyan', command = MoveFileRAW)
btn_raw.grid(row=2, column=4)
#btn_back.place(x = 0, y = 0)

root.mainloop()