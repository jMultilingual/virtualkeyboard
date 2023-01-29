import sqlite3
from commonnames import *
def make():


    NAME = hi_IN
    
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
                            KEY_1:            ['KEY_1', '१  ऍ', '१', "ऍ", '', ''],
                            KEY_2:            ['KEY_2', '२ ॅ','२','ॅ', '', ''],
                            KEY_3:            ['KEY_3', '३ ्र',"३","्र", '', ''],
                            KEY_4:            ['KEY_4', "४ र्","४","र्", '', ''],
                            KEY_5:            ['KEY_5', "५ ज्ञ","५","ज्ञ", '', ''],
                            KEY_6:            ['KEY_6', "६ त्र","६","त्र",'', ''],
                            KEY_7:            ['KEY_7', "७ क्ष","७","क्ष", '', ''],
                            KEY_8:            ['KEY_8', "८ श्र","८","श्र", '', ''],
                            KEY_9:            ['KEY_9', "९ (","९","(", '', ''],
                            KEY_0:            ['KEY_0', "० )","०",")",  '', ''],
                            KEY_MINUS:        ['KEY_MINUS', "- ः","-","ः", '' , '' ],
                            KEY_ASCIICIRCUM:       ['KEY_ASCIICIRCUM',"ृ ऋ","ृ","ऋ", '', ''],
                            KEY_BAR   :       ['KEY_BAR', " |","","|", '',    ''],
                            KEY_Q     :       ['KEY_Q', "ौ  औ","ौ","औ", '', ''],
                            KEY_W     :       ['KEY_W', "ै ऐ","ै","ऐ", '', ''],
                            KEY_E     :       ['KEY_E', "ा आ","ा","आ", '', ''],
                            KEY_R     :       ['KEY_R', "ी ई","ी","ई", '', ''],
                            KEY_T     :       ['KEY_T', "ू ऊ","ू","ऊ", '', ''],
                            KEY_Y     :       ['KEY_Y', "ब भ","ब","भ", '', ''],
                            KEY_U     :       ['KEY_U', "ह ङ","ह","ङ", '', ''],
                            KEY_I     :       ['KEY_I', "ग घ","ग","घ", '', ''],
                            KEY_O     :       ['KEY_O', "द ध","द","ध", '', ''],
                            KEY_P     :       ['KEY_P', "ज झ","ज","झ", '', ''],
                            KEY_AT    :       ['KEY_AT', "ड ढ","ड","ढ", '',''],
                            KEY_BRACKETLEFT    :       ['KEY_BRACKETLEFT', "़ ञ","़","ञ",'',''],
                            KEY_A     :       ['KEY_A', "ो ओ","ो","ओ", '', ''],
                            KEY_S     :       ['KEY_S', "े ए","े","ए", '', ''],
                            KEY_D     :       ['KEY_D', "् अ","्","अ", '', ''],
                            KEY_F     :       ['KEY_F', "ि  इ","ि","इ", '', ''],
                            KEY_G     :       ['KEY_G', "ु उ","ु","उ", '', ''],
                            KEY_H     :       ['KEY_H', "प फ","प","फ", '', ''],
                            KEY_J     :       ['KEY_J',         "र ऱ","र","ऱ", '', ''],
                            KEY_K     :       ['KEY_K',         "क ख","क","ख", '', ''],
                            KEY_L     :       ['KEY_L',         "त  थ","त","थ", '', ''],
                            KEY_SEMICOLON:    ['KEY_SEMICOLON', 'च छ',"च",'छ', '', ''],
                            KEY_COLON:        ['KEY_COLON',     "ट  ठ","ट",'ठ', '', ''],
                            KEY_BRACKETRIGHT   :        ['KEY_BRACKETRIGHT',        "ॉ ऑ","ॉ","ऑ", '', ''],
                            KEY_Z    :        ['KEY_Z',         "ॐ Z","ॐ","Z", '',  ''],
                            KEY_X    :        ['KEY_X',         "ं ँ","ं","ँ", '',  ''],
                            KEY_C    :        ['KEY_C',         "म ण","म","ण", '',  ''],
                            KEY_B    :        ['KEY_B',         "व B","व","B", '',  ''],
                            KEY_V    :        ['KEY_V',         "न V","न","V", '',  ''],
                            KEY_N    :        ['KEY_N',         "ल ळ","ल","ळ", '',  ''],
                            KEY_M    :        ['KEY_M',         "स श","स","श", '',  ''],
                            KEY_COMMA:        ['KEY_COMMA',     ", ष",",","ष",'', ''],
                            KEY_PERIOD  :        ['KEY_PERIOD',       ". ।",".","।", '', ''],
                            KEY_SLASH:        ['KEY_SLASH',     "य य़","य","य़", '', ''],
                            KEY_BACKSLASH:    ['KEY_BACKSLASH', " ","","", '', ''],
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
