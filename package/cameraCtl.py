from abc import *
from cgitb import reset
from email.mime import audio
import pyautogui
import pygetwindow

import enums


PREFIX_CAM_TITLE = 'EOS'
#PREFIX_CAM_TITLE = '제목 없음'
PREFIX_PIC_STYLE_TITLE = '픽쳐 스타일'




class SSCamera(metaclass=ABCMeta):
    "ss studio camera interface!"
    
    cmd=0
    res=True    
    def __init__(self) -> None:
        print('Call super init')
        cmd=0
        res=True  
    
    #abstractmethod
    def Do(self, cmd):
        pass
    def Stop(self):
        pass
    def Return(self):
        return self.res
    #def ActiveWindow(self, win):
    #    if win.isActive == False:
    #        try:
    #            win.activate()
    #        except:
    #            win.minimize()
    #            win.restore()
    #            #win.maximize()  
    def ActivateWindow(self, title):
        win = pyautogui.getWindowsWithTitle(title)
            
        if win:
            win = pyautogui.getWindowsWithTitle(title)[0]
            if win.isActive == False:
                try:
                    win.activate()
                except:
                    win.minimize()
                    win.restore()
                    #win.maximize()  
        else:
            return None
        
        return win               
    
class SSSwitchStyle(SSCamera):
    """Switch picture syle"""    
    
    def SetShutterSpeed(self, speed):
        KEY_INTERVAL = 0.5
        POS_SHUTSPEED_MENU = (194, 366)
               
        win = super().ActivateWindow(PREFIX_CAM_TITLE) 
        if win is not None:   
            try:         
                # 셔속 더블 클릭해야됨
                pyautogui.doubleClick(win.left + POS_SHUTSPEED_MENU[0], win.top + POS_SHUTSPEED_MENU[1])
                
                 # 초기 스피드 F2.8
                pyautogui.press(pyautogui.KEYBOARD_KEYS.up, interval=KEY_INTERVAL)
                #iSpeed = enums.CamSSpeed.F28
                
                for iSpeed in enums.CamSSpeed:
                    if iSpeed == speed:
                        break
                    pyautogui.press(pyautogui.KEYBOARD_KEYS.right, interval=KEY_INTERVAL)
            except:
                return False
                
        else:
            return False
        
        return True
        
    def SetExposure(self, exp):
        KEY_INTERVAL = 0.5
        POS_EXP_MENU = (194, 366)
               
        win = super().ActivateWindow(PREFIX_CAM_TITLE) 
        if win is not None:   
            try:         
                # 노출 더블 클릭해야됨
                pyautogui.doubleClick(win.left + POS_EXP_MENU[0], win.top + POS_EXP_MENU[1])
                
                 # 초기 노출 30"
                pyautogui.press(pyautogui.KEYBOARD_KEYS.up, interval=KEY_INTERVAL)
                #iExp = enums.CamExp.EXP_30
                
                for iExp in enums.CamExp:
                    if iExp == exp:
                        break
                    pyautogui.press(pyautogui.KEYBOARD_KEYS.right, interval=KEY_INTERVAL)
            except:
                return False
                
        else:
            return False

        return True              
        
        
    
    def SetPicStyle(self, style):
        POS_PS_MENU = (194, 366)
        POS_PS_MENU_MONO = (194, 366)
        POS_PS_MENU_COLOR = (194, 409)
                
        bRet = True

        win = super().ActivateWindow(PREFIX_CAM_TITLE) 
        if win is not None:   
            try:         
                # 픽쳐스타일 메뉴 클릭
                pyautogui.click(win.left + POS_PS_MENU[0], win.top + POS_PS_MENU[1])
                
                if enums.PicStyle.MONO == style:
                    # 픽쳐스타일 메뉴중 흑백 클릭
                    pyautogui.click(win.left + POS_PS_MENU_MONO[0], win.top + POS_PS_MENU_MONO[1])
                elif enums.PicStyle.COLOR == style:
                    #픽쳐스타일 메뉴중 컬러 클릭
                    pyautogui.click(win.left + POS_PS_MENU_COLOR[0], win.top + POS_PS_MENU_COLOR[1])
                else:
                    print('not switch cmd')
            except:
                return False
                
        else:
            return False        
        
        # 잘못하다가 픽쳐스타일 윈도우가 열려서 막히는 경우를 방지
        subWin =  super().ActivateWindow(PREFIX_PIC_STYLE_TITLE)
        if subWin is not None: 
            #픽쳐스타일 윈도우 취소 클릭
            pyautogui.click(subWin.left + 332, subWin.top + 261)
            
        return bRet

    
    def Do(self, style):
        return self.SetPicStyle(style)
    
    def Stop(self):
        pass

class SSShooter(SSCamera):
    
    def TakePic(self):
        POS_TP_SHOT = (201, 77)
    
        bRet = True
        
        win = super().ActivateWindow(PREFIX_CAM_TITLE)        
        if win is not None:
            # 촬영버튼 클릭
            try:
                pyautogui.click(win.left + POS_TP_SHOT[0], win.top + POS_TP_SHOT[1])
            except:
                bRet = False
        else:
            bRet = False
        
        return bRet
    
    def Do(self):
        return self.TakePic()
        
    def Stop(self):
        pass
    def Return(self):
        return self.res
    
class SSBurstShot(SSShooter):
    def Do(self, cmd):
        pass
    def Stop(self):
        pass
    def Return(self):
        return self.res

def DoCmdJob(cmd):
    bRet = True
    
    switcher = SSSwitchStyle()
        
    if 'cmd:mono' == cmd:
        print('run cmd(mono)')
        switcher.Do(enums.PicStyle.MONO)
        
        
    elif 'cmd:color' == cmd:
        print('run cmd(color)')
        #SetColor()
        switcher.Do(enums.PicStyle.COLOR)
        
    return bRet

if __name__=='__main__':
    
    DoCmdJob('cmd:mono')
    
    
    
    
