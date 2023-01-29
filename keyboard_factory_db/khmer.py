import sqlite3
from commonnames import *

def make():

    NAME = km_KH
     
    key_dic = {NAME:
                       {0:
                           {KEY_F1: ['KEY_F1', '', '', '', '', ''],
                            KEY_F2: ['KEY_F2', '', '', '', '', ''],
                            KEY_F3: ['KEY_F3', '', '', '', '', ''],
                            KEY_F4: ['KEY_F4', '', '', '', '', ''],
                            KEY_F5:               ['KEY_F5', '', '', '', '', ''],
                            KEY_F6:               ['KEY_F6', '', '', '', '', ''],
                            KEY_F7:               ['KEY_F7', '', '', '', '', ''],
                            KEY_F8:               ['KEY_F8', '', '', '', '', ''],
                            KEY_F9:               ['KEY_F9', '', '', '', '', ''],
                            KEY_F10:              ['KEY_F10', '', '', '', '', ''],
                            KEY_F11:              ['KEY_F11', '', '', '', '', ''],
                            KEY_F12:              ['KEY_F12', '', '', '', '', ''],
                            KEY_1:            ['KEY_1', "១ !","១","!", '', ''],
                            KEY_2:            ['KEY_2', '២ ៗ',"២",'ៗ', '', ''],
                            KEY_3:            ['KEY_3', '៣ ៊',"៣","៊", '', ''],
                            KEY_4:            ['KEY_4', "៤ ៛","៤","៛", '', ''],
                            KEY_5:            ['KEY_5', "៥ ័","៥","័", '', ''],
                            KEY_6:            ['KEY_6', "៦ ៌","៦","៌",'', ''],
                            KEY_7:            ['KEY_7', "៧ ៍","៧","៍", '', ''],
                            KEY_8:            ['KEY_8', "៨ ៏","៨","៏", '', ''],
                            KEY_9:            ['KEY_9', "៩ ៎","៩","៎", '', ''],
                            KEY_0:            ['KEY_0', "០ ៑","០","៑",  '', ''],
                            KEY_MINUS:        ['KEY_MINUS', "- _","-","_", '' , '' ],
                            KEY_ASCIICIRCUM:       ['KEY_ASCIICIRCUM',"= +","=","+", '', ''],
                            KEY_BAR   :       ['KEY_BAR', "‌‌","","", '',    ''],
                            KEY_Q     :       ['KEY_Q', "ឆ ឈ","ឆ","ឈ", '', ''],
                            KEY_W     :       ['KEY_W', "ឹ ឺ","ឹ","ឺ", '', ''],
                            KEY_E     :       ['KEY_E', "េ ែ","េ","ែ", '', ''],
                            KEY_R     :       ['KEY_R', "រ ឬ","រ","ឬ", '', ''],
                            KEY_T     :       ['KEY_T', "ត ទ","ត","ទ", '', ''],
                            KEY_Y     :       ['KEY_Y', "យ ួ","យ","ួ",  '', ''],
                            KEY_U     :       ['KEY_U', "ុ ូ","ុ","ូ", '', ''],
                            KEY_I     :       ['KEY_I', "ិ ី","ិ","ី", '', ''],
                            KEY_O     :       ['KEY_O', "ោ ៅ","ោ","ៅ", '', ''],
                            KEY_P     :       ['KEY_P', "ផ ភ","ផ","ភ", '', ''],
                            KEY_AT    :       ['KEY_AT', "ើ ោះ","ើ","ោះ", '',''],
                            KEY_BRACKETLEFT    :       ['KEY_BRACKETLEFT', "ឿ ៀ","ឿ","ៀ",'',''],
                            KEY_A     :       ['KEY_A', "ា ៃ","ា","ៃ", '', ''],
                            KEY_S     :       ['KEY_S', "ស ាំ","ស","ាំ", '', ''],
                            KEY_D     :       ['KEY_D', "ដ ឌ","ដ","ឌ", '', ''],
                            KEY_F     :       ['KEY_F', "ថ ធ","ថ","ធ", '', ''],
                            KEY_G     :       ['KEY_G', "ង ុះ","ង","ុះ", '', ''],
                            KEY_H     :       ['KEY_H', "ហ ះ","ហ","ះ", '', ''],
                            KEY_J     :       ['KEY_J',         "ញ្ ុំ","ញ","ុំ", '', ''],
                            KEY_K     :       ['KEY_K',         "ក គ","ក","គ",'', ''],
                            KEY_L     :       ['KEY_L',         "ល ឡ","ល","ឡ",'', ''],
                            KEY_SEMICOLON:    ['KEY_SEMICOLON', "ៈ ៖","ៈ","៖", '', ''],
                            KEY_COLON:        ['KEY_COLON',     "់ ៉","់",'៉', '', ''],
                            KEY_BRACKETRIGHT   :        ['KEY_BRACKETRIGHT',        "\\ /","\\","/", '', ''],
                            KEY_Z    :        ['KEY_Z',         "ឋ ឍ","ឋ","ឍ", '',  ''],
                            KEY_X    :        ['KEY_X',         "ខ ឃ","ខ","ឃ", '',  ''],
                            KEY_C    :        ['KEY_C',         "ច ជ","ច","ជ", '',  ''],
                            KEY_B    :        ['KEY_B',         "ប ព","ប","ព", '',  ''],
                            KEY_V    :        ['KEY_V',         "វ េះ","វ","េះ", '',  ''],
                            KEY_N    :        ['KEY_N',         "ន ណ","ន","ណ", '',  ''],
                            KEY_M    :        ['KEY_M',         "ម ំ","ម","ំ", '',  ''],
                            KEY_COMMA:        ['KEY_COMMA', "អ ,","អ",",",'', ''],
                            KEY_PERIOD  :        ['KEY_PERIOD', "។ .","។",".", '', ''],
                            KEY_SLASH:        ['KEY_SLASH',     "​​​?","​","?", '', ''],
                            KEY_BACKSLASH:    ['KEY_BACKSLASH', "‌‌","","", '', ''],
                            KEY_SPACE:        ['KEY_SPACE',     "្ ", "្", " ", "", ""]},
                       

                     1:
                            {KEY_F1:               ['KEY_F1', 'KEY_F1', 'KEY_F1', 'KEY_F1', '', ''],
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
                            KEY_F12:              ['KEY_F12', 'KEY_F12', 'KEY_F12', 'KEY_F12', '', ''],
                            KEY_1:            ['KEY_1', "1 ᧡","1","᧡", '', ''],
                            KEY_2:            ['KEY_2', '2 ᧢',"2",'᧢', '', ''],
                            KEY_3:            ['KEY_3', '3 ᧣',"3","᧣", '', ''],
                            KEY_4:            ['KEY_4', "4 ᧤","4","᧤", '', ''],
                            KEY_5:            ['KEY_5', "5 ᧦","5","᧥", '', ''],
                            KEY_6:            ['KEY_6', "6 ᧦","6","᧦",'', ''],
                            KEY_7:            ['KEY_7', "7 ᧧","7","᧧", '', ''],
                            KEY_8:            ['KEY_8', "8 ᧨","8","᧨", '', ''],
                            KEY_9:            ['KEY_9', "9 ᧩","9","᧩", '', ''],
                            KEY_0:            ['KEY_0', "0 ᧪","0","᧪",  '', ''],
                            KEY_MINUS:        ['KEY_MINUS', "{  ᧫","{","᧫", '' , '' ],
                            KEY_ASCIICIRCUM:       ['KEY_ASCIICIRCUM',"} ᧬","}","᧬", '', ''],
                            KEY_BAR   :       ['KEY_BAR', "៙ ᧠","៙","᧠", '',    ''],
                            KEY_Q     :       ['KEY_Q', "* ᧭","*","᧭", '', ''],
                            KEY_W     :       ['KEY_W', "W ᧮","W","᧮", '', ''],
                            KEY_E     :       ['KEY_E', "ឯ ᧯","ឯ","᧯", '', ''],
                            KEY_R     :       ['KEY_R', "ឫ ៰","ឫ","៰", '', ''],
                            KEY_T     :       ['KEY_T', "ឦ ៱","ឦ","៱", '', ''],
                            KEY_Y     :       ['KEY_Y', "Y ៲","Y","៲", '', ''],
                            KEY_U     :       ['KEY_U', "ឧ ៳","ឧ","៳", '', ''],
                            KEY_I     :       ['KEY_I', "ឥ ៴","ឥ","៴", '', ''],
                            KEY_O     :       ['KEY_O', "ឱ ៵","ឱ","៵", '', ''],
                            KEY_P     :       ['KEY_P', "ឳ ៶","ឳ","៶", '', ''],
                            KEY_AT    :       ['KEY_AT', "[ ៷","[","៷", '',''],
                            KEY_BRACKETLEFT    :       ['KEY_BRACKETLEFT', "] ៸","]","៸",'',''],
                            KEY_A     :       ['KEY_A', "ឩ ᧰","ឩ","᧰", '', ''],
                            KEY_S     :       ['KEY_S', "ឪ ᧱","ឪ","᧱", '', ''],
                            KEY_D     :       ['KEY_D', "D ᧲","D","᧲", '', ''],
                            KEY_F     :       ['KEY_F', "F ᧳","F","᧳", '', ''],
                            KEY_G     :       ['KEY_G', "G ᧴","G","᧴", '', ''],
                            KEY_H     :       ['KEY_H', "H ᧵","H","᧵", '', ''],
                            KEY_J     :       ['KEY_J',         "ឮ ᧶","ឮ","᧶", '', ''],
                            KEY_K     :       ['KEY_K',         "ឭ ᧷","ឭ","᧷", '', ''],
                            KEY_L     :       ['KEY_L',         "ឰ ᧸","ឰ","᧸", '', ''],
                            KEY_SEMICOLON:    ['KEY_SEMICOLON', "; ᧹",";","᧹", '', ''],
                            KEY_COLON:        ['KEY_COLON',     "៝ ᧺","៝",'᧺', '', ''],
                            KEY_BRACKETRIGHT   :        ['KEY_BRACKETRIGHT',        "៚ ៹","៚","៹", '', ''],
                            KEY_Z    :        ['KEY_Z',         "# ᧻","#","᧻", '',  ''],
                            KEY_X    :        ['KEY_X',         "@ ᧼","@","᧼", '',  ''],
                            KEY_C    :        ['KEY_C',         "& ᧽","&","᧽", '',  ''],
                            KEY_B    :        ['KEY_B',         "% ᧿","%","᧿", '',  ''],
                            KEY_V    :        ['KEY_V',         "$ ᧾","$","᧾", '',  ''],
                            KEY_N    :        ['KEY_N',         "( N","(","N", '',  ''],
                            KEY_M    :        ['KEY_M',         "m M","m","M", '',  ''],
                            KEY_COMMA:        ['KEY_COMMA',     "‹ អ","‹","អ",'', ''],
                            KEY_PERIOD  :        ['KEY_PERIOD',       "› ឝ","›","ឝ", '', ''],
                            KEY_SLASH:        ['KEY_SLASH',     "៕ ឞ","៕","ឞ", '', ''],
                            KEY_BACKSLASH:    ['KEY_BACKSLASH', "៙ ᧠","៙","᧠", '', ''],
                            KEY_SPACE:        ['KEY_SPACE',     "SPACE", " ", "", "", ""]}
                      }
                        
                    
                       

               }
    con = sqlite3.connect("keyboard_mapper.sqlite3")
    with con:
        cur = con.cursor()
        cur.execute(f"DROP TABLE IF EXISTS {NAME}")
        PAGE = 0
        cur.execute(f"CREATE TABLE  IF NOT EXISTS {NAME} (KEY_NAME TEXT, DISPLAY_TEXT TEXT, BEFORE_TEXT TEXT, AFTER_TEXT TEXT, UNDER_TEXT TEXT, UPPER_TEXT TEXT, PAGE INT)")
        values = key_dic[NAME][PAGE].values()
        for v in values:
            v.append(PAGE)
            cur.execute(f"INSERT INTO {NAME} VALUES(?, ?, ?, ?, ?, ?, ?)", v)
        PAGE = 1
        values = key_dic[NAME][PAGE].values()
        for v in values:
            v.append(PAGE)
            cur.execute(f"INSERT INTO {NAME} VALUES(?, ?, ?, ?, ?, ?, ?)", v)
    
def main():
    make()
if __name__ == "__main__":
    main()
