import sqlite3
from commonnames import *

def make():


    NAME = gez_ET
    
    import unicodedata
    COMBINING_GEMINATION_AND_VOWEL_LENGTH_MARK = unicodedata.lookup("ETHIOPIC COMBINING GEMINATION AND VOWEL LENGTH MARK")
    ETHIOPIA_SECTION_MARK = unicodedata.lookup("ETHIOPIC SECTION MARK")
    ETHIOPIC_WORDSPACE = unicodedata.lookup("ETHIOPIC WORDSPACE")
    ETHIOPIC_FULL_STOP = unicodedata.lookup("ETHIOPIC FULL STOP")
    ETHIOPIC_COMMA = unicodedata.lookup("ETHIOPIC COMMA")
    ETHIOPIC_SEMICOLON = unicodedata.lookup("ETHIOPIC SEMICOLON")
    ETHIOPIC_COLON = unicodedata.lookup("ETHIOPIC COLON")
    ETHIOPIC_PREFACE_COLON =  unicodedata.lookup("ETHIOPIC PREFACE COLON")
    ETHIOPIC_QUESTION_MARK = unicodedata.lookup("ETHIOPIC QUESTION MARK")
    ETHIOPIC_PARAGRAPH_SEPARATOR = unicodedata.lookup("ETHIOPIC PARAGRAPH SEPARATOR")
    ETHIOPIC_COMBINING_GEMINATION_MARK = unicodedata.lookup("ETHIOPIC COMBINING GEMINATION MARK") 
    ETHIOPIC_COMBINING_VOWEL_LENGTH_MARK = unicodedata.lookup("ETHIOPIC COMBINING VOWEL LENGTH MARK")
    
    key_dic =  {NAME:       {KEY_F1:               ['KEY_F1', '', '', '', '', ''],
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
                            KEY_1:            ['KEY_1', "፩ ፲", "፩", "፲", '', ''],
                            KEY_2:            ['KEY_2', '፪ ፳', "፪", '፳', '', ''],
                            KEY_3:            ['KEY_3', '፫ ፴', "፫", "፴", '', ''],
                            KEY_4:            ['KEY_4', "፬ ፵", "፬", "፵", '', ''],
                            KEY_5:            ['KEY_5', "፭ ፶", "፭", "፶", '', ''],
                            KEY_6:            ['KEY_6', "፮ ፷", "፮", "፷",'', ''],
                            KEY_7:            ['KEY_7', "፯ ፸","፯", "፸", '', ''],
                            KEY_8:            ['KEY_8', "፰ ፹", "፰", "፹", '', ''],
                            KEY_9:            ['KEY_9', "፱ ፺", "፱", "፺", '', ''],
                            KEY_0:            ['KEY_0', "፻ ፼", "፻", "፼",  '', ''],
                            KEY_MINUS:        ['KEY_MINUS', "{0} {1}".format(ETHIOPIC_COMBINING_GEMINATION_MARK, ETHIOPIC_COMBINING_VOWEL_LENGTH_MARK),"{0}".format(ETHIOPIC_COMBINING_GEMINATION_MARK),"{0}".format(ETHIOPIC_COMBINING_VOWEL_LENGTH_MARK), '' , '' ],
                            KEY_ASCIICIRCUM:       ['KEY_ASCIICIRCUM',"= +","=","+", '', ''],
                            KEY_BAR   :       ['KEY_BAR', "{0} ~".format(COMBINING_GEMINATION_AND_VOWEL_LENGTH_MARK),"{0}".format(COMBINING_GEMINATION_AND_VOWEL_LENGTH_MARK),"~", '',    ''],
                            KEY_Q     :       ['KEY_Q', "ቅ {0}".format(ETHIOPIA_SECTION_MARK), "ቅ", "{0}".format(ETHIOPIA_SECTION_MARK), '', ''],
                            KEY_W     :       ['KEY_W', "ው {0}".format(ETHIOPIC_WORDSPACE),"ው","{0}".format(ETHIOPIC_WORDSPACE), '', ''],
                            KEY_E     :       ['KEY_E', "እ ዕ","እ","ዕ", '', ''],
                            KEY_R     :       ['KEY_R', "ር R","ር","R", '', ''],
                            KEY_T     :       ['KEY_T', "ት ጥ","ት","ጥ", '', ''],
                            KEY_Y     :       ['KEY_Y', "ይ Y","ይ","Y", '', ''],
                            KEY_U     :       ['KEY_U', "ኡ ዑ","ኡ","ዑ", '', ''],
                            KEY_I     :       ['KEY_I', "ኢ ዒ","ኢ","ዒ", '', ''],
                            KEY_O     :       ['KEY_O', "ኦ ዖ","ኦ","ዖ", '', ''],
                            KEY_P     :       ['KEY_P', "ፕ ጵ","ፕ","ጵ", '', ''],
                            KEY_AT    :       ['KEY_AT', "[ {","[","{", '',''],
                            KEY_BRACKETLEFT    :       ['KEY_BRACKETLEFT', "]  }","]","}",'',''],
                            KEY_A     :       ['KEY_A', "አ ዐ","አ","ዐ", '', ''],
                            KEY_S     :       ['KEY_S', "ስ ሽ","ስ","ሽ", '', ''],
                            KEY_D     :       ['KEY_D', "ድ D","ድ","D", '', ''],
                            KEY_F     :       ['KEY_F', "ፍ F","ፍ","F", '', ''],
                            KEY_G     :       ['KEY_G', "ግ G","ግ","G", '', ''],
                            KEY_H     :       ['KEY_H', "ህ H","ህ","H", '', ''],
                            KEY_J     :       ['KEY_J',         "ጅ J","ጅ", "J", '', ''],
                            KEY_K     :       ['KEY_K',         "ክ ኽ","ክ", "ኽ", '', ''],
                            KEY_L     :       ['KEY_L',         "ል L","ል", "L", '', ''],
                            KEY_SEMICOLON:    ['KEY_SEMICOLON', "{0}  {1}".format(ETHIOPIC_SEMICOLON, ETHIOPIC_PREFACE_COLON),"{0}".format(ETHIOPIC_SEMICOLON), "{0}".format(ETHIOPIC_PREFACE_COLON), '', ''],
                            KEY_COLON:        ['KEY_COLON',     "{0}  ".format(ETHIOPIC_COLON),"{0}".format(ETHIOPIC_COLON),'"', '', ''],
                            KEY_BRACKETRIGHT   :        ['KEY_BRACKETRIGHT',        "\\ {0}".format(ETHIOPIC_PARAGRAPH_SEPARATOR),"\\","{0}".format(ETHIOPIC_PARAGRAPH_SEPARATOR), '', ''],
                            KEY_Z    :        ['KEY_Z',         "ዝ ዥ","ዝ", "ዥ", '',  ''],
                            KEY_X    :        ['KEY_X',         "ሽ X","ሽ", "X", '',  ''],
                            KEY_C    :        ['KEY_C',         "ች ጭ","ች", "ጭ", '',  ''],
                            KEY_B    :        ['KEY_B',         "ብ B","ብ", "B", '',  ''],
                            KEY_V    :        ['KEY_V',         "ቭ V","ቭ", "V", '',  ''],
                            KEY_N    :        ['KEY_N',         "ን ኝ", "ን","ኝ", '',  ''],
                            KEY_M    :        ['KEY_M',         "ም M", "ም","M", '',  ''],
                            KEY_COMMA:        ['KEY_COMMA',     "{0} <".format(ETHIOPIC_COMMA),"{0}".format(ETHIOPIC_COMMA),"<",'', ''],
                            KEY_PERIOD  :        ['KEY_PERIOD',       "{0} >".format(ETHIOPIC_FULL_STOP),"{0}".format(ETHIOPIC_FULL_STOP),">", '', ''],
                            KEY_SLASH:        ['KEY_SLASH',     "! {0}".format(ETHIOPIC_QUESTION_MARK),"!","{0}".format(ETHIOPIC_QUESTION_MARK), '', ''],
                            KEY_BACKSLASH:    ['KEY_BACKSLASH', "{0} ?".format(COMBINING_GEMINATION_AND_VOWEL_LENGTH_MARK),"{0}".format(COMBINING_GEMINATION_AND_VOWEL_LENGTH_MARK),"?", '', ''],
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
