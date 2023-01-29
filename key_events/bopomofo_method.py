# -*- coding: utf-8 -*-
from PySide6.QtCore import Qt, QDataStream
from PySide6.QtGui import QFontMetrics, QTextCursor, QTextCharFormat
from PySide6.QtWidgets import QListWidgetItem, QPlainTextEdit, QTextEdit, QLineEdit, QListWidget
from keyboard_factory_db.commonnames import *
import re, os
import sqlite3


def proxy_keyPressEvent(self, event):
    tc = self.textCursor()
    out = QDataStream()
    tc = self.textCursor()

    if event.key() in NonCharKeys:
        return
 
    if event.keyCombination() in SK:

        tc.insertText(self.keyDicts[event.key()].underRight if self.keyDicts[event.key()] != -1 else "")
        
    elif event.key() in SE:
        
        tc.insertText(self.keyDicts[SETK[event.key()]].underRight if self.keyDicts[SETK[event.key()]] != -1 else "")
        
    else:
        
        if event.key() == Qt.Key_Return:
            if self.listwidget.isEdittingBopomofo:
                
                
                tc = self.textCursor()
                other = QTextCursor(tc)
                other.setPosition(self.start_pos)
                other.setPosition(self.end_pos, KeepAnchor)
                
                for i in other.selectedText():
                    #編集対象の中に、未変換のボポモフォがあれば受け付けないことにする
                    if i in BopomofoAllLists:
                        return
                self.listwidget.isEdittingBopomofo = False
                self.listwidget.setHidden(True)
                tc.setPosition(self.start_pos)
                tc.setPosition(self.end_pos, KeepAnchor)
                charFormat = tc.charFormat()
                charFormat.clearProperty(BopomofoListProperty)
                tc.setCharFormat(charFormat)
                self.setExtraSelections([])
                return
            
            else:
                
                return QTextEdit.keyPressEvent(self, event)

            

        elif event.key() == Qt.Key_Left:
            if self.listwidget.isVisible():
                d = self.textCursor()
                d.movePosition(Left, MoveAnchor)
                if d.position() >= self.start_pos and not self.listwidget.isVisible():
                    self.setTextCursor(d)
                    return
            
            return QTextEdit.keyPressEvent(self, event)
        elif event.key() == Qt.Key_Right:
            if self.listwidget.isVisible():
                d = self.textCursor()
                d.movePosition(Right, MoveAnchor)
                if d.position() <= self.end_pos and not self.listwidget.isVisible():
                    self.setTextCursor(d)
                    return
            return QTextEdit.keyPressEvent(self, event)

        
        elif event.key() in (Qt.Key_Backspace, Qt.Key_Delete, Qt.Key_Up, Qt.Key_Down):
            
            if event.key() == Qt.Key_Backspace:
                if self.listwidget.isEdittingBopomofo:
                    tc = self.textCursor()
                    if tc.position() > self.start_pos:
                        self.end_pos -= 1
                        self.extraSelectionsUpdate()
                        self.isEditLock = False
                        return QTextEdit.keyPressEvent(self, event)
                    return 
                else:
                    self.isEditLock = False
                    self.extraSelectionsUpdate()
                    return QTextEdit.keyPressEvent(self, event)
                
            elif event.key() == Qt.Key_Delete:
                if self.listwidget.isEdittingBopomofo:
                    self.isEditLock = False
                    tc = self.textCursor()
                    if tc.position() < self.end_pos:
                        self.end_pos -= 1
                        self.extraSelectionsUpdate()
                        return QTextEdit.keyPressEvent(self, event)
                    return         
            
            if event.key() == Qt.Key_Up:
                
                if not self.listwidget.isVisible():
                    tc = self.textCursor()                
                    tc.movePosition(Up, MoveAnchor)
                    self.setTextCursor(tc)
                    return False
                
                if self.listwidget.current_index%9 == 0 and self.listwidget.current_index >= 0:                
                    if self.listwidget.page > 0:
                        
                        self.listwidget.page -= 1
                    
                    self.listwidget.scrollToItem(self.listwidget.item(self.listwidget.current_index-9), QListWidget.ScrollHint.PositionAtTop)
                
                if self.listwidget.current_index > 0:
                    self.listwidget.current_index -= 1
                
                self.listwidget.setCurrentRow(self.listwidget.current_index)
                
                return False
            
            if event.key() == Qt.Key_Down:
      
                if self.listwidget.isHidden():
                    
                    tc = self.textCursor()
                    other = QTextCursor(tc)
              
                    other.movePosition(PreviousCharacter, KeepAnchor, 1)
                    if other.selectedText() in BopomofoAllLists:
                        #ボポモフォ文字が残っている場合には受け付けない
                        return
                    char = tc.charFormat()
                    self.listwidget.items.clear()
                    self.listwidget.clear()
                    kanjis_str = char.property(BopomofoListProperty)
                    if kanjis_str:
                        
                        self.listwidget.count_stop = len(kanjis_str)
                        itemCount = len(kanjis_str)%9
                        if itemCount != 0:                       
                            for i in range(9-itemCount):                                
                                kanjis_str.append("")
                                
                        self.listwidget.items = [QListWidgetItem() for i in range(0, len(kanjis_str))]
                        for num, kanji in enumerate(kanjis_str):
                            itemNum = num%9+1
                            if kanji:                                
                                self.listwidget.items[num].setText(str(itemNum)+kanji)
                            else:
                                self.listwidget.items[num].setText(kanji)
                                
                        for num, kanji in enumerate(self.listwidget.items):
                                self.listwidget.insertItem(num, kanji)
                        self.listwidget.setCurrentItem (self.listwidget.item (0))
                        self.listwidget.show()

                else:
                
                    if self.listwidget.isHidden() and not self.listwidget.isBopomofoEditting:
                        tc = self.textCursor()                
                        tc.movePosition(Down, MoveAnchor)
                        self.setTextCursor(tc)
                        return False
 
                    if self.listwidget.current_index < self.listwidget.count_stop-1:
                        self.listwidget.current_index += 1
                        
                    if self.listwidget.current_index%9 == 0 and self.listwidget.current_index != 0 and self.listwidget.current_index < self.listwidget.count_stop:      
                        
                        self.listwidget.page += 1
                        self.listwidget.scrollToItem(self.listwidget.item(self.listwidget.current_index), QListWidget.ScrollHint.PositionAtTop)
                        
            
       
                    self.listwidget.setCurrentRow(self.listwidget.current_index)
                    return False
                
            return QTextEdit.keyPressEvent(self, event)
        
        if not self.listwidget.isEdittingBopomofo:
            self.listwidget.isEdittingBopomofo = True
            self.start_pos = tc.position()
            
        if self.listwidget.isHidden():
            text = self.keyDicts[event.key()].underLeft
            
            if not self.isEditLock:
                other = QTextCursor(tc)
                op = self.checkBopomofoCount(tc)          

                #３文字のボポモフォの真ん中には決まった母音字が入る。
                #これら３文字は最後の母音にはならない。                

                if text not in BopomofoToneLists:
                    if op == 3:
                        
                        tc.movePosition(PreviousCharacter, KeepAnchor, op)
                        if text in BopomofoConsonantLists:
                            #子音字の場合は、一番最初の文字を置き換える
                            ot = QTextCursor(tc)
                            ot.setPosition(tc.position())
                            ot.insertText(text)
                            ot.deleteChar()
                            self.end_pos = max(ot.position(), self.end_pos)
                            self.extraSelectionsUpdate()
                            return
                        elif text in BopomofoMiddleVowelLists:
                            ot = QTextCursor(tc)
                            ot.setPosition(tc.position()+1)
                            ot.setPosition(tc.position()+2, KeepAnchor)
                            ot.insertText(text)
                            self.end_pos = max(ot.position(), self.end_pos)
                            self.extraSelectionsUpdate()
                            return
                        elif text in BopomofoThirdVowelLists:
                            #母音字の場合は、直前の文字を置き換える
                            ot = QTextCursor(tc)
                            ot.setPosition(tc.position()+2)
                            ot.setPosition(tc.position()+3, KeepAnchor)
                            ot.insertText(text)
                            self.end_pos = max(ot.position(), self.end_pos)
                            self.extraSelectionsUpdate()
                            return
                            
                            
                    elif op == 2:
                        tc.movePosition(PreviousCharacter, KeepAnchor, op)
                        if tc.selectedText()[0] in BopomofoVowelLists:
                            #母音字が先頭にある場合は２連続では続かない
                            #また、母音＋子音という組み合わせもない
                            return
                        if text in BopomofoConsonantLists:
                            #子音字の場合は、一番最初の文字を置き換える
                            ot = QTextCursor(tc)
                            ot.setPosition(tc.position())                    
                            ot.insertText(text)
                            ot.deleteChar()
                            self.end_pos = max(ot.position(), self.end_pos)
                            self.extraSelectionsUpdate()
                            return
                        elif text in BopomofoMiddleVowelLists:
                            ot = QTextCursor(tc)
                            ot.setPosition(tc.position())
                            ot.setPosition(tc.position()+1)
                            ot.setPosition(tc.position()+2, KeepAnchor)
                            ot.insertText(text)
                            self.end_pos = max(ot.position(), self.end_pos)
                            self.extraSelectionsUpdate()
                            return
                        elif text in BopomofoThirdVowelLists:
                            ot = QTextCursor(tc)
                            ot.setPosition(tc.position())
                            ot.setPosition(tc.position()+1)
                            ot.setPosition(tc.position()+2, MoveAnchor)
                            ot.insertText(text)
                            self.end_pos = max(ot.position(), self.end_pos)
                            self.extraSelectionsUpdate()                            
                            return
                        
                    elif op == 1:
                        tc.movePosition(PreviousCharacter, KeepAnchor, op)
                        if text in BopomofoConsonantLists:
                            #子音字の場合は、一番最初の文字を置き換える
                            #子音字が２つ連続することはないので、そのまま関数を終了する。
                            ot = QTextCursor(tc)
                            ot.setPosition(tc.position())
                            ot.insertText(text)
                            ot.deleteChar()
                            self.end_pos = max(ot.position(), self.end_pos)
                            self.extraSelectionsUpdate()
                            return
                        tc.clearSelection()
                        tc.movePosition(NextCharacter, MoveAnchor, 1)                

                checker = QTextCursor(tc)
                checker.movePosition(PreviousCharacter, KeepAnchor, 1)
                if text in BopomofoToneLists and checker.selectedText() in BopomofoToneLists:
                    return
            
                tc.insertText(text)
                
            op = self.checkBopomofoCount(tc)
            
            if text in BopomofoToneLists:
                
                
                other = QTextCursor(tc)
                other.movePosition(PreviousCharacter, KeepAnchor, op)
                data = os.path.join(os.getcwd(), "dicts\\bopomofo.sqlite3")
        
                with sqlite3.connect(data) as con:
                    cur = con.cursor()

                    cur.execute("SELECT DATA FROM BOPOMOFO WHERE NAME = ?", (other.selectedText(), ))
                    fetchone = cur.fetchone()
                    if fetchone is None:
                        self.isEditLock = True
                        
        if event.key() in (Qt.Key_1, Qt.Key_2, Qt.Key_3, Qt.Key_4, Qt.Key_5, Qt.Key_6, Qt.Key_7, Qt.Key_8, Qt.Key_9):  
            
            if self.listwidget.isVisible():                
                num = listNumberDic[event.key()]
                t = self.listwidget.items[num+9*self.listwidget.page].text()
                if not t:
                    return                    
                tc = self.textCursor()
                charFormat = tc.charFormat()
                tc.movePosition(PreviousCharacter, MoveAnchor, 1)        
                t = t.replace(str(num+1), "", 1)                    
                tc.insertText(t, charFormat)
                tc.deleteChar()           
                self.listwidget.setHidden(True)
                self.extraSelectionsUpdate()
                return
            
        if self.listwidget.isHidden():
            if self.listwidget.isEdittingBopomofo:
                self.end_pos = max(tc.position(), self.end_pos)
                
                self.setBopomofoList(tc, op)
                self.extraSelectionsUpdate() 
            
       
    

    
            
        
 
