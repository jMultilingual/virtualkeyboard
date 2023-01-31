from PySide6.QtGui import QTextCursor, QTextFormat, QTextCharFormat
from PySide6.QtCore import QKeyCombination, Qt, QLocale

listNumberDic = {Qt.Key_1:0, Qt.Key_2:1,
                       Qt.Key_3:2, Qt.Key_4:3,
                       Qt.Key_4:3, Qt.Key_5:4,
                       Qt.Key_5:4, Qt.Key_6:5,
                       Qt.Key_7:6, Qt.Key_8:7,
                       Qt.Key_8:7, Qt.Key_9:8,
                       Qt.Key_9:8}

class KeyDict(dict):

    def __missing__(self, key):
        return -1

    def __add__(self, other_dict):
        other_keys = other_dict.keys()
        for i in other_keys:
            self[i] = other_dict[i]

        return self

    
BopomofoCharacterLists = [chr(i) for i in range(0x03105, 0x0312E)]
BopomofoConsonantLists = [chr(i) for i in range(0x03105, 0x0311A)]
BopomofoMiddleVowelLists = [chr(0x03127), chr(0x03128), chr(0x03129)]
BopomofoVowelLists = [chr(i) for i in range(0x0311A, 0x0312E)]
BopomofoThirdVowelLists = [chr(i) for i in range(0x0311A, 0x03127)] + [chr(i) for i in range(0x0312A, 0x0312E)]
BopomofoToneLists = ["ˉ","ˇ","ˋ","ˊ","˙"]
BopomofoAllLists = BopomofoCharacterLists + ["ˉ","ˇ","ˋ","ˊ","˙"]
UserProperty = QTextFormat.UserProperty
BopomofoListProperty = UserProperty + 1

FontPointSize = QTextFormat.Property.FontPointSize
DotLine  = QTextCharFormat.UnderlineStyle.DotLine
DashDotLine = QTextCharFormat.UnderlineStyle.DashDotLine


PreviousCharacter = QTextCursor.PreviousCharacter
NextCharacter = QTextCursor.NextCharacter
PreviousBlock = QTextCursor.PreviousBlock

NextBlock = QTextCursor.NextBlock
EndOfBlock = QTextCursor.EndOfBlock
StartOfBlock = QTextCursor.StartOfBlock
StartOfLine  = QTextCursor.StartOfLine
EndOfLine = QTextCursor.EndOfLine

Start = QTextCursor.Start
End = QTextCursor.End

Right = QTextCursor.Right
Down = QTextCursor.Down
Left = QTextCursor.Left
Up= QTextCursor.Up


MoveAnchor = QTextCursor.MoveAnchor
KeepAnchor = QTextCursor.KeepAnchor

ar_MA =  QLocale(QLocale.Language.Arabic, QLocale.Country.Morocco).name()
be_BY = QLocale(QLocale.Language.Belarusian, QLocale.Country.Belarus).name()
bn_BD = QLocale(QLocale.Language.Bangla, QLocale.Country.Bangladesh).name()
bs_BA = QLocale(QLocale.Language.Bosnian, QLocale.Country.BosniaAndHerzegovina).name()
bg_BG = QLocale(QLocale.Language.Bulgarian, QLocale.Country.Bulgaria).name()
chr_US = QLocale(QLocale.Language.Cherokee, QLocale.Country.UnitedStates).name()
cs_CZ =  QLocale(QLocale.Language.Czech, QLocale.Country.Czechia).name()

