
from enum import IntEnum
from xml.dom.pulldom import START_DOCUMENT

from pyautogui import PAUSE

# 카메라 조작 관련 enum

class PicStyle(IntEnum):
    "Picture style enumerate"
    COLOR = 1
    MONO = 2
    
class CmdRes(IntEnum):
    "return value of result"
    SUCCESS = 1
    FAIL = 2
    TIMEOUT = 3
    


class TabletCmds(IntEnum):
    "CMDs"
    COLOR_USER = 1
    MONO_USER = 2
    START = 3
    PAUSE = 4
    RESET = 5
    TIME = 6
    COLOR = 7
    MONO = 8
    SETTIME = 9
    

class CamExp(IntEnum):
    "Camera Exposure"
    EXP_30 = 1
    EXP_25 = 2
    EXP_20 = 3
    EXP_15 = 4
    EXP_13 = 5
    EXP_10 = 6
    EXP_8 = 6
    EXP_6 = 7
    EXP_5 = 8
    EXP_4 = 9
    EXP_3 = 10
    EXP_2DOT5 = 11
    EXP_2 = 12
    EXP_1DOT6 = 13
    EXP_1DOT3 = 14
    EXP_1 = 15
    EXP_0DOT8 = 16
    EXP_0DOT6 = 17
    EXP_0DOT5 = 18
    EXP_0DOT4 = 19
    EXP_0DOT3 = 20
    EXP_1DIV4 = 21
    EXP_1DIV5 = 22
    EXP_1DIV6 = 23
    EXP_1DIV8 = 24
    EXP_1DIV10 = 25
    EXP_1DIV13 = 26
    EXP_1DIV15 = 27
    EXP_1DIV20 = 28
    EXP_1DIV25 = 29
    EXP_1DIV30 = 30
    EXP_1DIV40 = 31
    EXP_1DIV50 = 32
    EXP_1DIV60 = 33
    EXP_1DIV80 = 34
    EXP_1DIV100 = 35
    EXP_1DIV125 = 36
    EXP_1DIV160 = 37
    EXP_1DIV200 = 38
    EXP_1DIV250 = 39
    
class CamSSpeed(IntEnum):
    "Camera shutter speed"
    F28 = 1
    F32 = 2
    F35 = 3
    F40 = 4
    F45 = 5
    F50 = 6
    F56 = 7
    F63 = 8
    F71 = 9
    F80 = 10
    F90 = 11
    
    