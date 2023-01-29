import sqlite3
from commonnames import *
def make():


    NAME = hi_EG
    
    import unicodedata
    import os, sys

    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))    
    sys.path.append(os.path.join("\\".join(os.path.dirname(__file__).split("\\")[:-1]), '..'))
    from dicts import hieroglyph_dict
    
    key_dic = {NAME:       {KEY_F1:               ['KEY_F1', '', '', '', '', ''],
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
                            KEY_MINUS:        ['KEY_MINUS', "- =", "-", "=", '' , '' ],
                            KEY_ASCIICIRCUM:       ['KEY_ASCIICIRCUM',"^ ~", "^", "~", '', ''],
                            KEY_BAR   :       ['KEY_BAR', "\\ |", "\\", "|", '',    ''],
                            KEY_Q     :       ['KEY_Q', "{0} Q".format(unicodedata.lookup(hieroglyph_dict.q[0])), "q", "Q", '', ''],
                            KEY_W     :       ['KEY_W', "{0} W".format(unicodedata.lookup(hieroglyph_dict.w[0])), "w", "W", '', ''],
                            KEY_E     :       ['KEY_E', "{0} E".format(unicodedata.lookup(hieroglyph_dict.e[0])), "e", "E", '', ''],
                            KEY_R     :       ['KEY_R', "{0} R".format(unicodedata.lookup(hieroglyph_dict.r[0])), "r", "R", '', ''],
                            KEY_T     :       ['KEY_T', "{0} T".format(unicodedata.lookup(hieroglyph_dict.t[0])), "t", "T", '', ''],
                            KEY_Y     :       ['KEY_Y', "{0} Y".format(unicodedata.lookup(hieroglyph_dict.y[0])), "y", "Y", '', ''],
                            KEY_U     :       ['KEY_U', "{0} U".format(unicodedata.lookup(hieroglyph_dict.u[0])), "u", "U", '', ''],
                            KEY_I     :       ['KEY_I', "{0} I".format(unicodedata.lookup(hieroglyph_dict.i[0])), "i", "I", '', ''],
                            KEY_O     :       ['KEY_O', "{0} O".format(unicodedata.lookup(hieroglyph_dict.o[0])), "o", "O", '', ''],
                            KEY_P     :       ['KEY_P', "{0} P".format(unicodedata.lookup(hieroglyph_dict.p[0])), "p", "P", '', ''],
                            KEY_AT    :       ['KEY_AT', "{0} `".format(unicodedata.lookup(hieroglyph_dict.aa[0])),"aa", "`", '',''],
                            KEY_BRACKETLEFT    :       ['KEY_BRACKETLEFT', "[ {", "[", "{",'',''],
                            KEY_A     :       ['KEY_A', "{0} A".format(unicodedata.lookup(hieroglyph_dict.a[0])), "a", "A", '', ''],
                            KEY_S     :       ['KEY_S', "{0} S".format(unicodedata.lookup(hieroglyph_dict.s[0])), "s", "S", '', ''],
                            KEY_D     :       ['KEY_D', "{0} D".format(unicodedata.lookup(hieroglyph_dict.d[0])), "d", "D", '', ''],
                            KEY_F     :       ['KEY_F', "{0} F".format(unicodedata.lookup(hieroglyph_dict.f[0])), "f", "F", '', ''],
                            KEY_G     :       ['KEY_G', "{0} G".format(unicodedata.lookup(hieroglyph_dict.g[0])), "g", "G", '', ''],
                            KEY_H     :       ['KEY_H', "{0} H".format(unicodedata.lookup(hieroglyph_dict.h[0])), "h", "H", '', ''],
                            KEY_J     :       ['KEY_J',         "{0} J".format(unicodedata.lookup(hieroglyph_dict.nl[0])), "nl", "J", '', ''],
                            KEY_K     :       ['KEY_K',         "{0} K".format(unicodedata.lookup(hieroglyph_dict.k[0])), "k", "K", '', ''],
                            KEY_L     :       ['KEY_L',         "{0} L".format(unicodedata.lookup(hieroglyph_dict.l[0])), "l", "L", '', ''],
                            KEY_SEMICOLON:    ['KEY_SEMICOLON', "{0} +".format(unicodedata.lookup(hieroglyph_dict.nu[0])), "nu", "+", '', ''],
                            KEY_COLON:        ['KEY_COLON',     ": *", ":", "*", '', ''],
                            KEY_BRACKETRIGHT   :        ['KEY_BRACKETRIGHT',        "] }", "]", "}", '', ''],
                            KEY_Z    :        ['KEY_Z',         "{0} Z".format(unicodedata.lookup(hieroglyph_dict.z[0])), "z", "Z", '',  ''],
                            KEY_X    :        ['KEY_X',         "{0} X".format(unicodedata.lookup(hieroglyph_dict.x[0])), "x", "X", '',  ''],
                            KEY_C    :        ['KEY_C',         "{0} C".format(unicodedata.lookup(hieroglyph_dict.c[0])), "c", "C", '',  ''],
                            KEY_B    :        ['KEY_B',         "{0} B".format(unicodedata.lookup(hieroglyph_dict.b[0])), "b", "B", '',  ''],
                            KEY_V    :        ['KEY_V',         "{0} V".format(unicodedata.lookup(hieroglyph_dict.v[0])), "v", "V", '',  ''],
                            KEY_N    :        ['KEY_N',         "{0} N".format(unicodedata.lookup(hieroglyph_dict.n[0])), "n", "N", '',  ''],
                            KEY_M    :        ['KEY_M',         '{0} M'.format(unicodedata.lookup(hieroglyph_dict.m[0])), 'm', 'M', '',  ''],
                            KEY_COMMA:        ['KEY_COMMA',",   <", ",", "<",'', ''],
                            KEY_PERIOD  :        ['KEY_PERIOD',".     >", ".", ">", '', ''],
                            KEY_SLASH:        ['KEY_SLASH',     "/ ?", "/", "?", '', ''],
                            KEY_BACKSLASH:    ['KEY_BACKSLASH', "\\ _", "\\", "_", '', ''],
                            KEY_SPACE:        ['KEY_SPACE',     "SPACE", " ", "", "", ""]}}

    print(hieroglyph_dict.g[0])
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