da_DK = QLocale(QLocale.Language.Danish, QLocale.Country.Denmark).name()
dz_BT =  QLocale(QLocale.Language.Dzongkha , QLocale.Country.Bhutan).name()
de_DE = QLocale(QLocale.Language.German, QLocale.Country.Germany).name()
hi_IN = QLocale(QLocale.Language.Hindi, QLocale.Country.India).name()
fr_FR = QLocale(QLocale.Language.French, QLocale.Country.France).name()
is_IS = QLocale(QLocale.Language.Icelandic, QLocale.Country.Iceland).name()
iu_CA = QLocale(QLocale.Language.Inuktitut, QLocale.Country.Canada).name()
it_IT = QLocale(QLocale.Language.Italian, QLocale.Country.Italy).name()
ee_GH = QLocale(QLocale.Language.Ewe, QLocale.Country.Ghana).name()
hr_HR = QLocale(QLocale.Language.Croatian, QLocale.Country.Croatia).name()
haw_US = QLocale(QLocale.Language.Hausa, QLocale.Country.Nigeria).name()
sr_RS = QLocale(QLocale.Language.Serbian, QLocale.Country.Serbia).name()
sq_AL = QLocale(QLocale.Language.Albanian, QLocale.Country.Albania).name()
en_GB = QLocale(QLocale.English, QLocale.UnitedKingdom).name()
es_ES = QLocale(QLocale.Language.Spanish, QLocale.Country.Spain).name()
et_EE = QLocale(QLocale.Language.Estonian, QLocale.Country.Estonia).name()
fo_FO = QLocale(QLocale.Language.Faroese, QLocale.Country.FaroeIslands).name()
fi_FI = QLocale(QLocale.Language.Finnish, QLocale.Country.Finland).name()
ru_RU = QLocale(QLocale.Language.Russian, QLocale.Country.Russia).name()
zh_CN = QLocale(QLocale.Language.Chinese, QLocale.Country.China).name()
ko_KR = QLocale(QLocale.Language.Korean, QLocale.Country.SouthKorea).name()
hi_IN = QLocale(QLocale.Language.Hindi, QLocale.Country.India).name()
ar_EG = QLocale(QLocale.Language.Arabic, QLocale.Country.Egypt).name()
el_GR = QLocale(QLocale.Language.Greek, QLocale.Country.Greece).name()
kl_GL = QLocale(QLocale.Language.Kalaallisut, QLocale.Country.Greenland).name()
ka_GE = QLocale(QLocale.Language.Georgian, QLocale.Country.Georgia).name()
gez_ET = QLocale(QLocale.Language.Geez, QLocale.Country.Ethiopia).name()
ga_ID = QLocale(QLocale.Language.Irish, QLocale.Country.Ireland).name()
gu_IN = QLocale(QLocale.Language.Gujarati, QLocale.Country.India).name()
hy_AM = QLocale(QLocale.Language.Armenian, QLocale.Country.Armenia).name()
as_IN = QLocale(QLocale.Language.Assamese, QLocale.Country.India).name()
az_AZ = QLocale(QLocale.Language.Azerbaijani, QLocale.Country.Azerbaijan).name()
ba_RU = QLocale(QLocale.Language.Bashkir, QLocale.Country.Russia).name()
mn_MN = QLocale(QLocale.Language.Mongolian, QLocale.Country.Mongolia).name()
ha_NG = QLocale(QLocale.Language.Hausa, QLocale.Country.Nigeria).name()
he_IL = QLocale(QLocale.Language.Hebrew, QLocale.Country.Israel).name()
jv_ID = QLocale(QLocale.Language.Javanese, QLocale.Country.Indonesia).name()
kn_IN = QLocale(QLocale.Language.Kannada, QLocale.Country.India).name()
ka_GE = QLocale(QLocale.Language.Georgian, QLocale.Country.Georgia).name()
kk_KZ = QLocale(QLocale.Language.Kazakh, QLocale.Country.Kazakhstan).name()
km_KH = QLocale(QLocale.Language.Khmer, QLocale.Country.Cambodia).name()
kok_IN = QLocale(QLocale.Language.Konkani, QLocale.Country.India).name()
ky_KG = QLocale(QLocale.Language.Kyrgyz, QLocale.Country.Kyrgyzstan).name()
lo_LA = QLocale(QLocale.Language.Lao, QLocale.Country.Laos).name()
lt_LT = QLocale(QLocale.Language.Lithuanian, QLocale.Country.Lithuania).name()
lb_LU = QLocale(QLocale.Language.Luxembourgish, QLocale.Country.Luxembourg).name()
lv_LV = QLocale(QLocale.Language.Latvian, QLocale.Country.Latvia).name()
hu_HU = QLocale(QLocale.Language.Hungarian, QLocale.Country.Hungary).name()
mt_MT = QLocale(QLocale.Language.Maltese, QLocale.Country.Malta).name() 
mk_cyri_MK = QLocale(QLocale.Language.Macedonian, QLocale.Country.Macedonia).name()
mr_IN = QLocale(QLocale.Language.Marathi, QLocale.Country.India).name()
ml_IN = QLocale(QLocale.Language.Malayalam, QLocale.Country.India).name()
my_MM = QLocale(QLocale.Language.Burmese, QLocale.Country.Myanmar).name()
ro_MD = QLocale(QLocale.Language.Romanian, QLocale.Country.Moldova).name()
nl_NL = QLocale(QLocale.Language.Dutch, QLocale.Country.Netherlands).name()
nqo_GN = QLocale(QLocale.Language.Nko, QLocale.Country.Guinea).name()
nb_NO = QLocale(QLocale.Language.NorwegianBokmal, QLocale.Country.Norway).name()
or_IN = QLocale(QLocale.Language.Odia, QLocale.Country.India).name()
ps_AF = QLocale(QLocale.Language.Pashto, QLocale.Country.Afghanistan).name()
pl_PL = QLocale(QLocale.Language.Polish, QLocale.Country.Poland).name()
pt_PT = QLocale(QLocale.Language.Portuguese, QLocale.Country.Portugal).name()
pa_PK = QLocale(QLocale.Language.Punjabi, QLocale.Country.Pakistan).name()
ro_RO = QLocale(QLocale.Language.Romanian, QLocale.Country.Romania).name()
ru_RU = QLocale(QLocale.Language.Russian, QLocale.Country.Russia).name()
sah_RU = QLocale(QLocale.Language.Sakha, QLocale.Country.Russia).name()
sa_IN = QLocale(QLocale.Language.Sanskrit, QLocale.Country.India).name()
fr_SN = QLocale(QLocale.Language.French, QLocale.Country.Senegal).name()
si_LK = QLocale(QLocale.Language.Sinhala, QLocale.Country.SriLanka).name()
sk_SK = QLocale(QLocale.Language.Slovak, QLocale.Country.Slovakia).name()
sl_SI = QLocale(QLocale.Language.Slovenian, QLocale.Country.Slovenia).name()
sv_SE = QLocale(QLocale.Language.Swedish, QLocale.Country.Sweden).name()
syr_IQ = QLocale(QLocale.Language.Syriac, QLocale.Country.Syria).name()
tg_TJ = QLocale(QLocale.Language.Tajik, QLocale.Country.Tajikistan).name()
ta_IN = QLocale(QLocale.Language.Tamil, QLocale.Country.India).name()
te_IN = QLocale(QLocale.Language.Telugu, QLocale.Country.India).name()
th_TH = QLocale(QLocale.Language.Thai, QLocale.Country.Thailand).name()
tr_TR = QLocale(QLocale.Language.Turkish, QLocale.Country.Turkey).name()
dv_MV = QLocale(QLocale.Language.Divehi, QLocale.Country.Maldives).name()
tk_TM = QLocale(QLocale.Language.Turkmen, QLocale.Country.Turkmenistan).name()
uk_UA = QLocale(QLocale.Language.Ukrainian, QLocale.Country.Ukraine).name()
uz_UZ = QLocale(QLocale.Language.Uzbek, QLocale.Country.Uzbekistan).name()
tzm_MA = QLocale(QLocale.Language.CentralAtlasTamazight, QLocale.Country.Morocco).name()
vi_VN = QLocale(QLocale.Language.Vietnamese, QLocale.Country.Vietnam).name()
cy_GB = QLocale(QLocale.Language.Welsh, QLocale.Country.UnitedKingdom).name()
wo_SN = QLocale(QLocale.Language.Wolof, QLocale.Country.Senegal).name()
yo_NG = QLocale(QLocale.Language.Yoruba, QLocale.Country.Nigeria).name()
ckb_IQ = QLocale(QLocale.Language.CentralKurdish, QLocale.Country.Turkey).name()
ccp_BD = QLocale(QLocale.Language.Chakma, QLocale.Country.Bangladesh).name()
cjm_VN = 'cja_VN'

