from PySide6.QtWidgets import (QApplication, QTextEdit,QMenu, QMainWindow,
                               QSpacerItem, QHBoxLayout, QVBoxLayout, QWidget,
                               QDockWidget, QPushButton, QListWidgetItem)
from PySide6.QtGui import QAction, QActionGroup, QIcon, QFont, QFontMetricsF, QFontMetrics, QTextCharFormat
from PySide6.QtCore import Qt, QSize, QByteArray, QDataStream, QIODevice
from handmade_ime_listwidget import HandmadeIMEListWidget

import sys, os, sqlite3, re
from keyboard_factory_db.commonnames import *

from hangul import chamo_dict, hangul_repair
from dicts import yi_dict, kantaiji_dict
from key_events import yi_method, bopomofo_method, kantaiji_method





class KeyboardPushButton(QPushButton):

    def __init__(self, keys=["", "", "", "", "", "", ""],
                       icon= QIcon(), text="", objectName="", parent=None
                 ):

        super().__init__(icon, text, parent)

        self.keys = keys
        self.setObjectName(objectName)
        self.setFocusPolicy(Qt.NoFocus)
        self.underLeft = keys[INPUT_TEXT]
        self.underRight = keys[SHIFT_INPUT_TEXT]
        self.upperLeft = keys[ALT_INPUT_TEXT]
        self.upperRight = keys[SHIFT_ALT_INPUT_TEXT]

    def setKeys(self, keys):
        self.keys = keys
        self.underLeft = keys[INPUT_TEXT]
        self.underRight = keys[SHIFT_INPUT_TEXT]
        self.upperLeft = keys[ALT_INPUT_TEXT]
        self.upperRight = keys[SHIFT_ALT_INPUT_TEXT]

  

    def sizeHint(self):
        
        font = self.font()
        matrics = QFontMetricsF(font)
        width = matrics.horizontalAdvance(self.text())
        
        if self.objectName() == KEY_TAB:
            
            return QSize(width+20, 40)
        elif self.objectName() == KEY_CAPSLOCK:
            return QSize(width+40, 40)
        elif self.objectName() == KEY_LEFTSHIFT:
            return QSize(width+60, 40)
        elif self.objectName() == KEY_ENTER:
            return QSize(width+30, 80)
        elif self.objectName() == KEY_SPACE:
            return QSize(width+120, 40)

        return QSize(width, 40)

    def minimumSizeHint(self):
        
        font = self.font()
        matrics = QFontMetricsF(font)
        width = matrics.horizontalAdvance(self.text())

        if self.objectName() == KEY_ENTER:
            
            return QSize(width+30, 80)
        elif self.objectName() == KEY_SPACE:
            return QSize(width+120, 40)

        return QSize(width+20, 40)


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUI()

        self.edit = TextEdit(self)
        self.setCentralWidget(self.edit)

    def closeEvent(self, event):


        QApplication.closeAllWindows()
        
        return super().closeEvent(event)

    def initUI(self):
        self.keyboardDockWidget = QDockWidget("キーボード")
        self.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, self.keyboardDockWidget)
        self.keyboardMenu = QMenu(title="キーボード")
        self.writingSystemChangeMenu = QMenu(title="キーボード切替")
        self.keyboardMenu.addMenu(self.writingSystemChangeMenu)
        self.menuBar().addMenu(self.keyboardMenu)

        self.en_GB_Action = QAction(text="アルファベット(英国)",
                                     triggered = self.writingSystemChanged,
                                     data = en_GB,
                                     checkable = True,
                                     checked = True
                                     )

        self.ru_RU_Action = QAction(text="キリル文字(ロシア)",
                                     triggered = self.writingSystemChanged,
                                     data = ru_RU,
                                     checkable = True
                                    )
        self.zh_CN_Action = QAction(text="簡体字",
                                     triggered = self.writingSystemChanged,
                                     data = zh_CN,
                                     checkable=True)

        self.ko_KR_Action = QAction(text="ハングル文字",
                                    triggered = self.writingSystemChanged,
                                    data = ko_KR,
                                    checkable = True
                                    )
        
        self.hi_IN_Action = QAction(text="デーヴァナーガリ―(インド)",
                                    triggered = self.writingSystemChanged,
                                    data = hi_IN,
                                    checkable = True
                                    )
        
        self.ar_EG_Action = QAction(text="アラビア文字(エジプト)",
                                    triggered = self.writingSystemChanged,
                                    data = ar_EG,
                                    checkable = True
                                    )

        self.gez_ET_Action = QAction(text="ゲエズ文字(エチオピア)",
                                     triggered = self.writingSystemChanged,
                                     data = gez_ET,
                                     checkable = True
                                     )

        self.km_KH_Action = QAction(text="クメール文字(カンボジア)",
                                    triggered = self.writingSystemChanged,
                                    data = km_KH,
                                    checkable = True
                                    )
        self.yi_CN_Action = QAction(text="彝語",
                                    triggered = self.writingSystemChanged,
                                    data = yi_CN,
                                    checkable = True
                                    )
        self.bo_TA_Action = QAction(text="ボポモフォ(台湾)",
                                    triggered = self.writingSystemChanged,
                                    data = bo_TA,
                                    checkable = True
                                    )

        self.hi_EG_Action = QAction(text="ヒエログリフ(エジプト聖刻文字)",
                                    triggered = self.writingSystemChanged,
                                    data=hi_EG,
                                    checkable=True
                                    )

        self.cu_PE_Action = QAction(text="楔形文字",
                                    triggered = self.writingSystemChanged,
                                    data = cu_PE,
                                    checkable = True
                                    )

        
        self.actionGroup = QActionGroup(self)
        self.actionGroup.addAction(self.en_GB_Action)
        self.actionGroup.addAction(self.ru_RU_Action)
        self.actionGroup.addAction(self.zh_CN_Action)
        self.actionGroup.addAction(self.ko_KR_Action)        
        self.actionGroup.addAction(self.hi_IN_Action)
        self.actionGroup.addAction(self.ar_EG_Action)
        self.actionGroup.addAction(self.gez_ET_Action)
        self.actionGroup.addAction(self.km_KH_Action)
        self.actionGroup.addAction(self.yi_CN_Action)
        self.actionGroup.addAction(self.bo_TA_Action)
        self.actionGroup.addAction(self.hi_EG_Action)
        self.actionGroup.addAction(self.cu_PE_Action)
        self.writingSystemChangeMenu.addActions(
            [self.en_GB_Action, self.ru_RU_Action,
             self.zh_CN_Action, self.ko_KR_Action,
             self.hi_IN_Action, self.ar_EG_Action,
             self.gez_ET_Action, self.km_KH_Action,
             self.yi_CN_Action, self.bo_TA_Action,
             self.hi_EG_Action, self.cu_PE_Action
             ]
            )
    def writingSystemChanged(self):
        self.edit.writingSystem = self.sender().data()
        self.edit.changeWritingSystem()
    

