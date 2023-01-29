from PySide6.QtCore import Qt
from PySide6.QtGui import QFontMetrics, QTextCursor, QTextCharFormat
from PySide6.QtWidgets import QListWidgetItem, QPlainTextEdit, QTextEdit, QLineEdit
import re
from keyboard_factory_db.commonnames import *

def proxy_keyPressEvent(self, event):
    
        
    tc = self.textCursor()        
    if event.key() == Qt.Key_Return:
        if not self.listwidget.isVisible():  
            pass                
#            return False      
        else:
            text = self.listwidget.currentItem().text()                
            regex = re.compile("w+$")
            match = regex.match(text)
            if match is not None:
                text = text.replace(match.string, match.string[0])                
            tc.movePosition(PreviousCharacter, KeepAnchor, self.henkan_num)
            tc.insertText(text)
            self.listwidget.hide()
            self.listwidget.clear()
            return False
    if event.key() == Qt.Key_Down:

        if self.listwidget.isVisible():                
            row = self.listwidget.currentRow()
            if row < self.listwidget.count() -1:
                self.listwidget.setCurrentRow(row+1)
           
            return False
        else:
            return True
    elif event.key() == Qt.Key_Up:
        if self.listwidget.isVisible():
            row = self.listwidget.currentRow()
            if row > 0:
                self.listwidget.setCurrentRow(row-1)
            return False
        else:
            return True
    elif event.key() == Qt.Key_Right:
        if self.listwidget.isVisible():
            return False
        else:
            return True
    elif event.key() == Qt.Key_Left:
        if self.listwidget.isVisible():
            return False
        else:
            return True
    if event.key() in ( Qt.Key_A, Qt.Key_B, Qt.Key_C, Qt.Key_D, Qt.Key_E,  Qt.Key_F, Qt.Key_G, 
                Qt.Key_H, Qt.Key_I, Qt.Key_J, Qt.Key_K, Qt.Key_L, Qt.Key_Semicolon, Qt.Key_M,
                Qt.Key_N,  Qt.Key_O, Qt.Key_P, Qt.Key_At, 
                Qt.Key_Q, Qt.Key_R, Qt.Key_S, Qt.Key_T, Qt.Key_U,
                Qt.Key_V, Qt.Key_W, Qt.Key_X, Qt.Key_Y, Qt.Key_Z):
        
        if event.key() == Qt.Key_Semicolon:
            tc.insertText(self.keyDicts[event.key()].underLeft)
        elif event.key() == Qt.Key_At:
            tc.insertText(self.keyDicts[event.key()].underLeft)
        elif event.key() == Qt.Key_J:
       
            tc.insertText(self.keyDicts[event.key()].underLeft)
        else:
            QTextEdit.keyPressEvent(self, event)
        self.end_pos = tc.position()           
        m = self.tc_back(tc, 2)                    
        if not m:                        
            tc.setPosition(self.end_pos, MoveAnchor)
            m = self.tc_back(tc, 1)      
        if not m:
            self.listwidget.clear()
            self.listwidget.hide()
        return False        
    if event.key() in (Qt.Key_Backspace, Qt.Key_Delete):

        QTextEdit.keyPressEvent(self, event)
        self.end_pos = tc.position()            
        m = self.tc_back(tc, 2)   
        if not m:
            tc.setPosition(self.end_pos, MoveAnchor)
            m = self.tc_back(tc, 1)
        if not m:
            self.listwidget.clear()
            self.listwidget.hide()
   
        return False        