lat_LA = 'lat_lA'

lif_IN = 'lif_IN'

gsw_DE = alzas_Deutsch = "gsw_DE"

#オルチキ文字
olck = 'olck'
#パスパ文字
phag = 'phag'
#パウチンハウ
pauc = 'pauc'

#彝語
yi_CN = 'yi_CN'
#ボポモフォ
bo_TA = 'bo_TA'
#ヒエログリフ
hi_EG = 'hi_EG'
#楔形文字
cu_PE = 'cu_PE'
#ディンカ語
din_SD = 'din_SD'
#エルバサン語
el_IT = 'el_IT'
#フリスク語
fry_NL = "fry_NL"
#ゴート語
go_EU = "go_EU"
#カイティー文字
kai_IN = 'kai_IN'
#カシ語
kha_IN = 'kha_IN'
#カロ―シュティー文字
khar = 'khar'
#リス語
lis_CH = 'lis_CH'
#ブギス語(ロンタラ文字)
bug_IN = 'bug_IN'
#マンダ語
myz = 'myz'
#ナバホ語
nv_US = 'nv_US'
#古代北アラビア文字
narb = 'narb'
#オガム文字
ogam = 'ogam'
#サモティギア文字
sgs = 'sgs'
#タクリ語
ta_IN = 'ta_IN'

#古イタリア文字
ital = 'ital'
#サマリア語
smp = 'smp'
#悉曇文字
sidd = 'sidd'
#シレジア語
szl_PL = QLocale(QLocale.Language.Silesian, QLocale.Country.Poland).name()
#ソーラー語
sora = 'sora'
#南エジプト文字
sarb = 'sarb'
#スンダ文字
sunda = 'sunda'
#ウガリット文字
ugar = 'ugar'

syc = 'syc'
#ipa
ipa = 'ipa'


#バグ-> ja_JP
ba_IN = QLocale(QLocale.Language.Balinese, QLocale.Country.Indonesia).name()
ba_IN = 'ba_IN'
bat_IN = QLocale(QLocale.Language.BatakToba, QLocale.Country.Indonesia).name()
bat_IN = 'bat_IN'


KEY_F1 = "KEY_F1"
KEY_F2 = "KEY_F2"
KEY_F3 = "KEY_F3"
KEY_F4 = "KEY_F4"
KEY_F5 = "KEY_F5"
KEY_F6 = "KEY_F6"
KEY_F7 = "KEY_F7"
KEY_F8 = "KEY_F8"
KEY_F9 = "KEY_F9"
KEY_F10 = "KEY_F10"
KEY_F11 = "KEY_F11"
KEY_F12 = "KEY_F12"

KEY_A = "KEY_A"
KEY_B = "KEY_B"
KEY_C = "KEY_C"
KEY_D = "KEY_D"
KEY_E = "KEY_E"
KEY_F = "KEY_F"
KEY_G = "KEY_G"
KEY_H = "KEY_H"
KEY_I = "KEY_I"
KEY_J = "KEY_J"
KEY_K = "KEY_K"
KEY_L = "KEY_L"
KEY_M = "KEY_M"
KEY_N = "KEY_N"
KEY_O = "KEY_O"
KEY_P = "KEY_P"
KEY_Q = "KEY_Q"
KEY_R = "KEY_R"
KEY_S = "KEY_S"
KEY_T = "KEY_T"
KEY_U = "KEY_U"
KEY_V = "KEY_V"
KEY_W = "KEY_W"
KEY_X = "KEY_X"
KEY_Y = "KEY_Y"
KEY_Z = "KEY_Z"


KEY_0 = "KEY_0"
KEY_1 = "KEY_1"
KEY_2 = "KEY_2"
KEY_3 = "KEY_3"
KEY_4 = "KEY_4"
KEY_5 = "KEY_5"
KEY_6 = "KEY_6"
KEY_7 = "KEY_7"
KEY_8 = "KEY_8"
KEY_9 = "KEY_9"