class TextEdit(QTextEdit):

    def __init__(self, window, parent=None):
        super().__init__(parent)

        self._window = window

        self.writingSystem = en_GB

        self.initKeyboard()

        self.chamo_keys = chamo_dict.dic.keys()

        self.listwidget = HandmadeIMEListWidget(self)

        self.hangulIsEditting = False
        self.hangulPosition = -1

        self.currentCharFormatChanged.connect(
            lambda charFormat:
            self.document().setDefaultFont(charFormat.font())
            )

        self.isEditLock = False
        self.start_pos = 0
        self.end_pos = 0

        self.kantaiji_dic = kantaiji_dict.dic
        self.kantaiji_keys = self.kantaiji_dic.keys()
        

    def insertHangul(self, tc, event):

        tc.movePosition(PreviousCharacter, KeepAnchor, 2)
        t = tc.selectedText()
        text = chamo_dict.dic[t]

        if text != -1:
            tc.insertText(text)

        return self.checkHangul(tc, event)

    def hangulUpdate(self, tc, event):

        if self.checkHangul(tc, event):

                extraSelection = QTextEdit.ExtraSelection()
                extraSelection.cursor = QTextCursor(self.textCursor())
                extraSelection.cursor.movePosition(
                    PreviousCharacter, KeepAnchor, 1
                    )
                extraSelection.format = QTextCharFormat()
                extraSelection.format.setFontUnderline(True)
                extraSelection.format.setUnderlineStyle(DotLine)
                self.setExtraSelections([extraSelection])
        
        
    def checkHangul(self, tc, event):
        tc = QTextCursor(tc)
        tc.movePosition(PreviousCharacter, KeepAnchor, 1)
        t = tc.selectedText()[0]
        if ord(chr(0x0AC00)) <= ord(t) <= ord(chr(0x0D7A3)):
            return True
        if ord(chr(0x01100)) <= ord(t) <= ord(chr(0x011FF)):
            return True
        if ord(chr(0x03131)) <= ord(t) <= ord(chr(0x031BE)):
            return True

        return False

    def tc_back(self, tc, num=3):
        tc.movePosition(PreviousCharacter, KeepAnchor, num)
        st = tc.selectedText()
        for k in self.insert_dic_keys:
            match = k.match(st)
            if match:
                self.listwidget.clear()
                values = self.insert_dic[k]
                self.listwidget.addItems(values)
                self.henkan_num = len(match.string)
                self.listwidget.setCurrentRow(0)
                self.listwidget.show()
                return True
        return False


    def checkBopomofoCount(self, tc):

        other = QTextCursor(tc)
        other.movePosition(PreviousCharacter, KeepAnchor, 4)

        count = 0
        for i in other.selectedText():
            if i in BopomofoAllLists:
                count += 1

        return count

    def setBopomofoList(self, tc, op=4):

        other = QTextCursor(tc)
        other.movePosition(PreviousCharacter, KeepAnchor, op)
        selectedText = other.selectedText()
        data = os.path.join(os.getcwd(), "dicts\\bopomofo.sqlite3")

        with sqlite3.connect(data) as con:
            cur = con.cursor()

            cur.execute(
                "SELECT DATA FROM BOPOMOFO WHERE NAME =?", (selectedText, )
                )

            fetchone = cur.fetchone()
            if fetchone:
                qb = QByteArray(fetchone[0])
                out = QDataStream(qb, QIODevice.ReadOnly)
                kanjis_str = out.readQStringList()
                original_kanjis_str = list(kanjis_str)
                if original_kanjis_str:
                    self.listwidget.count_stop = len(kanjis_str)
                    itemCount = len(kanjis_str)%9
                    if itemCount != 0:
                        for i in range(9-itemCount):
                            kanjis_str.append("")

                    self.listwidget.items = [
                        QListWidgetItem() for i in range(0, len(kanjis_str))
                        ]

                    for num, kanji in enumerate(kanjis_str):
                        itemNum = num%9 + 1
                        if kanji:
                            self.listwidget.items[
                                num
                                ].setText(
                                    str(itemNum) + kanji
                                    )
                        else:
                            self.listwidget.items[
                                num
                                ].setText(kanji)
                    firstText = self.listwidget.items[0].text()
                    text = firstText[1:]
                    other.insertText(text)
                    otherCharFormat = other.charFormat()
                    other.movePosition(
                        PreviousCharacter, KeepAnchor
                        )
                    otherCharFormat.setProperty(
                        BopomofoListProperty,
                        original_kanjis_str
                        )
                    other.setCharFormat(otherCharFormat)
                    self.end_pos = tc.position()
                    self.extraSelectionsUpdate()
                    return False
        return True
        
    def extraSelectionsUpdate(self):
        self.setExtraSelections([])
        extra = QTextEdit.ExtraSelection()
        extra.cursor = QTextCursor(self.document())
        extra.cursor.setPosition(self.start_pos)
        extra.cursor.setPosition(self.end_pos, KeepAnchor)
        extra.format = QTextCharFormat()
        extra.format.setFontUnderline(True)
        extra.format.setUnderlineStyle(DashDotLine)
        self.setExtraSelections([extra])

    def get_text(self):

        if self.writingSystem != zh_CN:
            return

        text = self.listwidget.currentItem().text()
        text = text[1:]

        tc = self.textCursor()
        tc.setPosition(self.start_pos)
        tc.movePosition(
                        NextCharacter,
                        KeepAnchor,
                        len(self.split_text[0] + 1)
                        )
        tc.insertText(text)
        self.isPinyinEditting = 1
        self.start_pos = tc.position()

        if self.split_text:
            self.split_text= self.split_text[1:]
        else:
            self.listwidget.setHidden(True)

        if self.listwidget.isVisible():
            if self.split_text == [""] or not self.split_text:
                self.listwidget.setHidden(True)

        self.extraSelectionsUpdate()

    def padding(self):
        count = len(self.henkan_after_list)%9
        if count:
            for i in range(9-count, 0, -1):
                self.henkan_after_list.append("")
                
                
    def re_search(self):

        tc = self.textCursor()
        if not self.isPinyinEditting:
            self.start_pos = tc.position() -1
            self.isPinyinEditting = 1

        self.end_pos = tc.position()
        tc.setPosition(self.start_pos)
        tc.movePosition(
            NextCharacter, KeepAnchor,
            self.end_pos - self.start_pos
            )
        alphabet = re.compile("[*]", re.MULTILINE)
        self.split_text = alphabet.split(tc.selectedText())
        text = self.split_text[0] + "*"

        for i in self.kantaiji_keys:
            if i.match(text):
                kanjis = self.kantaiji_dic[i]
                self.henkan_after_list = list(kanjis)

        self.extraSelectionsUpdate()
        self.padding()
        self.listwidget.items = [
            QListWidgetItem() for i in range(
                0,
                len(self.henkan_after_list))
            ]
        for l, kanji in enumerate(self.henkan_after_list):

            if kanji:
                self.listwidget.items[l].setText(str(l%9+1)+kanji)
            else:
                self.listwidget.items[l].setText(kanji)

        for number, kantaiji in enumerate(
                                self.listwidget.items
                                ):
            self.listwidget.insertItem(number, kantaiji)

            if self.isPinyinEditting:

                if not self.listwidget.isVisible():
                    self.listwidget.setCurrentRow(0)
                    self.listwidget.show()
                    
                        
        
        
            

    def keyPressEvent(self, event):

        if self.keyDicts[event.key()] != -1:
            self.keyDicts[event.key()].setFlat(True)

        tc = self.textCursor()

        if not self.listwidget.isVisible():
            
            
            if event.key() in (Qt.Key_Return, Qt.Key_Backspace,
                               Qt.Key_Delete, Qt.Key_Up,
                               Qt.Key_Down,   Qt.Key_Left, Qt.Key_Right):

                if self.writingSystem == ko_KR:
                    if event.key() == Qt.Key_Backspace:
                    
                        if self.hangulIsEditting:
                            self.hangulPosition = tc.position()
                            if hangul_repair.repair(self, tc, event):
                                self.hangulUpdate(tc, event)
                                return

                    elif event.key() == Qt.Key_Delete:
                        return super().keyPressEvent(event)

                    else:
                        self.setExtraSelections([])
                        return super().keyPressEvent(event)

                elif self.writingSystem != bo_TA:
                    return super().keyPressEvent(event)
                
                    

                return super().keyPressEvent(event)
                    

            

        if self.writingSystem == yi_CN:
            yi_method.proxy_keyPressEvent(self, event)
            return

        elif self.writingSystem == bo_TA:
            
            bopomofo_method.proxy_keyPressEvent(self, event)
            return

        elif self.writingSystem == zh_CN:
           
            kantaiji_method.proxy_keyPressEvent(self, event)
            return
                

        if event.keyCombination() in SK and self.keyDicts[event.key()] != -1:
            tc.insertText(self.keyDicts[event.key()].underRight)

        elif event.key() in SE and self.keyDicts[event.key()] != -1:
            tc.insertText(self.keyDicts[event.key()].underRight)

        elif self.keyDicts[event.key()] != -1:
            tc.insertText(self.keyDicts[event.key()].underLeft)

        
        if self.writingSystem == ko_KR:
            self.setExtraSelections([])
            if self.keyDicts[event.key()] != -1:
                
                self.hangulIsEditting = self.insertHangul(tc, event)
                self.hangulUpdate(tc,event)
            return

            
        
                
        return

    def keyReleaseEvent(self, event):


        if self.keyDicts[event.key()] != -1:
            self.keyDicts[event.key()].setFlat(False)

        if event.key() == Qt.Key_Backspace:
            if self.writingSystem == ko_KR:
                tc = self.textCursor()
                self.hangulIsEditting = (tc.position()
                                         ==
                                         self.hangulPosition)
                
            

        return super().keyReleaseEvent(event)

    def initKeyboard(self):
        

        self.Key_Escape = KeyboardPushButton(objectName = KEY_ESCAPE)
        self.Key_F1 = KeyboardPushButton(objectName=KEY_F1)
        self.Key_F2 = KeyboardPushButton(objectName=KEY_F2)
        self.Key_F3 = KeyboardPushButton(objectName=KEY_F3)
        self.Key_F4 = KeyboardPushButton(objectName=KEY_F4)
        self.Key_F5 = KeyboardPushButton(objectName=KEY_F5)
        self.Key_F6 = KeyboardPushButton(objectName=KEY_F6)
        self.Key_F7 = KeyboardPushButton(objectName=KEY_F7)
        self.Key_F8 = KeyboardPushButton(objectName=KEY_F8)
        self.Key_F9 = KeyboardPushButton(objectName=KEY_F9)
        self.Key_F10 = KeyboardPushButton(objectName=KEY_F10)
        self.Key_F11 = KeyboardPushButton(objectName=KEY_F11)
        self.Key_F12 = KeyboardPushButton(objectName=KEY_F12)
        
        
        self.Key_1 = KeyboardPushButton(objectName=KEY_1)
        self.Key_2 = KeyboardPushButton(objectName=KEY_2)
        self.Key_3 = KeyboardPushButton(objectName=KEY_3)
        self.Key_4 = KeyboardPushButton(objectName=KEY_4)
        self.Key_5 = KeyboardPushButton(objectName=KEY_5)
        self.Key_6 = KeyboardPushButton(objectName=KEY_6)
        self.Key_7 = KeyboardPushButton(objectName=KEY_7)
        self.Key_8 = KeyboardPushButton(objectName=KEY_8)
        self.Key_9 = KeyboardPushButton(objectName=KEY_9)
        self.Key_0 = KeyboardPushButton(objectName=KEY_0)
        

        self.Key_A = KeyboardPushButton(objectName=KEY_A)

        self.Key_B = KeyboardPushButton(objectName=KEY_B)
        self.Key_C = KeyboardPushButton(objectName=KEY_C)
        self.Key_D = KeyboardPushButton(objectName=KEY_D)
        self.Key_E = KeyboardPushButton(objectName=KEY_E)
        self.Key_F = KeyboardPushButton(objectName=KEY_F)
        self.Key_G = KeyboardPushButton(objectName=KEY_G)
        self.Key_H = KeyboardPushButton(objectName=KEY_H)
        self.Key_I = KeyboardPushButton(objectName=KEY_I)
        self.Key_J = KeyboardPushButton(objectName=KEY_J)
        self.Key_K = KeyboardPushButton(objectName=KEY_K)
        self.Key_L = KeyboardPushButton(objectName=KEY_L)
        self.Key_M = KeyboardPushButton(objectName=KEY_M)
        self.Key_N = KeyboardPushButton(objectName=KEY_N)
        self.Key_O = KeyboardPushButton(objectName=KEY_O)
        self.Key_P = KeyboardPushButton(objectName=KEY_P)
        self.Key_Q = KeyboardPushButton(objectName=KEY_Q)
        self.Key_R = KeyboardPushButton(objectName=KEY_R)
        self.Key_S = KeyboardPushButton(objectName=KEY_S)
        self.Key_T = KeyboardPushButton(objectName=KEY_T)
        self.Key_U = KeyboardPushButton(objectName=KEY_U)
        self.Key_V = KeyboardPushButton(objectName=KEY_V)
        self.Key_W = KeyboardPushButton(objectName=KEY_W)
        self.Key_X = KeyboardPushButton(objectName=KEY_X)
        self.Key_Y = KeyboardPushButton(objectName=KEY_Y)
        self.Key_Z = KeyboardPushButton(objectName=KEY_Z)


        self.Key_IME = KeyboardPushButton(objectName=KEY_IME)
        self.Key_Tab = KeyboardPushButton(objectName=KEY_TAB)
        
        self.Key_CapsLock = KeyboardPushButton(objectName=KEY_CAPSLOCK)
        self.Key_LeftShift = KeyboardPushButton(objectName=KEY_LEFTSHIFT)
        self.Key_LeftControl  = KeyboardPushButton(objectName=KEY_LEFTCONTROL)
        self.Key_WindowMark = KeyboardPushButton(objectName=KEY_WINDOW)
        self.Key_LeftAlt = KeyboardPushButton(objectName=KEY_LEFTALT)
        self.Key_NoConversion = KeyboardPushButton(objectName=KEY_NOCONVERSION)
        self.Key_Space = KeyboardPushButton(objectName=KEY_SPACE)
        self.Key_Conversion = KeyboardPushButton(objectName=KEY_CONVERSION)
        self.Key_Katakana = KeyboardPushButton(objectName=KEY_KATAKANA)
        self.Key_RightAlt = KeyboardPushButton(objectName=KEY_RIGHTALT)
        self.Key_Menu = KeyboardPushButton(objectName=KEY_TOOL)
        
        
        self.Key_RightCtrl = KeyboardPushButton(objectName=KEY_RIGHTCONTROL)
        

        self.Key_Enter = KeyboardPushButton(objectName=KEY_ENTER)
        self.Key_Colon = KeyboardPushButton(objectName=KEY_COLON)
        self.Key_Semicolon = KeyboardPushButton(objectName=KEY_SEMICOLON)
        self.Key_At = KeyboardPushButton(objectName=KEY_AT)
        self.Key_Comma = KeyboardPushButton(objectName=KEY_COMMA)
        self.Key_Period = KeyboardPushButton(objectName=KEY_PERIOD)
        self.Key_Slash = KeyboardPushButton(objectName=KEY_SLASH)
        self.Key_Backslash = KeyboardPushButton(objectName=KEY_BACKSLASH)
        self.Key_BracketLeft = KeyboardPushButton(objectName=KEY_BRACKETLEFT)
        self.Key_BracketRight = KeyboardPushButton(objectName=KEY_BRACKETRIGHT)
        self.Key_Minus = KeyboardPushButton(objectName=KEY_MINUS)
        self.Key_AsciiCircum = KeyboardPushButton(objectName=KEY_CIRCUMFLEX)
        self.Key_Bar = KeyboardPushButton(objectName=KEY_BAR)
        self.Key_BackSpace = KeyboardPushButton(objectName=KEY_BACKSPACE)
       
        self.Key_RightShift = KeyboardPushButton(objectName=KEY_RIGHTSHIFT)
   
        
        self.keyDicts = KeyDict({Qt.Key_F1:self.Key_F1, Qt.Key_F2:self.Key_F2, Qt.Key_F3: self.Key_F3, Qt.Key_F4: self.Key_F4, Qt.Key_F5: self.Key_F5, Qt.Key_F6: self.Key_F6, Qt.Key_F7: self.Key_F7, Qt.Key_F8: self.Key_F8, Qt.Key_F9: self.Key_F9, Qt.Key_F10: self.Key_F10, Qt.Key_F11: self.Key_F11, Qt.Key_F12: self.Key_F12,
                                 Qt.Key_1:self.Key_1, Qt.Key_2:self.Key_2, Qt.Key_3: self.Key_3, Qt.Key_4: self.Key_4, Qt.Key_5: self.Key_5, Qt.Key_6: self.Key_6, Qt.Key_7: self.Key_7, Qt.Key_8: self.Key_8, Qt.Key_9: self.Key_9, Qt.Key_0: self.Key_0,
                                 Qt.Key_A:self.Key_A, Qt.Key_B:self.Key_B, Qt.Key_C: self.Key_C, Qt.Key_D: self.Key_D, Qt.Key_E: self.Key_E, Qt.Key_F: self.Key_F, Qt.Key_G: self.Key_G, Qt.Key_H: self.Key_H, Qt.Key_I: self.Key_I, Qt.Key_J: self.Key_J, Qt.Key_K: self.Key_K, Qt.Key_L: self.Key_L, Qt.Key_M:self.Key_M,
                                 Qt.Key_N:self.Key_N, Qt.Key_O:self.Key_O, Qt.Key_P: self.Key_P, Qt.Key_Q: self.Key_Q, Qt.Key_R: self.Key_R, Qt.Key_S: self.Key_S, Qt.Key_T: self.Key_T, Qt.Key_U: self.Key_U, Qt.Key_V: self.Key_V, Qt.Key_W: self.Key_W, Qt.Key_X: self.Key_X, Qt.Key_Y:self.Key_Y, Qt.Key_Z: self.Key_Z,
                                 Qt.Key_Minus: self.Key_Minus, Qt.Key_AsciiCircum: self.Key_AsciiCircum, Qt.Key_Bar: self.Key_Bar, Qt.Key_At: self.Key_At, Qt.Key_BracketLeft: self.Key_BracketLeft, Qt.Key_Semicolon: self.Key_Semicolon, Qt.Key_Colon: self.Key_Colon, Qt.Key_BracketRight: self.Key_BracketRight,
                                 Qt.Key_Comma: self.Key_Comma, Qt.Key_Period:self.Key_Period, Qt.Key_Slash: self.Key_Slash, Qt.Key_Backslash: self.Key_Backslash,
                                 Qt.Key_Space: self.Key_Space,
                                 Qt.Key_Exclam:self.Key_1, Qt.Key_QuoteDbl: self.Key_2,
                                 Qt.Key_NumberSign: self.Key_3, Qt.Key_Dollar: self.Key_4,
                                 Qt.Key_Percent: self.Key_5,
                                 Qt.Key_Ampersand: self.Key_6, Qt.Key_Apostrophe: self.Key_7,
                                 Qt.Key_ParenLeft: self.Key_8, Qt.Key_ParenRight: self.Key_9,
                                Qt.Key_AsciiTilde: self.Key_AsciiCircum, Qt.Key_Bar: self.Key_Backslash,
                                Qt.Key_Asterisk: self.Key_Colon, Qt.Key_BraceLeft: self.Key_BracketLeft,
                                Qt.Key_BraceRight: self.Key_BracketRight, Qt.Key_QuoteLeft: self.Key_At,
                                Qt.Key_AsciiTilde: self.Key_AsciiCircum,Qt.Key_Plus:self.Key_Semicolon,
                                Qt.Key_Question: self.Key_Slash, Qt.Key_Equal: self.Key_Minus,
                                Qt.Key_Underscore: self.Key_Backslash, Qt.Key_Less:self.Key_Comma,
                                 Qt.Key_Greater: self.Key_Period})
       
                                       



        column = 0
        escapeSpacerItem = QSpacerItem(40, 40)
        f4SpacerItem = QSpacerItem(20, 40)
        f8SpacerItem = QSpacerItem(20, 40)
        
        self.functionLineKeyboardHBoxLayout = QHBoxLayout()
 
        self.functionLineKeyboardHBoxLayout.addWidget(self.Key_Escape )
        self.functionLineKeyboardHBoxLayout.addItem(escapeSpacerItem)
        self.functionLineKeyboardHBoxLayout.addWidget(self.Key_F1)
        self.functionLineKeyboardHBoxLayout.addWidget(self.Key_F2)
        self.functionLineKeyboardHBoxLayout.addWidget(self.Key_F3)
        self.functionLineKeyboardHBoxLayout.addWidget(self.Key_F4)
        self.functionLineKeyboardHBoxLayout.addItem(f4SpacerItem)
        self.functionLineKeyboardHBoxLayout.addWidget(self.Key_F5)
        self.functionLineKeyboardHBoxLayout.addWidget(self.Key_F6)
        self.functionLineKeyboardHBoxLayout.addWidget(self.Key_F7)
        self.functionLineKeyboardHBoxLayout.addWidget(self.Key_F8)
        self.functionLineKeyboardHBoxLayout.addItem(f8SpacerItem)
        self.functionLineKeyboardHBoxLayout.addWidget(self.Key_F9)
        self.functionLineKeyboardHBoxLayout.addWidget(self.Key_F10)
        self.functionLineKeyboardHBoxLayout.addWidget(self.Key_F11)
        self.functionLineKeyboardHBoxLayout.addWidget(self.Key_F12)
        
        self.numberLineKeyboardHBoxLayout = QHBoxLayout()
        self.numberLineKeyboardHBoxLayout.addWidget(self.Key_IME)
        self.numberLineKeyboardHBoxLayout.addWidget(self.Key_1)
        self.numberLineKeyboardHBoxLayout.addWidget(self.Key_2)
        self.numberLineKeyboardHBoxLayout.addWidget(self.Key_3)
        self.numberLineKeyboardHBoxLayout.addWidget(self.Key_4)
        self.numberLineKeyboardHBoxLayout.addWidget(self.Key_5)
        self.numberLineKeyboardHBoxLayout.addWidget(self.Key_6)
        self.numberLineKeyboardHBoxLayout.addWidget(self.Key_7)
        self.numberLineKeyboardHBoxLayout.addWidget(self.Key_8)
        self.numberLineKeyboardHBoxLayout.addWidget(self.Key_9)
        self.numberLineKeyboardHBoxLayout.addWidget(self.Key_0)
        self.numberLineKeyboardHBoxLayout.addWidget(self.Key_Minus)
        self.numberLineKeyboardHBoxLayout.addWidget(self.Key_AsciiCircum)
        self.numberLineKeyboardHBoxLayout.addWidget(self.Key_Bar)

        

        self.tabAndCapsLockKeyboardVBoxLayout = QVBoxLayout()
        self.tabAndCapsLockKeyboardEnterHBoxLayout = QHBoxLayout()
        self.tabLineKeyboardHBoxLayout = QHBoxLayout()
        
        self.tabLineKeyboardHBoxLayout.addWidget(self.Key_Tab)
        self.tabLineKeyboardHBoxLayout.addWidget(self.Key_Q)
        self.tabLineKeyboardHBoxLayout.addWidget(self.Key_W)
        self.tabLineKeyboardHBoxLayout.addWidget(self.Key_E)
        self.tabLineKeyboardHBoxLayout.addWidget(self.Key_R)
        self.tabLineKeyboardHBoxLayout.addWidget(self.Key_T)
        self.tabLineKeyboardHBoxLayout.addWidget(self.Key_Y)
        self.tabLineKeyboardHBoxLayout.addWidget(self.Key_U)
        self.tabLineKeyboardHBoxLayout.addWidget(self.Key_I)
        self.tabLineKeyboardHBoxLayout.addWidget(self.Key_O)
        self.tabLineKeyboardHBoxLayout.addWidget(self.Key_P)
        self.tabLineKeyboardHBoxLayout.addWidget(self.Key_At)
        self.tabLineKeyboardHBoxLayout.addWidget(self.Key_BracketLeft)
        

        self.capsLockLineKeyboardHBoxLayout = QHBoxLayout()
        self.capsLockLineKeyboardHBoxLayout.addWidget(self.Key_CapsLock) 
        self.capsLockLineKeyboardHBoxLayout.addWidget(self.Key_A)
        self.capsLockLineKeyboardHBoxLayout.addWidget(self.Key_S)
        self.capsLockLineKeyboardHBoxLayout.addWidget(self.Key_D)
        self.capsLockLineKeyboardHBoxLayout.addWidget(self.Key_F)
        self.capsLockLineKeyboardHBoxLayout.addWidget(self.Key_G)
        self.capsLockLineKeyboardHBoxLayout.addWidget(self.Key_H)
        self.capsLockLineKeyboardHBoxLayout.addWidget(self.Key_J)
        self.capsLockLineKeyboardHBoxLayout.addWidget(self.Key_K)
        self.capsLockLineKeyboardHBoxLayout.addWidget(self.Key_L)
        self.capsLockLineKeyboardHBoxLayout.addWidget(self.Key_Semicolon)
        self.capsLockLineKeyboardHBoxLayout.addWidget(self.Key_Colon)
        self.capsLockLineKeyboardHBoxLayout.addWidget(self.Key_BracketRight)

        self.shiftLineKeyboardHBoxLayout = QHBoxLayout()
        self.shiftLineKeyboardHBoxLayout.addWidget(self.Key_LeftShift)
        self.shiftLineKeyboardHBoxLayout.addWidget(self.Key_Z)
        self.shiftLineKeyboardHBoxLayout.addWidget(self.Key_X)
        self.shiftLineKeyboardHBoxLayout.addWidget(self.Key_C)
        self.shiftLineKeyboardHBoxLayout.addWidget(self.Key_V)
        self.shiftLineKeyboardHBoxLayout.addWidget(self.Key_B)
        self.shiftLineKeyboardHBoxLayout.addWidget(self.Key_N)
        self.shiftLineKeyboardHBoxLayout.addWidget(self.Key_M)
        self.shiftLineKeyboardHBoxLayout.addWidget(self.Key_Comma)
        self.shiftLineKeyboardHBoxLayout.addWidget(self.Key_Period)
        self.shiftLineKeyboardHBoxLayout.addWidget(self.Key_Slash)
        self.shiftLineKeyboardHBoxLayout.addWidget(self.Key_Backslash)


        self.ctrlLineKeyboardHBoxLayout = QHBoxLayout()
        self.ctrlLineKeyboardHBoxLayout.addWidget(self.Key_LeftControl)
        self.ctrlLineKeyboardHBoxLayout.addWidget(self.Key_WindowMark)
        self.ctrlLineKeyboardHBoxLayout.addWidget(self.Key_LeftAlt)
        self.ctrlLineKeyboardHBoxLayout.addWidget(self.Key_NoConversion)
        self.ctrlLineKeyboardHBoxLayout.addWidget(self.Key_Space)
        self.ctrlLineKeyboardHBoxLayout.addWidget(self.Key_Conversion)
        self.ctrlLineKeyboardHBoxLayout.addWidget(self.Key_Katakana)
        self.ctrlLineKeyboardHBoxLayout.addWidget(self.Key_RightAlt)
        self.ctrlLineKeyboardHBoxLayout.addWidget(self.Key_Menu)
        self.ctrlLineKeyboardHBoxLayout.addWidget(self.Key_RightCtrl)
   
    
        vSpacerItem =  QSpacerItem(500, 20)
        
        self.keyboardVBoxLayout = QVBoxLayout()
        
        self.keyboardVBoxLayout.addLayout(self.functionLineKeyboardHBoxLayout)
        self.keyboardVBoxLayout.addItem(vSpacerItem)
        self.keyboardVBoxLayout.addLayout(self.numberLineKeyboardHBoxLayout)
        
        self.tabAndCapsLockKeyboardVBoxLayout.addLayout(self.tabLineKeyboardHBoxLayout)
        self.tabAndCapsLockKeyboardVBoxLayout.addLayout(self.capsLockLineKeyboardHBoxLayout)
        self.tabAndCapsLockKeyboardEnterHBoxLayout.addLayout(self.tabAndCapsLockKeyboardVBoxLayout, 90)
        self.tabAndCapsLockKeyboardEnterHBoxLayout.addWidget(self.Key_Enter, 10)
        self.tabAndCapsLockKeyboardEnterHBoxLayout.setSpacing(1)

        self.keyboardVBoxLayout.addLayout(self.tabAndCapsLockKeyboardEnterHBoxLayout)
        self.keyboardVBoxLayout.addLayout(self.shiftLineKeyboardHBoxLayout)
        self.keyboardVBoxLayout.addLayout(self.ctrlLineKeyboardHBoxLayout)
        self.keyboardVBoxLayout.setSpacing(1)

        self.keyboardWidget = QWidget()
        self.keyboardWidget.setLayout(self.keyboardVBoxLayout)
        self._window.keyboardDockWidget.setWidget(self.keyboardWidget)        
        
        self.changeWritingSystem()

    def window(self):
        return self._window

    def changeWritingSystem(self):

        if self.writingSystem == ko_KR:
            self.document().setDefaultFont(QFont("Malgun Gothic", 18))

        elif self.writingSystem == yi_CN:
            self.document().setDefaultFont(QFont('Microsoft Yi Baiti', 12))
            self.font_metrics = QFontMetrics(self.listwidget.font())
            self.insert_dic = KeyDict()
            self.insert_dic += yi_dict.dic
            self.insert_dic_keys = self.insert_dic.keys()
            self.listwidget.setWritingSystem(yi_CN)
            tc = self.textCursor()
            char = tc.charFormat()
            font = QFont('Microsoft Yi Baiti', 12)
            char.setFont(font)
            tc.setCharFormat(char)
            self.setTextCursor(tc)

        elif self.writingSystem == bo_TA:
            self.document().setDefaultFont(QFont("游明朝", 18))
            self.listwidget.setWritingSystem(bo_TA)

        elif self.writingSystem == zh_CN:
            self.document().setDefaultFont(QFont("游明朝", 18))
            self.isPinyinEditting = 0
            self.split_text = []
            self.henkan_after_list = []
            self.listwidget.items = []
            self.listwidget_font = QFont('游明朝', 20)
            self.henkan_num = 0
            self.start_pos = 0
            self.end_pos = 0
            self.font_metrics = QFontMetrics(self.listwidget.font())
            self.listwidget.setWritingSystem(zh_CN)
            
            

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        
        db_path = os.path.join(
                BASE_DIR, "keyboard_factory_db\\keyboard_mapper.sqlite3"
                )
    
        with sqlite3.connect(db_path) as con:
        
            cur = con.cursor()
            cur.execute(f"SELECT * FROM {self.writingSystem}")
            dic = {}
            data = cur.fetchall()
            for key in data:
                dic[key[0]] = key
                button = self._window.keyboardDockWidget.widget().findChild(
                    QPushButton, key[KEYNAMETEXT]
                    )

                if button:
                    button.setKeys(key)
                    button.setText(dic[button.objectName()][DISPLAYTEXT])
                    


def main():

    app = (QApplication([])
           if QApplication.instance() is None
           else
           QApplication.instance())

    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
