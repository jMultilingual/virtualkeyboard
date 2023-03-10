import sqlite3

from commonnames import *

def make():
 
    NAME = ar_EG
    key_dic = {NAME:       {KEY_F1:               ['KEY_F1', 'KEY_F1', 'KEY_F1', 'KEY_F1', '', ''],
                            KEY_F2:               ['KEY_F2', 'KEY_F2', 'KEY_F2', 'KEY_F2', '', ''],
                            KEY_F3:               ['KEY_F3', 'KEY_F3', 'KEY_F3', 'KEY_F3', '', ''],
                            KEY_F4:               ['KEY_F4', 'KEY_F4', 'KEY_F4', 'KEY_F4', '', ''],
                            KEY_F5:               ['KEY_F5', 'KEY_F5', 'KEY_F5', 'KEY_F5', '', ''],
                            KEY_F6:               ['KEY_F6', 'KEY_F6', 'KEY_F6', 'KEY_F6', '', ''],
                            KEY_F7:               ['KEY_F7', 'KEY_F7', 'KEY_F7', 'KEY_F7', '', ''],
                            KEY_F8:               ['KEY_F8', 'KEY_F8', 'KEY_F8', 'KEY_F8', '', ''],
                            KEY_F9:               ['KEY_F9', 'KEY_F9', 'KEY_F9', 'KEY_F9', '', ''],
                            KEY_F10:              ['KEY_F10', 'KEY_F10', 'KEY_F10', 'KEY_F10', '', ''],
                            KEY_F11:              ['KEY_F11', 'KEY_F11', 'KEY_F11', 'KEY_F11', '', ''],
                            KEY_F12:              ['KEY_F12', '\\', '\\', 'KEY_F12', '', ''],
                            KEY_1:            ['KEY_1', "1 !", "1", "!", '', ''],
                            KEY_2:            ['KEY_2', '2 @', "2", '@', '', ''],
                            KEY_3:            ['KEY_3', '3 #', "3", "#", '', ''],
                            KEY_4:            ['KEY_4', "4 $", "4", "$", '', ''],
                            KEY_5:            ['KEY_5', "5 %", "5", "%", '', ''],
                            KEY_6:            ['KEY_6', "6 ^", "6", "^",'', ''],
                            KEY_7:            ['KEY_7', "7 &&","7", "&&", '', ''],
                            KEY_8:            ['KEY_8', "8 *", "8", "*", '', ''],
                            KEY_9:            ['KEY_9', "9 )", "9", ")", '', ''],
                            KEY_0:            ['KEY_0', "0 (", "0", "(",  '', ''],
                            KEY_MINUS:        ['KEY_MINUS', "-  _", "-", "_", '' , '' ],
                            KEY_ASCIICIRCUM:       ['KEY_ASCIICIRCUM',"=     +","=","+", '', ''],
                            KEY_BAR   :       ['KEY_BAR', "??     ??","??","??", '',    ''],
                            KEY_Q     :       ['KEY_Q', "??     ??","??","??", '', ''],
                            KEY_W     :       ['KEY_W', "??     ??","??","??", '', ''],
                            KEY_E     :       ['KEY_E', "??     ??","??","??", '', ''],
                            KEY_R     :       ['KEY_R', "??     ??","??","??", '', ''],
                            KEY_T     :       ['KEY_T', "??     ????","??","????", '', ''],
                            KEY_Y     :       ['KEY_Y', "??     ??","??","??", '', ''],
                            KEY_U     :       ['KEY_U', "??     ???","??","???", '', ''],
                            KEY_I     :       ['KEY_I', "??     ??","??","??", '', ''],
                            KEY_O     :       ['KEY_O', "??     ??","??","??", '', ''],
                            KEY_P     :       ['KEY_P', "??     ??","??","??", '', ''],
                            KEY_AT    :       ['KEY_AT', "??     <","??","<", '',''],
                            KEY_BRACKETLEFT    :       ['KEY_BRACKETLEFT', "??     >","??",">",'',''],
                            KEY_A     :       ['KEY_A', "??     ??","??","??", '', ''],
                            KEY_S     :       ['KEY_S', "??     ??","??","??", '', ''],
                            KEY_D     :       ['KEY_D', "??     ]","??","]", '', ''],
                            KEY_F     :       ['KEY_F', "??     [","??","[", '', ''],
                            KEY_G     :       ['KEY_G', "??     ????","??","????", '', ''],
                            KEY_H     :       ['KEY_H', "??     ??","??","??", '', ''],
                            KEY_J     :       ['KEY_J',         "??     ??","??","??", '', ''],
                            KEY_K     :       ['KEY_K',         "??     ??","??","??", '', ''],
                            KEY_L     :       ['KEY_L',         "??     /","??","/", '', ''],
                            KEY_SEMICOLON:    ['KEY_SEMICOLON', "??     :","??",":", '', ''],
                            KEY_COLON:        ['KEY_COLON',     '??     "',"??",'"', '', ''],
                            KEY_BRACKETRIGHT   :        ['KEY_BRACKETRIGHT',        "\\     |","\\","|", '', ''],
                            KEY_Z    :        ['KEY_Z',         "??     ~","??","~", '',  ''],
                            KEY_X    :        ['KEY_X',         "??     ??","??","??", '',  ''],
                            KEY_C    :        ['KEY_C',         "??     }","??","}", '',  ''],
                            KEY_B    :        ['KEY_B',         "????     ????","????","????", '',  ''],
                            KEY_V    :        ['KEY_V',         "??     {","??","{", '',  ''],
                            KEY_N    :        ['KEY_N',         "??     ??","??","??", '',  ''],
                            KEY_M    :        ['KEY_M',         "??     ???","??","???", '',  ''],
                            KEY_COMMA:        ['KEY_COMMA',     "??     ,","??",",",'', ''],
                            KEY_PERIOD  :        ['KEY_PERIOD',       "??     .","??",".", '', ''],
                            KEY_SLASH:        ['KEY_SLASH',     "??     ??","??","??", '', ''],
                            KEY_BACKSLASH:    ['KEY_BACKSLASH', "??     ??","??","??", '', ''],
                            KEY_SPACE:        ['KEY_SPACE',     "SPACE", " ", "", "", ""]}}


    con = sqlite3.connect("keyboard_mapper.sqlite3")
    with con:
        cur = con.cursor()
        cur.execute(f"DROP TABLE IF EXISTS {NAME}")
        PAGE = 0
        cur.execute(f"CREATE TABLE  IF NOT EXISTS {NAME} (KEY_NAME TEXT, DISPLAY_TEXT TEXT, BEFORE_TEXT TEXT, AFTER_TEXT TEXT, UNDER_TEXT TEXT, UPPER_TEXT TEXT, PAGE INT)")
        values = key_dic[NAME].values()
        for v in values:
            v.append(PAGE)
            cur.execute(f"INSERT INTO {NAME} VALUES(?, ?, ?, ?, ?, ?, ?)", v)

    
def main():
    make()
if __name__ == "__main__":
    main()

