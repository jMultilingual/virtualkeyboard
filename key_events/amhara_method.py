from PySide6.QtCore import Qt
from PySide6.QtGui import QFontMetrics, QTextCursor, QTextCharFormat
from PySide6.QtWidgets import QListWidgetItem, QPlainTextEdit, QTextEdit, QLineEdit

import sys
import os


from keyboard_factory_db.commonnames import *
import re

def proxy_keyPressEvent(self, event):
  
   
    tc = self.textCursor()            
  
    if (event.modifiers() & Qt.AltModifier) and (event.modifiers() & Qt.ShiftModifier):
        if event.key() in self.keyDicts:
            tc.insertText(self.keyDicts[event.key()].upperRight)
            self.end_pos = max(tc.position(), self.end_pos)
            return
    if (event.modifiers() & Qt.AltModifier):
        if event.key() in self.keyDicts:
            tc.insertText(self.keyDicts[event.key()].underLeft)
            self.end_pos = max(tc.position(), self.end_pos)
            return
        
    
    
    if event.modifiers() == Qt.KeyboardModifier.ShiftModifier and event.key() in self.keyDicts: 

        s_pos = tc.position()
        tc.movePosition(PreviousCharacter, KeepAnchor, 1)
        text = tc.selectedText() 
        if text == " ":
            #空白の場合はそのままスルー
            tc.clearSelection()
                        
        if event.key() == Qt.Key_A:
                                    
            if text in self.dict_a_keys:
                self.repairing_insertion(tc, self.dict_a[text])
            else:
                self.new_insertion(tc, self.keyDicts[event.key()].underRight, s_pos)
        
            return
        elif event.key() == Qt.Key_I:
              
            if text in self.dict_i_keys:                            
                self.repairing_insertion(tc, self.dict_i[text])    
            else:
                self.new_insertion(tc, self.keyDicts[event.key()].underRight, s_pos)
           
            return
        elif event.key() == Qt.Key_O:
                             
            if text in self.dict_o_keys:                            
                self.repairing_insertion(tc, self.dict_o[text])    
            else:
                self.new_insertion(tc, self.keyDicts[event.key()].underRight, s_pos)
           
            return
        elif event.key() == Qt.Key_U:
                             
            if text in self.dict_u_keys:                            
                self.repairing_insertion(tc, self.dict_u[text])    
            else:
                self.new_insertion(tc, self.keyDicts[event.key()].underRight, s_pos)
           
            return                        
        elif event.key() == Qt.Key_E:
            
            if text in self.dict_e_keys:
                self.repairing_insertion(tc, self.dict_e[text])
            else:
                self.new_insertion(tc, self.keyDicts[event.key()].underRight, s_pos)
                                       
            return
        elif event.key() == Qt.Key_H:
            
            if text in self.dict_h_keys:
                self.repairing_insertion(tc, self.amhara_hinsert_dict[text])
            else:
                self.new_insertion(tc, self.keyDicts[event.key()].underRight, s_pos)
            
        elif event.key() == Qt.Key_S:
            if text in self.dict_s_keys:
                self.repairing_insertion(tc, self.amhara_sinsert_dict[text])
            else:
                self.new_insertion(tc, self.keyDicts[event.key()].underRight, s_pos)
        else:
            self.new_insertion(tc, self.keyDicts[event.key()].underRight, s_pos)
        return            
    if event.key() in self.keyDicts:
        #まず、文字を入れる。入れこんだところが開始値となる        
        s_pos = tc.position()
        tc.movePosition(PreviousCharacter, KeepAnchor, 1)
        text = tc.selectedText() 
        if text == " ":
            #空白の場合はそのままスルー
            tc.clearSelection()
                        
        if event.key() == Qt.Key_A:
            self.sIsPushed = False
            self.hIsPushed = False
            if text in self.dict_a_keys:
                self.repairing_insertion(tc, self.dict_a[text])
            else:
                self.new_insertion(tc, self.keyDicts[event.key()].underLeft, s_pos)
            
            return
        elif event.key() == Qt.Key_I:
            self.sIsPushed = False
            self.hIsPushed = False
            if text in self.dict_i_keys:                            
                self.repairing_insertion(tc, self.dict_i[text])    
            else:
                self.new_insertion(tc, self.keyDicts[event.key()].underLeft, s_pos)
       
            return
        elif event.key() == Qt.Key_O:
            self.sIsPushed = False
            self.hIsPushed = False
            if text in self.dict_o_keys:                            
                self.repairing_insertion(tc, self.dict_o[text])    
            else:
                self.new_insertion(tc, self.keyDicts[event.key()].underLeft, s_pos)
         
            return
        elif event.key() == Qt.Key_U:
            self.sIsPushed = False
            self.hIsPushed = False
            if text in self.dict_u_keys:                            
                self.repairing_insertion(tc, self.dict_u[text])    
            else:
                self.new_insertion(tc, self.keyDicts[event.key()].underLeft, s_pos)
           
            return
            
        elif event.key() == Qt.Key_E:
            self.sIsPushed = False
            self.hIsPushed = False
            if text in self.dict_e_keys:
                self.repairing_insertion(tc, self.dict_e[text])
            else:
                self.new_insertion(tc, self.keyDicts[event.key()].underLeft, s_pos)
            
                
            return
        elif event.key() == Qt.Key_H:
            self.hIsPushed = True
            if not self.sIsPushed:
                
                if text in self.dict_h_keys:
                    self.repairing_insertion(tc, self.dict_h[text])
                else:
                    self.new_insertion(tc, self.keyDicts[event.key()].underLeft, s_pos)
                
            else:
                self.hIsPushed = False
                self.sIsPushed = False
                self.new_insertion(tc, self.keyDicts[event.key()].underLeft, s_pos)
           
        elif event.key() == Qt.Key_S:
            self.sIsPushed = True
            if not self.hIsPushed:
                if text in self.dict_s_keys:
                    self.repairing_insertion(tc, self.dict_s[text])
                else:
                    self.new_insertion(tc, self.keyDicts[event.key()].underLeft, s_pos)
            else:
                self.hIsPushed = False
                self.sIsPushed = False
                self.new_insertion(tc, self.keyDicts[event.key()].underLeft, s_pos)
        elif event.key() == Qt.Key_Y:
            if text in self.dict_y_keys:
                self.repairing_insertion(tc, self.dict_y[text])
            else:
                self.new_insertion(tc, self.keyDicts[event.key()].underLeft, s_pos)
                
        elif event.key() == Qt.Key_Colon:
            if text in self.dict_colon_keys:
                self.repairing_insertion(tc, self.dict_colon[text])
            else:
                self.new_insertion(tc, self.keyDicts[event.key()].underLeft, s_pos)
        elif event.key() == Qt.Key_Period:
            if text in self.dict_period_keys:
                self.repairing_insertion(tc, self.dict_period[text])
            else:
                self.new_insertion(tc, self.keyDicts[event.key()].underLeft, s_pos)
        else:
            self.sIsPushed = False
            self.hIsPushed = False
            self.new_insertion(tc, self.keyDicts[event.key()].underLeft, s_pos)
                        