KEY_COLON = "KEY_COLON"
KEY_SEMICOLON = "KEY_SEMICOLON"
KEY_BRACKETLEFT = "KEY_BRACKETLEFT"
KEY_BRACKETRIGHT = "KEY_BRACKETRIGHT"
KEY_AT = "KEY_AT"
KEY_PERIOD = "KEY_PERIOD"
KEY_COMMA  = "KEY_COMMA"
KEY_SLASH = "KEY_SLASH"
KEY_BACKSLASH = "KEY_BACKSLASH"
KEY_MINUS = "KEY_MINUS"
KEY_ASCIICIRCUM = "KEY_ASCIICIRCUM"
KEY_BAR = "KEY_BAR"


KEY_ESCAPE = "KEY_ESCAPE"
KEY_IME = "KEY_IME"
KEY_TAB = "KEY_TAB"
KEY_CAPSLOCK = "KEY_CAPSLOCK"
KEY_LEFTSHIFT = "KEY_LEFTSHIFT"
KEY_LEFTCONTROL = "KEY_LEFTCONTROL"
KEY_WINDOW = "KEY_WINDOW"
KEY_LEFTALT = "KEY_LEFTALT"
KEY_NOCONVERSION = "KEY_NOCONVERSION"

KEY_CONVERSION = "KEY_CONVERSION"
KEY_KATAKANA = "KEY_KATAKANA"
KEY_RIGHTALT = "KEY_RIGHTALT"
KEY_TOOL = "KEY_TOOL"
KEY_RIGHTCONTROL = "KEY_RIGHTCONTROL"
KEY_SPACE = "KEY_SPACE"
KEY_ENTER = "KEY_ENTER"
KEY_COLON = "KEY_COLON"
KEY_SEMICOLON = "KEY_SEMICOLON"
KEY_AT = "KEY_AT"
KEY_COMMA = "KEY_COMMA"
KEY_PERIOD = "KEY_PERIOD"
KEY_SLASH = "KEY_SLASH"
kEY_BACKSLASH = "KEY_BACKSLASH"
KEY_BRACKETLEFT = "KEY_BRACKETLEFT"
KEY_BRACKETRIGHT = "KEY_BRACKETRIGHT"
KEY_MINUS = "KEY_MINUS"
KEY_CIRCUMFLEX = "KEY_ASCIICIRCUM"
KEY_BAR = "KEY_BAR"
KEY_BACKSPACE = "KEY_BACKSPACE"
KEY_ENTER = "KEY_ENTER"
KEY_RIGHTSHIFT = "KEY_RIGHTSHIFT"


KNS = KEYNAMESMAP = {KEY_F1: Qt.Key_F1, KEY_F2: Qt.Key_F2, KEY_F3: Qt.Key_F3, KEY_F4: Qt.Key_F4, KEY_F5: Qt.Key_F5, KEY_F6: Qt.Key_F6, KEY_F7: Qt.Key_F7, KEY_F8: Qt.Key_F8, KEY_F9:Qt.Key_F9, KEY_F10: Qt.Key_F10, KEY_F11:Qt.Key_F11, KEY_F12:Qt.Key_F12,
          KEY_1 : Qt.Key_1,  KEY_2 : Qt.Key_2,  KEY_3 : Qt.Key_3 , KEY_4: Qt.Key_4, KEY_5: Qt.Key_5, KEY_6:  Qt.Key_6, KEY_7: Qt.Key_7,  KEY_8: Qt.Key_8,  KEY_9 :Qt.Key_9, KEY_0:Qt.Key_0,
          KEY_A : Qt.Key_A,  KEY_B : Qt.Key_B , KEY_C : Qt.Key_C , KEY_D: Qt.Key_D, KEY_E: Qt.Key_E, KEY_F:  Qt.Key_F, KEY_G: Qt.Key_G,  KEY_H: Qt.Key_H,  KEY_I :Qt.Key_I,  KEY_J: Qt.Key_J,   KEY_K  :Qt.Key_K  , KEY_L: Qt.Key_L,
          KEY_M : Qt.Key_M,  KEY_N : Qt.Key_N , KEY_O : Qt.Key_O , KEY_P: Qt.Key_P, KEY_Q: Qt.Key_Q, KEY_R:  Qt.Key_R, KEY_S: Qt.Key_S,  KEY_T : Qt.Key_T,KEY_U :Qt.Key_U,   KEY_V: Qt.Key_U,   KEY_V  :Qt.Key_V  , KEY_W: Qt.Key_W,
          KEY_X : Qt.Key_X,  KEY_Y : Qt.Key_Y,  KEY_Z : Qt.Key_Z , KEY_SEMICOLON: Qt.Key_Semicolon, KEY_COLON: Qt.Key_Colon, KEY_AT: Qt.Key_At, KEY_MINUS: Qt.Key_Minus, KEY_ASCIICIRCUM:Qt.Key_AsciiCircum, KEY_BAR: Qt.Key_Bar,
          KEY_BRACKETLEFT: Qt.Key_BracketLeft, KEY_BRACKETRIGHT: Qt.Key_BracketRight, KEY_SLASH: Qt.Key_Slash, KEY_BACKSLASH: Qt.Key_Backslash, KEY_SPACE: Qt.Key_Space,
          KEY_COMMA: Qt.Key_Comma, KEY_PERIOD: Qt.Key_Period}
KEM = KEYENUMSMAP = {key: value for key, value in zip(KEYNAMESMAP.values(), KEYNAMESMAP.keys())}

