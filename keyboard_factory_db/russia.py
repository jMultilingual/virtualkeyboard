import sqlite3
from commonnames import *

def make():
    
    
    NAME = ru_RU
    
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
                            KEY_1:            ['KEY_1', '1 !', '1', '!', '', ''],
                            KEY_2:            ['KEY_2', '2 "', "2", '"', '', ''],
                            KEY_3:            ['KEY_3', '3 №', "3", "№", '', ''],
                            KEY_4:            ['KEY_4', "4 ;", "4", ";", '', ''],
                            KEY_5:            ['KEY_5', "5 %", "5", "%", '', ''],
                            KEY_6:            ['KEY_6', "6 :", "6", ":",'', ''],
                            KEY_7:            ['KEY_7', "7 ?", "7", "?", '', ''],
                            KEY_8:            ['KEY_8', "8 *", "8", "*", '', ''],
                            KEY_9:            ['KEY_9', "9 (", "9", "(", '', ''],
                            KEY_0:            ['KEY_0', "ʊ\n0 )", "0", ")",  'ʊ', ''],
                            KEY_MINUS:        ['KEY_MINUS', "ˈ\n - _", "-", "_", 'ˈ' , '' ],
                            KEY_ASCIICIRCUM:       ['KEY_ASCIICIRCUM',"ː\n= +", "=", "+", 'ː', ''],
                            KEY_BAR   :       ['KEY_BAR', "ё Ё", "ё", "Ё", '',    ''],
                            KEY_Q     :       ['KEY_Q', "j\nй Й", "й", "Й", 'j', ''],
                            KEY_W     :       ['KEY_W', "ʦ\nц Ц", "ц", "Ц", 'ʦ', ''],
                            KEY_E     :       ['KEY_E', "u ʉ\nу У", "у", "У", 'u', 'ʉ'],
                            KEY_R     :       ['KEY_R', "k kʲ\nк К", "к", "К", 'k', 'kʲ'],
                            KEY_T     :       ['KEY_T', "ɛ\n е Е", "е", "Е", 'ɛ', ''],
                            KEY_Y     :       ['KEY_Y', "n nʲ\nн Н", "н", "Н", 'n', 'nʲ'],
                            KEY_U     :       ['KEY_U', "g gʲ\nг Г", "г", "Г", 'g', 'gʲ'],
                            KEY_I     :       ['KEY_I', "ʂ\nш Ш", "ш", "Ш", 'ʂ', ''],
                            KEY_O     :       ['KEY_O', "ɕː\nщ Щ", "щ", "Щ", '', 'ɕː'],
                            KEY_P     :       ['KEY_P', "z zʲ\nз З", "з", "З", 'z', 'zʲ'],
                            KEY_AT    :       ['KEY_AT', "x xʲ\nх Х", "х", "Х", 'x','xʲ'],
                            KEY_BRACKETLEFT    :       ['KEY_BRACKETLEFT', "ъ Ъ", "ъ", "Ъ",'',''],
                            KEY_A     :       ['KEY_A', "f fʲ\nф Ф", "ф", "Ф", 'f', 'fʲ'],
                            KEY_S     :       ['KEY_S', "ɨ\nы Ы", "ы", "Ы", 'ɨ', ''],
                            KEY_D     :       ['KEY_D', "v vʲ\nв В", "в", "В", 'v', 'vʲ'],
                            KEY_F     :       ['KEY_F', "ɐ æ\nа А", "а", "А", 'ɐ', 'æ'],
                            KEY_G     :       ['KEY_G', "p pʲ\nп П", "п", "П", 'p', 'pʲ'],
                            KEY_H     :       ['KEY_H', "r rʲ\nр Р", "р", "Р", 'r', 'rʲ'],
                            KEY_J     :       ['KEY_J',         "o ɵ\nо О", "о", "О", 'o', 'ɵ'],
                            KEY_K     :       ['KEY_K',         "ɫ lʲ\nл Л", "л", "Л", 'ɫ', 'lʲ'],
                            KEY_L     :       ['KEY_L',         "d dʲ\nд Д", "д", "Д", 'd', 'dʲ'],
                            KEY_SEMICOLON:    ['KEY_SEMICOLON', "ʐ\nж Ж", "ж", "Ж", 'ʐ', ''],
                            KEY_COLON:        ['KEY_COLON',     'э Э', "э", 'Э', '', ''],
                            KEY_BRACKETRIGHT   :        ['KEY_BRACKETRIGHT',        "\\ /", "\\", "/", '', ''],
                            KEY_Z    :        ['KEY_Z',         "я Я", "я", "Я", '',  ''],
                            KEY_X    :        ['KEY_X',         "ʨ\nч Ч", "ч", "Ч", '',  'ʨ'],
                            KEY_C    :        ['KEY_C',         "s sʲ\nс С", "с", "С", 's',  'sʲ'],
                            KEY_B    :        ['KEY_B',         "i\nи И", "и", "И", 'i',  ''],
                            KEY_V    :        ['KEY_V',         "m mʲ\nм М", "м", "М", 'm',  'mʲ'],
                            KEY_N    :        ['KEY_N',         "t tʲ\nт Т", "т", "Т", 't',  'tʲ'],
                            KEY_M    :        ['KEY_M',         "ь Ь", "ь", "Ь", '',  ''],
                            KEY_COMMA:        ['KEY_COMMA',     "bʲ\nб Б", "б", "Б",'bʲ', ''],
                            KEY_PERIOD  :        ['KEY_PERIOD',       "ю Ю", "ю", "Ю", '', ''],
                            KEY_SLASH:        ['KEY_SLASH',     ". , ", ".", ", ", '', ''],
                            KEY_BACKSLASH:    ['KEY_BACKSLASH', "ё Ё", "ё", "Ё", '', ''],
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


