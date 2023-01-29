# -*- coding: utf-8 -*-
from PySide6.QtCore import Qt
from PySide6.QtGui import QFontMetrics, QTextCursor, QTextCharFormat
from PySide6.QtWidgets import QListWidgetItem, QPlainTextEdit, QTextEdit, QLineEdit
from keyboard_factory_db.commonnames import *

import re
def proxy_keyPressEvent(self, event):

   
    tc = self.textCursor()
    
    if event.key() == Qt.Key_Return:
        if not self.listwidget.isVisible(): 
            tc.insertBlock()
            return False      
        else:
            currentitem = self.listwidget.currentItem()   
            if currentitem is None:
                return False
            text =  currentitem.text()            
            regex = re.compile(".*\w+$")
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
        tc.movePosition(Down, MoveAnchor, 1)
        self.setTextCursor(tc)
            
    elif event.key() == Qt.Key_Up:
        if self.listwidget.isVisible():
            row = self.listwidget.currentRow()
            if row > 0:
                self.listwidget.setCurrentRow(row-1)
            return False
        tc.movePosition(Up, MoveAnchor, 1)
        self.setTextCursor(tc)
    elif event.key() == Qt.Key_Right:
        if self.listwidget.isVisible():
            return False
        else:
            tc.movePosition(Right, MoveAnchor, 1)
            self.setTextCursor(tc)
            return True
    elif event.key() == Qt.Key_Left:
        if self.listwidget.isVisible():
            return False
        else:
            tc.movePosition(Left, MoveAnchor, 1)
            self.setTextCursor(tc)
            return True
    if event.key() in ( Qt.Key_B, Qt.Key_C, Qt.Key_D, Qt.Key_F,
                Qt.Key_G, Qt.Key_H, Qt.Key_J, Qt.Key_K, Qt.Key_L, Qt.Key_M,
                Qt.Key_N, Qt.Key_Q, Qt.Key_R, Qt.Key_S, 
                Qt.Key_V, Qt.Key_W,  Qt.Key_Y, Qt.Key_Z):
        
        QTextEdit.keyPressEvent(self, event)
        self.end_pos = tc.position()
        m = self.tc_back(tc, 4)
        if not m:
            tc.setPosition(self.end_pos, MoveAnchor)
            m = self.tc_back(tc, 3)  
            if not m:                    
                tc.setPosition(self.end_pos, MoveAnchor)
                m = self.tc_back(tc, 2)                    
                if not m:                        
                    tc.setPosition(self.end_pos, MoveAnchor)
                    m = self.tc_back(tc, 1)      
    
        return False
    
    if event.key() in (Qt.Key_A, Qt.Key_I, Qt.Key_U, Qt.Key_O, Qt.Key_E):
        QTextEdit.keyPressEvent(self, event)
        self.end_pos = tc.position()
        m = self.tc_back(tc, 4)
        if not m:
            tc.setPosition(self.end_pos, MoveAnchor)
            m = self.tc_back(tc, 3)  
            if not m:                    
                tc.setPosition(self.end_pos, MoveAnchor)
                m = self.tc_back(tc, 2)
                if not m:                        
                    tc.setPosition(self.end_pos, MoveAnchor)
                    m = self.tc_back(tc, 1)    

 
        
        return False
    
    elif event.key() == Qt.Key_P:
        tc.insertText("p")   
        self.end_pos = tc.position()
        m = self.tc_back(tc, 4)
        if not m:
            tc.setPosition(self.end_pos, MoveAnchor)
            m = self.tc_back(tc, 3) 
            if not m:                    
                tc.setPosition(self.end_pos, MoveAnchor)
                m = self.tc_back(tc, 2)
                if not m:
                    tc.setPosition(self.end_pos, MoveAnchor)
                    self.tc_back(tc, 1)
        
               
   
           
        return False
    
    elif event.key() == Qt.Key_T:
        tc.insertText("t")        
        self.end_pos = tc.position()
        m = self.tc_back(tc, 4)  
        if not m:
            tc.setPosition(self.end_pos, MoveAnchor)
            m = self.tc_back(tc, 3)
            if not m:
                tc.setPosition(self.end_pos, MoveAnchor)
                m = self.tc_back(tc, 2)     
                if not m:
                    tc.setPosition(self.end_pos, MoveAnchor)
                    self.tc_back(tc, 1)
   
        return False
    
    elif event.key() == Qt.Key_X:
        tc.insertText("x")
        self.end_pos = tc.position()
        m = self.tc_back(tc, 4)

        
        if not m:
            tc.setPosition(self.end_pos, MoveAnchor)
            m = self.tc_back(tc, 3)

            
            if not m:
                tc.setPosition(self.end_pos, MoveAnchor)
                m = self.tc_back(tc, 2)
                if not m:
                    tc.setPosition(self.end_pos, MoveAnchor)
                    self.tc_back(tc, 1)
                

        return False
    
    if event.key() in (Qt.Key_Backspace, Qt.Key_Delete):
        QTextEdit.keyPressEvent(self, event)
        self.end_pos = tc.position()
        m = self.tc_back(tc, 4)
        
        if not m:
            tc.setPosition(self.end_pos, MoveAnchor)
            m = self.tc_back(tc, 3)
            
            if not m:
                tc.setPosition(self.end_pos, MoveAnchor)
                m = self.tc_back(tc, 2)
                
                if not m:
                    tc.setPosition(self.end_pos, MoveAnchor)
                    m = self.tc_back(tc, 1)
                    if not m:
                        self.listwidget.clear()
                        self.listwidget.hide()

   
        return False        