TBD = TOKENBUTTONDICTS = {KEY_COMMA: Qt.Key_Comma, KEY_PERIOD: Qt.Key_Period, KEY_SEMICOLON: Qt.Key_Semicolon, KEY_COLON: Qt.Key_Colon, KEY_AT: Qt.Key_At, KEY_MINUS: Qt.Key_Minus, KEY_ASCIICIRCUM:Qt.Key_AsciiCircum, KEY_BAR: Qt.Key_Bar,
          KEY_BRACKETLEFT: Qt.Key_BracketLeft, KEY_BRACKETRIGHT: Qt.Key_BracketRight, KEY_SLASH: Qt.Key_Slash, KEY_BACKSLASH: Qt.Key_Backslash}
TKD = TOKENKEYDICTS = {key: value for key, value in zip(TOKENBUTTONDICTS.values(), TOKENBUTTONDICTS.keys())}
Key_Shift_F1 = QKeyCombination(Qt.ShiftModifier, Qt.Key_F1)
Key_Shift_F2 = QKeyCombination(Qt.ShiftModifier, Qt.Key_F2)
Key_Shift_F3 = QKeyCombination(Qt.ShiftModifier, Qt.Key_F3)
Key_Shift_F4 = QKeyCombination(Qt.ShiftModifier, Qt.Key_F4)
Key_Shift_F5 = QKeyCombination(Qt.ShiftModifier, Qt.Key_F5)
Key_Shift_F6 = QKeyCombination(Qt.ShiftModifier, Qt.Key_F6)
Key_Shift_F7 = QKeyCombination(Qt.ShiftModifier, Qt.Key_F7)
Key_Shift_F8 = QKeyCombination(Qt.ShiftModifier, Qt.Key_F8)
Key_Shift_F9 = QKeyCombination(Qt.ShiftModifier, Qt.Key_F9)
Key_Shift_F10 = QKeyCombination(Qt.ShiftModifier, Qt.Key_F10)
Key_Shift_F11 = QKeyCombination(Qt.ShiftModifier, Qt.Key_F11)
Key_Shift_F12 = QKeyCombination(Qt.ShiftModifier, Qt.Key_F12)


Key_Shift_1 = QKeyCombination(Qt.ShiftModifier, Qt.Key_1)
Key_Shift_2 = QKeyCombination(Qt.ShiftModifier, Qt.Key_2)
Key_Shift_3 = QKeyCombination(Qt.ShiftModifier, Qt.Key_3)
Key_Shift_4 = QKeyCombination(Qt.ShiftModifier, Qt.Key_4)
Key_Shift_5 = QKeyCombination(Qt.ShiftModifier, Qt.Key_5)
Key_Shift_6 = QKeyCombination(Qt.ShiftModifier, Qt.Key_6)
Key_Shift_7 = QKeyCombination(Qt.ShiftModifier, Qt.Key_7)
Key_Shift_8 = QKeyCombination(Qt.ShiftModifier, Qt.Key_8)
Key_Shift_9 = QKeyCombination(Qt.ShiftModifier, Qt.Key_9)
Key_Shift_0 = QKeyCombination(Qt.ShiftModifier, Qt.Key_0)


Key_Shift_A = QKeyCombination(Qt.ShiftModifier, Qt.Key_A)
Key_Shift_B = QKeyCombination(Qt.ShiftModifier, Qt.Key_B)
Key_Shift_C = QKeyCombination(Qt.ShiftModifier, Qt.Key_C)
Key_Shift_D = QKeyCombination(Qt.ShiftModifier, Qt.Key_D)
Key_Shift_E = QKeyCombination(Qt.ShiftModifier, Qt.Key_E)
Key_Shift_F = QKeyCombination(Qt.ShiftModifier, Qt.Key_F)
Key_Shift_G = QKeyCombination(Qt.ShiftModifier, Qt.Key_G)
Key_Shift_H = QKeyCombination(Qt.ShiftModifier, Qt.Key_H)
Key_Shift_I = QKeyCombination(Qt.ShiftModifier, Qt.Key_I)
Key_Shift_J = QKeyCombination(Qt.ShiftModifier, Qt.Key_J)
Key_Shift_K = QKeyCombination(Qt.ShiftModifier, Qt.Key_K)
Key_Shift_L = QKeyCombination(Qt.ShiftModifier, Qt.Key_L)
Key_Shift_M = QKeyCombination(Qt.ShiftModifier, Qt.Key_M)
Key_Shift_N = QKeyCombination(Qt.ShiftModifier, Qt.Key_N)
Key_Shift_O = QKeyCombination(Qt.ShiftModifier, Qt.Key_O)
Key_Shift_P = QKeyCombination(Qt.ShiftModifier, Qt.Key_P)
Key_Shift_Q = QKeyCombination(Qt.ShiftModifier, Qt.Key_Q)
Key_Shift_R = QKeyCombination(Qt.ShiftModifier, Qt.Key_R)
Key_Shift_S = QKeyCombination(Qt.ShiftModifier, Qt.Key_S)
Key_Shift_T = QKeyCombination(Qt.ShiftModifier, Qt.Key_T)
Key_Shift_U = QKeyCombination(Qt.ShiftModifier, Qt.Key_U)
Key_Shift_V = QKeyCombination(Qt.ShiftModifier, Qt.Key_V)
Key_Shift_W = QKeyCombination(Qt.ShiftModifier, Qt.Key_W)
Key_Shift_X = QKeyCombination(Qt.ShiftModifier, Qt.Key_X)
Key_Shift_Y = QKeyCombination(Qt.ShiftModifier, Qt.Key_Y)
Key_Shift_Z = QKeyCombination(Qt.ShiftModifier, Qt.Key_Z)

