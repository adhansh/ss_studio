
import config
import configparser
import os
import os.path

CONFIG_FILENAME = 'ssconfig.ini'

def DefaultConfig():
    currDir = os.getcwd()
    iniFile = currDir + '\\' + CONFIG_FILENAME
    
    saveCfg = configparser.ConfigParser()

    saveCfg['TITLE STRING']
        
    saveCfg['PREFIX_CAM_TITLE'] = 'EOS'
    saveCfg['PREFIX_PIC_STYLE_TITLE'] = '픽쳐 스타일'
    
    
    saveCfg['POS_PS_MENU']= {}
    saveCfg['POS_PS_MENU']['x'] = '194'
    saveCfg['POS_PS_MENU']['y'] = '366'
    
    saveCfg['POS_PS_MENU_MONO']= {}
    saveCfg['POS_PS_MENU_MONO']['x'] = '194'
    saveCfg['POS_PS_MENU_MONO']['y'] = '366'
    
    saveCfg['POS_PS_MENU_COLOR']= {}
    saveCfg['POS_PS_MENU_COLOR']['x'] = '194'
    saveCfg['POS_PS_MENU_COLOR']['y'] = '366'
    
    
    with open(iniFile, 'w') as configfile:
        saveCfg.write(configfile)

def LoadConfig():
    
    currDir = os.getcwd()
    iniFile = currDir + '\\' + CONFIG_FILENAME
        
    if os.path.isfile(iniFile) :
        laodCfg = configparser.ConfigParser()
        laodCfg.read(iniFile)
        
        config.POS_PS_MENU
        config.POS_PS_MENU_COLOR
        config.POS_PS_MENU_MONO
    else:
        print('no ini file, set default')
    
def SetValue():
    pass

def GetValue():
    pass
    
    
    
    
if __name__=='__main__':
    #LoadConfig()
    DefaultConfig()

    
    
    