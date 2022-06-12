import pyautogui

def SetPicStyle(style):
    POS_PS_MENU = (194, 366)
    POS_PS_MENU_MONO = (194, 366)
    POS_PS_MENU_COLOR = (194, 409)
    
    bRet = True
    
    try:
        win = pyautogui.getWindowsWithTitle('EOS')
        
        if win:
            win = pyautogui.getWindowsWithTitle('EOS')[0]
            win.activate()
        else:
            bRet= False
        
        # 픽쳐스타일 메뉴 클릭
        pyautogui.click(win.left + POS_PS_MENU[0], win.top + POS_PS_MENU[1])
        
        if ('mono' == style):
            # 픽쳐스타일 메뉴중 흑백 클릭
            pyautogui.click(win.left + POS_PS_MENU_MONO[0], win.top + POS_PS_MENU_MONO[1])
        elif('color' == style):
            #픽쳐스타일 메뉴중 컬러 클릭
            pyautogui.click(win.left + POS_PS_MENU_COLOR[0], win.top + POS_PS_MENU_COLOR[1])
        else:
            print('not switch cmd')
        
        # 잘못하다가 픽쳐스타일 윈도우가 열려서 막히는 경우를 방지
        subWin = pyautogui.getWindowsWithTitle('픽쳐 스타일')
        if subWin:
            subWin = pyautogui.getWindowsWithTitle('픽쳐 스타일')[0]
            #픽쳐스타일 윈도우 취소 클릭
            pyautogui.click(subWin.left + 332, subWin.top + 261)
            bRet = False
        
    except:
        return False
    else:
        return bRet
        
        
def DoCmdJob(cmd):
    bRet = True
    
    if 'cmd:mono' == cmd:
        print('run cmd(mono)')
        bRet = SetPicStyle('mono')
        
        
    elif 'cmd:color' == cmd:
        print('run cmd(color)')
        #SetColor()
        bRet = SetPicStyle('color')
        
    return bRet

if __name__=='__main__':
    while(True):
        picstyle = input('')
        SetPicStyle(picstyle)    
    
    
    