Key_Shift_Colon = QKeyCombination(Qt.ShiftModifier, Qt.Key_Colon)
Key_Shift_Semicolon = QKeyCombination(Qt.ShiftModifier, Qt.Key_Semicolon)
Key_Shift_Comma = QKeyCombination(Qt.ShiftModifier, Qt.Key_Comma)
Key_Shift_Period = QKeyCombination(Qt.ShiftModifier, Qt.Key_Period)
Key_Shift_Slash = QKeyCombination(Qt.ShiftModifier, Qt.Key_Slash)
Key_Shift_Backslash = QKeyCombination(Qt.ShiftModifier, Qt.Key_Backslash)
Key_Shift_At = QKeyCombination(Qt.ShiftModifier, Qt.Key_At)
Key_Shift_Minus = QKeyCombination(Qt.ShiftModifier, Qt.Key_Minus)
Key_Shift_Bar = QKeyCombination(Qt.ShiftModifier, Qt.Key_Bar)
Key_Shift_Asciicircum = QKeyCombination(Qt.ShiftModifier, Qt.Key_AsciiCircum)
Key_Shift_BracketLeft = QKeyCombination(Qt.ShiftModifier, Qt.Key_BracketLeft)
Key_Shift_BracketRight = QKeyCombination(Qt.ShiftModifier, Qt.Key_BracketRight)

Key_Alt_F1 = QKeyCombination(Qt.AltModifier, Qt.Key_F1)
Key_Alt_F2 = QKeyCombination(Qt.AltModifier, Qt.Key_F2)
Key_Alt_F3 = QKeyCombination(Qt.AltModifier, Qt.Key_F3)
Key_Alt_F4 = QKeyCombination(Qt.AltModifier, Qt.Key_F4)
Key_Alt_F5 = QKeyCombination(Qt.AltModifier, Qt.Key_F5)
Key_Alt_F6 = QKeyCombination(Qt.AltModifier, Qt.Key_F6)
Key_Alt_F7 = QKeyCombination(Qt.AltModifier, Qt.Key_F7)
Key_Alt_F8 = QKeyCombination(Qt.AltModifier, Qt.Key_F8)
Key_Alt_F9 = QKeyCombination(Qt.AltModifier, Qt.Key_F9)
Key_Alt_F10 = QKeyCombination(Qt.AltModifier, Qt.Key_F10)
Key_Alt_F11 = QKeyCombination(Qt.AltModifier, Qt.Key_F11)
Key_Alt_F12 = QKeyCombination(Qt.AltModifier, Qt.Key_F12)


Key_Alt_1 = QKeyCombination(Qt.AltModifier, Qt.Key_1)
Key_Alt_2 = QKeyCombination(Qt.AltModifier, Qt.Key_2)
Key_Alt_3 = QKeyCombination(Qt.AltModifier, Qt.Key_3)
Key_Alt_4 = QKeyCombination(Qt.AltModifier, Qt.Key_4)
Key_Alt_5 = QKeyCombination(Qt.AltModifier, Qt.Key_5)
Key_Alt_6 = QKeyCombination(Qt.AltModifier, Qt.Key_6)
Key_Alt_7 = QKeyCombination(Qt.AltModifier, Qt.Key_7)
Key_Alt_8 = QKeyCombination(Qt.AltModifier, Qt.Key_8)
Key_Alt_9 = QKeyCombination(Qt.AltModifier, Qt.Key_9)
Key_Alt_0 = QKeyCombination(Qt.AltModifier, Qt.Key_0)


Key_Alt_A = QKeyCombination(Qt.AltModifier, Qt.Key_A)
Key_Alt_B = QKeyCombination(Qt.AltModifier, Qt.Key_B)
Key_Alt_C = QKeyCombination(Qt.AltModifier, Qt.Key_C)
Key_Alt_D = QKeyCombination(Qt.AltModifier, Qt.Key_D)
Key_Alt_E = QKeyCombination(Qt.AltModifier, Qt.Key_E)
Key_Alt_F = QKeyCombination(Qt.AltModifier, Qt.Key_F)
Key_Alt_G = QKeyCombination(Qt.AltModifier, Qt.Key_G)
Key_Alt_H = QKeyCombination(Qt.AltModifier, Qt.Key_H)
Key_Alt_I = QKeyCombination(Qt.AltModifier, Qt.Key_I)
Key_Alt_J = QKeyCombination(Qt.AltModifier, Qt.Key_J)
Key_Alt_K = QKeyCombination(Qt.AltModifier, Qt.Key_K)
Key_Alt_L = QKeyCombination(Qt.AltModifier, Qt.Key_L)
Key_Alt_M = QKeyCombination(Qt.AltModifier, Qt.Key_M)
Key_Alt_N = QKeyCombination(Qt.AltModifier, Qt.Key_N)
Key_Alt_O = QKeyCombination(Qt.AltModifier, Qt.Key_O)
Key_Alt_P = QKeyCombination(Qt.AltModifier, Qt.Key_P)
Key_Alt_Q = QKeyCombination(Qt.AltModifier, Qt.Key_Q)
Key_Alt_R = QKeyCombination(Qt.AltModifier, Qt.Key_R)
Key_Alt_S = QKeyCombination(Qt.AltModifier, Qt.Key_S)
Key_Alt_T = QKeyCombination(Qt.AltModifier, Qt.Key_T)
Key_Alt_U = QKeyCombination(Qt.AltModifier, Qt.Key_U)
Key_Alt_V = QKeyCombination(Qt.AltModifier, Qt.Key_V)
Key_Alt_W = QKeyCombination(Qt.AltModifier, Qt.Key_W)
Key_Alt_X = QKeyCombination(Qt.AltModifier, Qt.Key_X)
Key_Alt_Y = QKeyCombination(Qt.AltModifier, Qt.Key_Y)
Key_Alt_Z = QKeyCombination(Qt.AltModifier, Qt.Key_Z)

