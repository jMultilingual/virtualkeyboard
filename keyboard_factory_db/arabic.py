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
                            KEY_BAR   :       ['KEY_BAR', "ذ     ّ","ذ","ّ", '',    ''],
                            KEY_Q     :       ['KEY_Q', "ض     َ","ض","َ", '', ''],
                            KEY_W     :       ['KEY_W', "ص     ً","ص","ً", '', ''],
                            KEY_E     :       ['KEY_E', "ث     ُ","ث","ُ", '', ''],
                            KEY_R     :       ['KEY_R', "ق     ٌ","ق","ٌ", '', ''],
                            KEY_T     :       ['KEY_T', "ف     لإ","ف","لإ", '', ''],
                            KEY_Y     :       ['KEY_Y', "غ     إ","غ","إ", '', ''],
                            KEY_U     :       ['KEY_U', "ع     ‘","ع","‘", '', ''],
                            KEY_I     :       ['KEY_I', "ه     ÷","ه","÷", '', ''],
                            KEY_O     :       ['KEY_O', "خ     ×","خ","×", '', ''],
                            KEY_P     :       ['KEY_P', "ح     ؛","ح","؛", '', ''],
                            KEY_AT    :       ['KEY_AT', "ج     <","ج","<", '',''],
                            KEY_BRACKETLEFT    :       ['KEY_BRACKETLEFT', "د     >","د",">",'',''],
                            KEY_A     :       ['KEY_A', "ش     ِ","ش","ِ", '', ''],
                            KEY_S     :       ['KEY_S', "س     ٍ","س","ٍ", '', ''],
                            KEY_D     :       ['KEY_D', "ي     ]","ي","]", '', ''],
                            KEY_F     :       ['KEY_F', "ب     [","ب","[", '', ''],
                            KEY_G     :       ['KEY_G', "ل     لأ","ل","لأ", '', ''],
                            KEY_H     :       ['KEY_H', "ا     أ","ا","أ", '', ''],
                            KEY_J     :       ['KEY_J',         "ت     ـ","ت","ـ", '', ''],
                            KEY_K     :       ['KEY_K',         "ن     ،","ن","،", '', ''],
                            KEY_L     :       ['KEY_L',         "م     /","م","/", '', ''],
                            KEY_SEMICOLON:    ['KEY_SEMICOLON', "ك     :","ك",":", '', ''],
                            KEY_COLON:        ['KEY_COLON',     'ط     "',"ط",'"', '', ''],
                            KEY_BRACKETRIGHT   :        ['KEY_BRACKETRIGHT',        "\\     |","\\","|", '', ''],
                            KEY_Z    :        ['KEY_Z',         "ئ     ~","ئ","~", '',  ''],
                            KEY_X    :        ['KEY_X',         "ء     ْ","ء","ْ", '',  ''],
                            KEY_C    :        ['KEY_C',         "ؤ     }","ؤ","}", '',  ''],
                            KEY_B    :        ['KEY_B',         "لا     لآ","لا","لآ", '',  ''],
                            KEY_V    :        ['KEY_V',         "ر     {","ر","{", '',  ''],
                            KEY_N    :        ['KEY_N',         "ى     آ","ى","آ", '',  ''],
                            KEY_M    :        ['KEY_M',         "ة     ’","ة","’", '',  ''],
                            KEY_COMMA:        ['KEY_COMMA',     "و     ,","و",",",'', ''],
                            KEY_PERIOD  :        ['KEY_PERIOD',       "ز     .","ز",".", '', ''],
                            KEY_SLASH:        ['KEY_SLASH',     "ظ     ؟","ظ","؟", '', ''],
                            KEY_BACKSLASH:    ['KEY_BACKSLASH', "ذ     ّ","ذ","ّ", '', ''],
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

