import sqlite3
from commonnames import *


def make():


    NAME = en_GB

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
                                 KEY_1:           ['KEY_1', '1 !', '1', '!', '', ''],
                                 KEY_2:           ['KEY_2', '2 "', "2", '"', '', ''],
                                KEY_3:            ['KEY_3', '3 #', '3', '#', '', ''],
                                KEY_4:            ['KEY_4', '4 $', '4', '$', '', ''],
                                KEY_5:            ['KEY_5', '5 %', '5', '%', '', ''],
                                KEY_6:            ['KEY_6', '6 &&','6', '&&','', ''],
                                KEY_7:            ['KEY_7', "7 '", '7', "'", '', ''],
                                KEY_8:            ['KEY_8', '8 (', '8', '(', '', ''],
                                KEY_9:            ['KEY_9', '9 )', '9', ')', '', ''],
                                KEY_0:            ['KEY_0', '0  ', '0', '',  '', ''],
                                KEY_MINUS:        ['KEY_MINUS', "- =", "-", "=", '' , '' ],
                                KEY_ASCIICIRCUM:       ['KEY_ASCIICIRCUMFLEX',"^ ~", "^", "~", '', ''],
                                KEY_BAR   :       ['KEY_BAR', "\\ |", "\\", "|", '', ''],
                                KEY_Q     :       ['KEY_Q', "q Q", "q", "Q", '', ''],
                                KEY_W     :       ['KEY_W', "w W", "w", "W", '', ''],
                                KEY_E     :       ['KEY_E', "ə ɛ\ne E", "e", "E", 'ə', 'ɛ'],
                                KEY_R     :       ['KEY_R', "r R", "r", "R", '', ''],
                                KEY_T     :       ['KEY_T', "θ\n t T", "t", "T", 'θ', ''],
                                KEY_Y     :       ['KEY_Y', "y Y", "y", "Y", '', ''],
                                KEY_U     :       ['KEY_U', "ʊ\nu U", "u", "U", 'ʊ', ''],
                                KEY_I     :       ['KEY_I', "ɪ\ni I", "i", "I", 'ɪ', ''],
                                KEY_O     :       ['KEY_O', "ɑ ɔ\no O", "o", "O", 'ɑ', 'ɔ'],
                                KEY_P     :       ['KEY_P', "p P", "p", "P", '', ''],
                                KEY_AT    :       ['KEY_AT', "@ `","@", "`", '',''],
                                KEY_BRACKETLEFT    :       ['KEY_LEFTBRACKET', "[ {", "[", "{",'',''],
                                KEY_A     :       ['KEY_A', "æ ʌ\na A", "a", "A", 'æ', 'ʌ'],
                                KEY_S     :       ['KEY_S', "ʃ\ns S", "s", "S", 'ʃ', ''],
                                KEY_D     :       ['KEY_D', "ð\nd D", "d", "D", 'ð', ''],
                                KEY_F     :       ['KEY_F', "f F", "f", "F", '', ''],
                                KEY_G     :       ['KEY_G', "g G", "g", "G", '', ''],
                                KEY_H     :       ['KEY_H', "h H", "h", "H", '', ''],
                                KEY_J     :       ['KEY_J',         "j J", "j", "J", '', ''],
                                KEY_K     :       ['KEY_K',         "k K", "k", "K", '', ''],
                                KEY_L     :       ['KEY_L',         "l L", "l", "L", '', ''],
                                KEY_SEMICOLON:    ['KEY_SEMICOLON', "; +", ";", "+", '', ''],
                                KEY_COLON:        ['KEY_COLON',     ": *", ":", "*", '', ''],
                                KEY_BRACKETRIGHT   :        ['KEY_BRACKETRIGHT',        "] }", "]", "}", '', ''],
                                KEY_Z    :        ['KEY_Z',         "ʒ\nz Z", "z", "Z", 'ʒ',  ''],
                                KEY_X    :        ['KEY_X',         "x X", "x", "X", '',  ''],
                                KEY_C    :        ['KEY_C',         "c C", "c", "C", '',  ''],
                                KEY_B    :        ['KEY_B',         "b B", "b", "B", '',  ''],
                                KEY_V    :        ['KEY_V',         "v V", "v", "V", '',  ''],
                                KEY_N    :        ['KEY_N',         "ŋ\nn N", "n", "N", 'ŋ',  ''],
                                KEY_M    :        ['KEY_M',         'm M', 'm', 'M', '',  ''],
                                KEY_COMMA:        ['KEY_COMMA',",   <", ",", "<",'', ''],
                                KEY_PERIOD  :        ['KEY_PERIOD',".     >", ".", ">", '', ''],
                                KEY_SLASH:        ['KEY_SLASH',     "/ ?", "/", "?", '', ''],
                                KEY_BACKSLASH:    ['KEY_BACKSLASH', "\\ _", "\\", "_", '', ''],
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
