import sqlite3
from commonnames import *


def make():


    NAME = bo_TA

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
                                 KEY_1:           ['KEY_1', 'b p\nㄅ !', 'ㄅ', '!', 'b', 'p'],
                                 KEY_2:           ['KEY_2', 'd t\nㄉ @', "ㄉ", '"', 'd', 't'],
                                KEY_3:            ['KEY_3', 'ˇ #', 'ˇ', '#', '', ''],
                                KEY_4:            ['KEY_4', 'ˋ $', 'ˋ', '$', '', ''],
                                KEY_5:            ['KEY_5', 'zh ʈʂ\nㄓ %', 'ㄓ', '%', 'zh', 'ʈʂ'],
                                KEY_6:            ['KEY_6', 'ˊ ^','ˊ', '^','', ''],
                                KEY_7:            ['KEY_7', "˙ &&", '˙', "&", '', ''],
                                KEY_8:            ['KEY_8', 'a a\nㄚ *', 'ㄚ', '*', 'a', 'a'],
                                KEY_9:            ['KEY_9', 'ㄞ (', 'ㄞ', '(', '', ''],
                                KEY_0:            ['KEY_0', 'an an\nㄢ  ', 'ㄢ', '',  'an', 'an'],
                                KEY_MINUS:        ['KEY_MINUS', "- _", "-", "_", '' , '' ],
                                KEY_ASCIICIRCUM:       ['KEY_ASCIICIRCUMFLEX',"= +", "=", "+", '', ''],
                                KEY_BAR   :       ['KEY_BAR', "` ~", "`", "~", '', ''],
                                KEY_Q     :       ['KEY_Q', "p pʰ\nㄆ Q", "ㄆ", "Q", 'p', 'pʰ'],
                                KEY_W     :       ['KEY_W', "t tʰ\nㄊ W", "ㄊ", "W", 't', 'tʰ'],
                                KEY_E     :       ['KEY_E', "g k\nㄍ E", "ㄍ", "E", 'g', 'k'],
                                KEY_R     :       ['KEY_R', "j ʨ\n R", "ㄐ", "R", 'j', 'ʨ'],
                                KEY_T     :       ['KEY_T', "ch ʈʂʰ\nㄔ T", "ㄔ", "T", 'ch', 'ʈʂʰ'],
                                KEY_Y     :       ['KEY_Y', "z  ts\nㄗ Y", "ㄗ", "Y", 'z', 'ts'],
                                KEY_U     :       ['KEY_U', "i  y\nㄧ U", "ㄧ",  "U", 'i', 'y'],
                                KEY_I     :       ['KEY_I', "o o\nㄛ I", "ㄛ", "I", 'o', 'o'],
                                KEY_O     :       ['KEY_O', "ei ei\nㄟ O", "ㄟ", "O", 'ei', 'ei'],
                                KEY_P     :       ['KEY_P', "en ən\nㄣ P", "ㄣ", "P", 'en', 'ən'],
                                KEY_AT    :       ['KEY_AT', "[ {","{", "]", '',''],
                                KEY_BRACKETLEFT    :       ['KEY_LEFTBRACKET', "] }", "]", "}",'',''],
                                KEY_A     :       ['KEY_A', "m m\nㄇ A", "ㄇ", "A", 'm', 'm'],
                                KEY_S     :       ['KEY_S', "n n\nㄋ  S", "ㄋ", "S", 'n', 'n'],
                                KEY_D     :       ['KEY_D', "k kʰ\nㄎ  D", "ㄎ", "D", 'k', 'kʰ'],
                                KEY_F     :       ['KEY_F', "q ʨʰ\nㄑ  F", "ㄑ", "F", 'q', 'ʨʰ'],
                                KEY_G     :       ['KEY_G', "sh ʂ\nㄕ  G", "ㄕ", "G", 'sh', 'ʂ'],
                                KEY_H     :       ['KEY_H', "c  tsʰ\nㄘ  H", "ㄘ", "H", 'c', 'tsʰ'],
                                KEY_J     :       ['KEY_J',         "u w\nㄨ J", "ㄨ", "J", 'u', 'w'],
                                KEY_K     :       ['KEY_K',         "e ɤ\nㄜ K", "ㄜ", "K", 'e', 'ɤ'],
                                KEY_L     :       ['KEY_L',         "ao au\nㄠ L", "ㄠ", "L", 'ao', 'au'],
                                KEY_SEMICOLON:    ['KEY_SEMICOLON', "ang ang\nㄤ :", "ㄤ", ":", 'ang', 'ang'],
                                KEY_COLON:        ['KEY_COLON',     " *", ":", "*", '', ''],
                                KEY_BRACKETRIGHT   :        ['KEY_BRACKETRIGHT',        "\\ |", "\\", "|", '', ''],
                                KEY_Z    :        ['KEY_Z',         "f f\nㄈ  Z", "ㄈ", "Z", 'f',  'f'],
                                KEY_X    :        ['KEY_X',         "l l\nㄌ  X", "ㄌ", "X", 'l',  'l'],
                                KEY_C    :        ['KEY_C',         "h x\nㄏ  C", "ㄏ", "C", 'h',  'x'],
                                KEY_B    :        ['KEY_B',         "r ɻ\nㄖ  B", "ㄖ", "B", 'r',  'ɻ'],
                                KEY_V    :        ['KEY_V',         "x ɕ\nㄒ  V", "ㄒ", "V", 'ㄒ',  'V'],
                                KEY_N    :        ['KEY_N',         "s s\nㄙ  N", "ㄙ", "N", 's',  's'],
                                KEY_M    :        ['KEY_M',         'ü ü\nㄩ  M', 'ㄩ', 'M', 'ü',  'ü'],
                                KEY_COMMA:        ['KEY_COMMA',"ê e\nㄝ   <", "ㄝ", "<",'ê', 'e'],
                                KEY_PERIOD  :        ['KEY_PERIOD',"ou ou\nㄡ     >", "ㄡ", ">", 'ou', 'ou'],
                                KEY_SLASH:        ['KEY_SLASH',     "eng əŋ\nㄥ ?", "ㄥ", "?", 'eng', 'əŋ'],
                                KEY_BACKSLASH:    ['KEY_BACKSLASH', "` ~", "`", "~", '', ''],
                                KEY_SPACE:        ['KEY_SPACE',     "SPACE", "ˉ", "", "", ""]}}
     
    
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
