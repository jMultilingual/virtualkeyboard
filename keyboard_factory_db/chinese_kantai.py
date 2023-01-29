import sqlite3
from commonnames import *
def make():


    NAME = zh_CN
    key_dic = {NAME:       {KEY_F1:              ['KEY_F1', '', '', '', '', ''],
                            KEY_F2:               ['KEY_F2', '', '', '', '', ''],
                            KEY_F3:               ['KEY_F3', '', '', '', '', ''],
                            KEY_F4:               ['KEY_F4', '', '', '', '', ''],
                            KEY_F5:               ['KEY_F5', '', '', '', '', ''],
                            KEY_F6:               ['KEY_F6', '', '', '', '', ''],
                            KEY_F7:               ['KEY_F7', '', '', '', '', ''],
                            KEY_F8:               ['KEY_F8', '', '', '', '', ''],
                            KEY_F9:               ['KEY_F9', '', '', '', '', ''],
                            KEY_F10:              ['KEY_F10', '', '', '', '', ''],
                            KEY_F11:              ['KEY_F11', '', '', '', '', ''],
                            KEY_F12:              ['KEY_F12', '', '', '', '', ''],
                            KEY_1:            ['KEY_1', '1 !', '1', '!', '', ''],
                            KEY_2:            ['KEY_2', '2 "', "2", '"', '', ''],
                            KEY_3:            ['KEY_3', '3 #', '3', '#', '', ''],
                            KEY_4:            ['KEY_4', '4 $', '4', '$', '', ''],
                            KEY_5:            ['KEY_5', '5 %', '5', '%', '', ''],
                            KEY_6:            ['KEY_6', '6 &&','6', '&&','', ''],
                            KEY_7:            ['KEY_7', "7 '", '7', "'", '', ''],
                            KEY_8:            ['KEY_8', '8 (', '8', '(', '', ''],
                            KEY_9:            ['KEY_9', '9 )', '9', ')', '', ''],
                            KEY_0:            ['KEY_0', '0  ', '0', '',  '', ''],
                            KEY_MINUS:        ['KEY_MINUS', "{0} =".format(" ̄"), "{0}".format(" ̄"), "=", '' , '' ],
                            KEY_ASCIICIRCUM:       ['KEY_ASCIICIRCUM',"{0} ~".format(" ̌"), "{0}".format(" ̌"), "~", '', ''],
                            KEY_BAR   :       ['KEY_BAR', "\\ |", "\\", "|", '',    ''],
                            KEY_Q     :       ['KEY_Q', "q ", "q", "", '', ''],
                            KEY_W     :       ['KEY_W', "w ", "w", "", '', ''],
                            KEY_E     :       ['KEY_E', "e ", "e", "", '', ''],
                            KEY_R     :       ['KEY_R', "r ", "r", "", '', ''],
                            KEY_T     :       ['KEY_T', "t ", "t", "", '', ''],
                            KEY_Y     :       ['KEY_Y', "y ", "y", "", '', ''],
                            KEY_U     :       ['KEY_U', "u ", "u", "", '', ''],
                            KEY_I     :       ['KEY_I', "i ", "i", "", '', ''],
                            KEY_O     :       ['KEY_O', "o ", "o", "", '', ''],
                            KEY_P     :       ['KEY_P', "p ", "p", "", '', ''],
                            KEY_AT    :       ['KEY_AT', "@ `\n{0} {1}".format(" ̀", " ́")," ̀", " ́", '@','`'],
                            KEY_BRACKETLEFT    :       ['KEY_BRACKETLEFT', "[ {", "[", "{",'',''],
                            KEY_A     :       ['KEY_A', "a ", "a", "", '', ''],
                            KEY_S     :       ['KEY_S', "s ", "s", "", '', ''],
                            KEY_D     :       ['KEY_D', "d ", "d", "", '', ''],
                            KEY_F     :       ['KEY_F', "f ", "f", "", '', ''],
                            KEY_G     :       ['KEY_G', "g ", "g", "", '', ''],
                            KEY_H     :       ['KEY_H', "h ", "h", "", '', ''],
                            KEY_J     :       ['KEY_J',         "j ", "j", "", '', ''],
                            KEY_K     :       ['KEY_K',         "k ", "k", "", '', ''],
                            KEY_L     :       ['KEY_L',         "l ", "l", "", '', ''],
                            KEY_SEMICOLON:    ['KEY_SEMICOLON', "; +", ";", "+", '', ''],
                            KEY_COLON:        ['KEY_COLON',     ": *", ":", "*", '', ''],
                            KEY_BRACKETRIGHT   :        ['KEY_BRACKETRIGHT',        "] }", "]", "}", '', ''],
                            KEY_Z    :        ['KEY_Z',         "z ", "z", "", '',  ''],
                            KEY_X    :        ['KEY_X',         "x ", "x", "", '',  ''],
                            KEY_C    :        ['KEY_C',         "c ", "c", "", '',  ''],
                            KEY_B    :        ['KEY_B',         "b ", "b", "", '',  ''],
                            KEY_V    :        ['KEY_V',         "ü ", "ü", "", '',  ''],
                            KEY_N    :        ['KEY_N',         "n ", "n", "", '',  ''],
                            KEY_M    :        ['KEY_M',         'm ', 'm', '', '',  ''],
                            KEY_COMMA:        ['KEY_COMMA',     ",   <", ",", "<",'', ''],
                            KEY_PERIOD  :        ['KEY_PERIOD',       ".     >", ".", ">", '', ''],
                            KEY_SLASH:        ['KEY_SLASH',     "/ ?", "/", "?", '', ''],
                            KEY_BACKSLASH:    ['KEY_BACKSLASH', "\\ _", "\\", "_", '', ''],
                            KEY_SPACE:        ['KEY_SPACE'      " ", " ", "", "", "", ""]}}
  
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