Key_Alt_Colon = QKeyCombination(Qt.AltModifier, Qt.Key_Colon)
Key_Alt_Semicolon = QKeyCombination(Qt.AltModifier, Qt.Key_Semicolon)
Key_Alt_Comma = QKeyCombination(Qt.AltModifier, Qt.Key_Comma)
Key_Alt_Period = QKeyCombination(Qt.AltModifier, Qt.Key_Period)
Key_Alt_Slash = QKeyCombination(Qt.AltModifier, Qt.Key_Slash)
Key_Alt_Backslash = QKeyCombination(Qt.AltModifier, Qt.Key_Backslash)
Key_Alt_At = QKeyCombination(Qt.AltModifier, Qt.Key_At)
Key_Alt_Minus = QKeyCombination(Qt.AltModifier, Qt.Key_Minus)
Key_Alt_Bar = QKeyCombination(Qt.AltModifier, Qt.Key_Bar)
Key_Alt_Asciicircum = QKeyCombination(Qt.AltModifier, Qt.Key_AsciiCircum)
Key_Alt_BracketLeft = QKeyCombination(Qt.AltModifier, Qt.Key_BracketLeft)
Key_Alt_BracketRight = QKeyCombination(Qt.AltModifier, Qt.Key_BracketRight)



Key_Alt_Control_F1 = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_F1)
Key_Alt_Control_F2 = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_F2)
Key_Alt_Control_F3 = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_F3)
Key_Alt_Control_F4 = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_F4)
Key_Alt_Control_F5 = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_F5)
Key_Alt_Control_F6 = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_F6)
Key_Alt_Control_F7 = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_F7)
Key_Alt_Control_F8 = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_F8)
Key_Alt_Control_F9 = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_F9)
Key_Alt_Control_F10 = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_F10)
Key_Alt_Control_F11 = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_F11)
Key_Alt_Control_F12 = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_F12)


Key_Alt_Control_1 = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_1)
Key_Alt_Control_2 = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_2)
Key_Alt_Control_3 = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_3)
Key_Alt_Control_4 = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_4)
Key_Alt_Control_5 = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_5)
Key_Alt_Control_6 = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_6)
Key_Alt_Control_7 = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_7)
Key_Alt_Control_8 = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_8)
Key_Alt_Control_9 = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_9)
Key_Alt_Control_0 = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_0)


Key_Alt_Control_A = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_A)
Key_Alt_Control_B = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_B)
Key_Alt_Control_C = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_C)
Key_Alt_Control_D = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_D)
Key_Alt_Control_E = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_E)
Key_Alt_Control_F = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_F)
Key_Alt_Control_G = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_G)
Key_Alt_Control_H = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_H)
Key_Alt_Control_I = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_I)
Key_Alt_Control_J = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_J)
Key_Alt_Control_K = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_K)
Key_Alt_Control_L = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_L)
Key_Alt_Control_M = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_M)
Key_Alt_Control_N = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_N)
Key_Alt_Control_O = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_O)
Key_Alt_Control_P = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_P)
Key_Alt_Control_Q = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_Q)
Key_Alt_Control_R = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_R)
Key_Alt_Control_S = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_S)
Key_Alt_Control_T = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_T)
Key_Alt_Control_U = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_U)
Key_Alt_Control_V = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_V)
Key_Alt_Control_W = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_W)
Key_Alt_Control_X = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_X)
Key_Alt_Control_Y = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_Y)
Key_Alt_Control_Z = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_Z)

Key_Alt_Control_Colon = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_Colon)
Key_Alt_Control_Semicolon = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_Semicolon)
Key_Alt_Control_Comma = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_Comma)
Key_Alt_Control_Period = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_Period)
Key_Alt_Control_Slash = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_Slash)
Key_Alt_Control_Backslash = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_Backslash)
Key_Alt_Control_At = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_At)
Key_Alt_Control_Minus = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_Minus)
Key_Alt_Control_Bar = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_Bar)
Key_Alt_Control_Asciicircum = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_AsciiCircum)
Key_Alt_Control_BracketLeft = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_BracketLeft)
Key_Alt_Control_BracketRight = QKeyCombination(Qt.AltModifier|Qt.ControlModifier, Qt.Key_BracketRight)



Key_Control_F3 = QKeyCombination(Qt.ControlModifier, Qt.Key_F3)
KEYNAMETEXT = 0
DISPLAYTEXT = 1
INPUT_TEXT = 2
SHIFT_INPUT_TEXT = 3
ALT_INPUT_TEXT = 4
SHIFT_ALT_INPUT_TEXT = 5

NonCharKeys = [Qt.Key_Escape, Qt.Key_Shift, Qt.Key_Control, Qt.Key_Alt, Qt.Key_F1, Qt.Key_F2, Qt.Key_F3,
               Qt.Key_F4, Qt.Key_F5, Qt.Key_F6, Qt.Key_F7, Qt.Key_F8, Qt.Key_F9, Qt.Key_F10,
               Qt.Key_F11, Qt.Key_F12, Qt.Key_CapsLock, Qt.Key_Tab]


