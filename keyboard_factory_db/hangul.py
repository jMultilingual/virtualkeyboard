import sqlite3
from commonnames import *
def make():
 
    NAME = ko_KR
    
    key_dic = {NAME:  {KEY_F1:               ['KEY_F1', 'KEY_F1', 'KEY_F1', 'KEY_F1', '', ''],
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
                            KEY_1:            ['KEY_1', '1 !', '1', '!', '', ''],
                            KEY_2:            ['KEY_2', '2 "', "2", '"', '', ''],
                            KEY_3:            ['KEY_3', '3 #', '3', '#', '', ''],
                            KEY_4:            ['KEY_4', '4 $', '4', '$', '', ''],
                            KEY_5:            ['KEY_5', '5 %', '5', '%', '', ''],
                            KEY_6:            ['KEY_6', '6 ^','6', '^','', ''],
                            KEY_7:            ['KEY_7', "7 &&", '7', "&&", '', ''],
                            KEY_8:            ['KEY_8', '8 *', '8', '*', '', ''],
                            KEY_9:            ['KEY_9', '9 (', '9', '(', '', ''],
                            KEY_0:            ['KEY_0', '0 )', '0', ')',  '', ''],
                            KEY_MINUS:        ['KEY_MINUS', "- _", "-", "_", '' , '' ],
                            KEY_ASCIICIRCUM:       ['KEY_ASCIICIRCUM',"^ ~", "^", "~", '', ''],
                            KEY_BAR   :       ['KEY_BAR', "`  ~","`","~", '',    ''],
                            KEY_Q     :       ['KEY_Q', "p b\n ㅂ  ㅃ", "ㅂ", "ㅃ", 'p', 'b'],
                            KEY_W     :       ['KEY_W', "t͡ɕ d͡ʑ\nㅈ  ㅉ","ㅈ","ㅉ", 't͡ɕ', 'd͡ʑ'],
                            KEY_E     :       ['KEY_E', "t t̚\nㄷ  ㄸ","ㄷ","ㄸ", 't', 't̚'],
                            KEY_R     :       ['KEY_R', "k k̚\nㄱ  ㄲ","ㄱ","ㄲ", 'k', 'k̚'],
                            KEY_T     :       ['KEY_T', "ㅅ  ㅆ","ㅅ","ㅆ", '', ''],
                            KEY_Y     :       ['KEY_Y', "ㅛ  ㅛ","ㅛ","ㅛ", '', ''],
                            KEY_U     :       ['KEY_U', "ㅕ  ㅕ","ㅕ","ㅕ", '', ''],
                            KEY_I     :       ['KEY_I', "ㅑ  ㅑ","ㅑ","ㅑ", '', ''],
                            KEY_O     :       ['KEY_O', "ɛ\nㅐ  ㅒ","ㅐ","ㅒ", 'ɛ', ''],
                            KEY_P     :       ['KEY_P', "ㅔ  ㅖ","ㅔ","ㅖ", '', ''],
                            KEY_AT    :       ['KEY_AT',"[  {","[","{", '',''],
                            KEY_BRACKETLEFT    :       ['KEY_BRACKETLEFT', "]  }","]","}",'',''],
                            KEY_A     :       ['KEY_A', "m \nㅁ  ㅁ","ㅁ","ㅁ", '', ''],
                            KEY_S     :       ['KEY_S', "s ɕ\nㄴ  ㄴ","ㄴ","ㄴ", 's', 'ɕ'],
                            KEY_D     :       ['KEY_D', "ŋ\nㅇ  ㅇ","ㅇ","ㅇ", '', 'ŋ'],
                            KEY_F     :       ['KEY_F', "l\nㄹ  ㄹ","ㄹ","ㄹ", 'l', ''],
                            KEY_G     :       ['KEY_G', "ɦ\nㅎ  ㅎ","ㅎ","ㅎ", 'ɦ', ''],
                            KEY_H     :       ['KEY_H', "o\nㅗ  ㅗ","ㅗ","ㅗ", 'o', ''],
                            KEY_J     :       ['KEY_J',         "ɔ\nㅓ  ㅓ","ㅓ","ㅓ", 'ɔ', ''],
                            KEY_K     :       ['KEY_K',         "a\nㅏ  ㅏ","ㅏ","ㅏ", 'a', ''],
                            KEY_L     :       ['KEY_L',         "i\nㅣ  ㅣ","ㅣ","ㅣ", 'i', ''],
                            KEY_SEMICOLON:    ['KEY_SEMICOLON', ";  :",";",":", '', ''],
                            KEY_COLON:        ['KEY_COLON',     "'  "'"',"'",'"', '', ''],
                            KEY_BRACKETRIGHT   :        ['KEY_BRACKETRIGHT',        "\\  |","\\","|", '', ''],
                            KEY_Z    :        ['KEY_Z',         "ㅋ  ㅋ","ㅋ","ㅋ", '',  ''],
                            KEY_X    :        ['KEY_X',         "t\nㅌ  ㅌ","ㅌ","ㅌ", 't',  ''],
                            KEY_C    :        ['KEY_C',         "t͡ɕʰ\nㅊ  ㅊ","ㅊ","ㅊ", 't͡ɕʰ',  ''],
                            KEY_V    :        ['KEY_V',         "pʰ p̚\nㅍ  ㅍ","ㅍ","ㅍ", 'pʰ',  'p̚'],
                            KEY_B    :        ['KEY_B',         "ㅠ  ㅠ","ㅠ","ㅠ", '',  ''],                            
                            KEY_N    :        ['KEY_N',         "u\nㅜ  ㅜ","ㅜ","ㅜ", 'u',  ''],
                            KEY_M    :        ['KEY_M',         "ɯ\nㅡ  ㅡ","ㅡ","ㅡ", 'ɯ',  ''],
                            KEY_COMMA:        ['KEY_COMMA',",   <", ",", "<",'', ''],
                            KEY_PERIOD  :        ['KEY_PERIOD',".  >",".",">", '', ''],
                            KEY_SLASH:        ['KEY_SLASH',     "/ ?", "/", "?", '', ''],
                            KEY_BACKSLASH:    ['KEY_BACKSLASH', "`  ~","`","~", '', ''],
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

