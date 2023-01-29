import sqlite3
from commonnames import *
def make():


    NAME = cu_PE
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
                            KEY_F12:              ['KEY_F12', 'KEY_F12', 'KEY_F12', 'KEY_F12', '', ''],
                            KEY_1:            ['KEY_1', '{0} !'.format(chr(0x12400)), '1', '!', '', ''],
                            KEY_2:            ['KEY_2', '{0} "'.format(chr(0x12408)), "2", '"', '', ''],
                            KEY_3:            ['KEY_3', '{0} #'.format(chr(0x1240F)), '3', '#', '', ''],
                            KEY_4:            ['KEY_4', '{0} $'.format(chr(0x12415)), '4', '$', '', ''],
                            KEY_5:            ['KEY_5', '{0} %'.format(chr(0x1241E)), '5', '%', '', ''],
                            KEY_6:            ['KEY_6', '{0} &&'.format(chr(0x12423)),'6', '&&','', ''],
                            KEY_7:            ['KEY_7', "{0} '".format(chr(0x1242C)), '7', "'", '', ''],
                            KEY_8:            ['KEY_8', '{0} ('.format(chr(0x12432)), '8', '(', '', ''],
                            KEY_9:            ['KEY_9', '{0} )'.format(chr(0x12434)), '9', ')', '', ''],
                            KEY_0:            ['KEY_0', '{0}  '.format(chr(0x1243A)), '0', '',  '', ''],
                            KEY_MINUS:        ['KEY_MINUS', "{0} =".format(chr(0x12470)), "-", "=", '' , '' ],
                            KEY_ASCIICIRCUM:       ['KEY_ASCIICIRCUM',"^ ~", "^", "~", '', ''],
                            KEY_BAR   :       ['KEY_BAR', "\\ |", "\\", "|", '',    ''],
                            KEY_Q     :       ['KEY_Q', "{0} Q".format(chr(0x12370)), "q", "Q", '', ''],
                            KEY_W     :       ['KEY_W', "{0} W".format(chr(0x12467)), "w", "W", '', ''],
                            KEY_E     :       ['KEY_E', "{0} E".format(chr(0x1208A)), "e", "E", '', ''],
                            KEY_R     :       ['KEY_R', "{0} R".format(chr(0x1228F)), "r", "R", '', ''],
                            KEY_T     :       ['KEY_T', "{0} T".format(chr(0x122EB)), "t", "T", '', ''],
                            KEY_Y     :       ['KEY_Y', "{0} Y".format(chr(0x12469)), "y", "Y", '', ''],
                            KEY_U     :       ['KEY_U', "{0} U".format(chr(0x1230B)), "u", "U", '', ''],
                            KEY_I     :       ['KEY_I', "{0} I".format(chr(0x1213F)), "i", "I", '', ''],
                            KEY_O     :       ['KEY_O', "{0} O".format(chr(0x1244F)), "o", "O", '', ''],
                            KEY_P     :       ['KEY_P', "{0} P".format(chr(0x1227A)), "p", "P", '', ''],
                            KEY_AT    :       ['KEY_AT', "@ `","@", "`", '',''],
                            KEY_BRACKETLEFT    :       ['KEY_BRACKETLEFT', "[ {", "[", "{",'',''],
                            KEY_A     :       ['KEY_A', "{0} A".format(chr(0x12000)), "a", "A", '', ''],
                            KEY_S     :       ['KEY_S', "{0} S".format(chr(0x12293)), "s", "S", '', ''],
                            KEY_D     :       ['KEY_D', "{0} D".format(chr(0x12055)), "d", "D", '', ''],
                            KEY_F     :       ['KEY_F', "{0} F".format(chr(0x12444)), "f", "F", '', ''],
                            KEY_G     :       ['KEY_G', "{0} G".format(chr(0x120B5)), "g", "G", '', ''],
                            KEY_H     :       ['KEY_H', "{0} H".format(chr(0x12129)), "h", "H", '', ''],
                            KEY_J     :       ['KEY_J',         "{0} J".format(chr(0x1244A)), "j", "J", '', ''],
                            KEY_K     :       ['KEY_K',         "{0} K".format(chr(0x12157)), "k", "K", '', ''],
                            KEY_L     :       ['KEY_L',         "{0} L".format(chr(0x121B7)), "l", "L", '', ''],
                            KEY_SEMICOLON:    ['KEY_SEMICOLON', "{0} +".format(chr(0x1245A)), ";", "+", '', ''],
                            KEY_COLON:        ['KEY_COLON',     "{0} *".format(chr(0x1245F)), ":", "*", '', ''],
                            KEY_BRACKETRIGHT   :        ['KEY_BRACKETRIGHT',        "] }", "]", "}", '', ''],
                            KEY_Z    :        ['KEY_Z',         "{0} Z".format(chr(0x1235D)), "z", "Z", '',  ''],
                            KEY_X    :        ['KEY_X',         "{0} X".format(chr(0x12458)), "x", "X", '',  ''],
                            KEY_C    :        ['KEY_C',         "{0} C".format(chr(0x12442)), "c", "C", '',  ''],
                            KEY_B    :        ['KEY_B',         "{0} B".format(chr(0x12040)), "b", "B", '',  ''],
                            KEY_V    :        ['KEY_V',         "{0} V".format(chr(0x12456)), "v", "V", '',  ''],
                            KEY_N    :        ['KEY_N',         "{0} N".format(chr(0x1223E)), "n", "N", '',  ''],
                            KEY_M    :        ['KEY_M',         '{0} M'.format(chr(0x12220)), 'm', 'M', '',  ''],
                            KEY_COMMA:        ['KEY_COMMA',",   <", ",", "<",'', ''],
                            KEY_PERIOD  :        ['KEY_PERIOD',".     >", ".", ">", '', ''],
                            KEY_SLASH:        ['KEY_SLASH',     "{0} ?".format(0x12465), "/", "?", '', ''],
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