SK = SHIFTMODIFIERS_KEYCOMBINATION = [Key_Shift_A, Key_Shift_B, Key_Shift_C, Key_Shift_D, Key_Shift_E, Key_Shift_F, Key_Shift_G, Key_Shift_H, Key_Shift_I, Key_Shift_J, Key_Shift_K, Key_Shift_L, Key_Shift_M, Key_Shift_N, Key_Shift_O, Key_Shift_P, Key_Shift_Q, Key_Shift_R, Key_Shift_S, Key_Shift_T,
                  Key_Shift_U, Key_Shift_V, Key_Shift_W, Key_Shift_X, Key_Shift_Y, Key_Shift_Z, Key_Shift_Colon, Key_Shift_Semicolon, Key_Shift_Comma, Key_Shift_Period, Key_Shift_Slash, Key_Shift_Backslash, Key_Shift_At, Key_Shift_Minus, Key_Shift_Bar,
                  Key_Shift_Asciicircum, Key_Shift_BracketLeft, Key_Shift_BracketRight]
SE = SHIFTMODIFIERS_ENUMS = [Qt.Key_Exclam, Qt.Key_QuoteDbl, Qt.Key_NumberSign,  Qt.Key_Dollar,  Qt.Key_Percent,  Qt.Key_Ampersand, Qt.Key_Apostrophe, Qt.Key_ParenLeft, Qt.Key_ParenRight, Qt.Key_Asterisk,
                        Qt.Key_Asterisk, Qt.Key_BraceLeft, Qt.Key_BraceRight, Qt.Key_QuoteLeft, Qt.Key_Bar, Qt.Key_AsciiTilde, Qt.Key_Plus, Qt.Key_Question, Qt.Key_Underscore, Qt.Key_Greater, Qt.Key_Less, Qt.Key_Equal]

SETK = SHIFTMODIFIERS_ENUMS_TO_KEYS = {Qt.Key_Exclam: Qt.Key_1, Qt.Key_QuoteDbl: Qt.Key_2, Qt.Key_NumberSign: Qt.Key_3, Qt.Key_Dollar: Qt.Key_4, Qt.Key_Percent: Qt.Key_5,
                                       Qt.Key_Ampersand: Qt.Key_6, Qt.Key_Apostrophe: Qt.Key_7, Qt.Key_ParenLeft: Qt.Key_8, Qt.Key_ParenRight: Qt.Key_9,
                                       Qt.Key.Key_AsciiTilde: Qt.Key.Key_AsciiCircum, Qt.Key.Key_Bar: Qt.Key.Key_Backslash,
                                        Qt.Key_Asterisk: Qt.Key_Colon, Qt.Key_BraceLeft: Qt.Key_BracketLeft, Qt.Key_BraceRight: Qt.Key_BracketRight, Qt.Key_QuoteLeft: Qt.Key_At,
                                       Qt.Key_AsciiTilde: Qt.Key_AsciiCircum, Qt.Key_Plus:Qt.Key_Semicolon, Qt.Key_Question: Qt.Key_Slash, Qt.Key_Equal: Qt.Key_Minus,
                                        Qt.Key_Underscore: Qt.Key_Backslash, Qt.Key_Less:Qt.Key_Comma, Qt.Key_Greater: Qt.Key_Period}


AK = ALTMODIFIERS_KEYCOMBINATION = [Key_Alt_A, Key_Alt_B, Key_Alt_C, Key_Alt_D, Key_Alt_E, Key_Alt_F, Key_Alt_G, Key_Alt_H, Key_Alt_I, Key_Alt_J, Key_Alt_K, Key_Alt_L, Key_Alt_M, Key_Alt_N, Key_Alt_O, Key_Alt_P, Key_Alt_Q, Key_Alt_R, Key_Alt_S, Key_Alt_T,
                  Key_Alt_U, Key_Alt_V, Key_Alt_W, Key_Alt_X, Key_Alt_Y, Key_Alt_Z, Key_Alt_Colon, Key_Alt_Semicolon, Key_Alt_Comma, Key_Alt_Period, Key_Alt_Slash, Key_Alt_Backslash, Key_Alt_At, Key_Alt_Minus, Key_Alt_Bar,
                  Key_Alt_Asciicircum, Key_Alt_BracketLeft, Key_Alt_BracketRight]

AKC = ALTMODIFIERS_CONTROLMODIFIERS_KEYCOMBINATION = [Key_Alt_Control_A, Key_Alt_Control_B, Key_Alt_Control_C, Key_Alt_Control_D, Key_Alt_Control_E, Key_Alt_Control_F, Key_Alt_Control_G, Key_Alt_Control_H, Key_Alt_Control_I, Key_Alt_Control_J, Key_Alt_Control_K, Key_Alt_Control_L, Key_Alt_Control_M, Key_Alt_Control_N, Key_Alt_Control_O, Key_Alt_Control_P, Key_Alt_Control_Q, Key_Alt_Control_R, Key_Alt_Control_S, Key_Alt_Control_T,
                  Key_Alt_Control_U, Key_Alt_Control_V, Key_Alt_Control_W, Key_Alt_Control_X, Key_Alt_Control_Y, Key_Alt_Control_Z, Key_Alt_Control_Colon, Key_Alt_Control_Semicolon, Key_Alt_Control_Comma, Key_Alt_Control_Period, Key_Alt_Control_Slash, Key_Alt_Control_Backslash, Key_Alt_Control_At, Key_Alt_Control_Minus, Key_Alt_Control_Bar,
                  Key_Alt_Control_Asciicircum, Key_Alt_Control_BracketLeft, Key_Alt_Control_BracketRight]

