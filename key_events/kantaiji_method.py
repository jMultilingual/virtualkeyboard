from PySide6.QtCore import Qt
from PySide6.QtGui import QFontMetrics, QTextCursor, QTextCharFormat
from PySide6.QtWidgets import QListWidgetItem, QPlainTextEdit, QTextEdit, QListWidget
import sys


from keyboard_factory_db.commonnames import *
import re

def reInsert(self, tc, regex, text, selectedText):

    chang_ = re.compile(regex)
    if chang_.match(selectedText):            
        tc.deleteChar()
        tc.insertText(text)            
        self.re_search()
        
        return True
    return False




    
def proxy_keyPressEvent(self, event):

     
    tc = self.textCursor()
    if event.key() == Qt.Key_Return:        
        if self.listwidget.isVisible():           
            return False
        tc.insertBlock()
        return False
    
    if event.key() == Qt.Key_Space:
        if self.listwidget.isVisible():           
            return False
        tc.insertText(" ")
        return False
    
    if event.key() in (Qt.Key_1, Qt.Key_2, Qt.Key_3, Qt.Key_4, Qt.Key_5, Qt.Key_6, Qt.Key_7, Qt.Key_8, Qt.Key_9, Qt.Key_0):  
        if self.listwidget.isHidden():           
            text = event.text()
            tc = self.textCursor()                                 
            tc.insertText(f"{text}")
            self.setTextCursor(tc)          
            return False
        
        num = listNumberDic[event.key()]
        
        t = self.listwidget.items[num+9*self.listwidget.page].text()        
        
        except_number = re.compile("^\d+", re.I)
        except_number_text = except_number.split(t)[1]
        
        tc = self.textCursor()
        tc.setPosition(self.start_pos)        
        tc.movePosition(NextCharacter, KeepAnchor, len(self.split_text[0])+1)
 
        if self.listwidget.isVisible():
            if tc.selectedText():                
                if tc.selectedText()[-1] != "*":
                    tc.clearSelection()
                    tc = self.textCursor()
                    tc.setPosition(self.start_pos)
                    tc.movePosition(NextCharacter, KeepAnchor, len(self.split_text[0]))
                    char = tc.charFormat()
                    #ピンインから漢字を入れ込む処理
                    tc.insertText(except_number_text, char)
                else:
                    char = tc.charFormat()
                    tc.insertText(except_number_text, char)
                    
            if self.split_text == []:
                self.listwidget.close()                          
            elif self.split_text == [""]:
                self.listwidget.close()
                
        self.isPinyinEditting = 1        
        self.start_pos = tc.position() 
        self.split_text = self.split_text[1:]
        
        if not self.split_text:
            self.listwidget.close()     
            
        elif self.split_text == [""]:        
            self.listwidget.close()
            
        else:
            self.re_search()
   
          
        return
    
    elif event.key() == Qt.Key_Backspace:
        
        if self.listwidget.isHidden():
            
            return QTextEdit.keyPressEvent(self, event)
        
        if self.start_pos == self.textCursor().position()-1:
            self.listwidget.setHidden(True)
            self.isPinyinEditting = False
            self.split_text.clear()            
               
            return QTextEdit.keyPressEvent(self, event)
        
        alpha = re.compile("[a-z][^\x01-\x7E]")
        tc = self.textCursor()
        tc.movePosition(PreviousCharacter, KeepAnchor, 2)
        if alpha.match(tc.selectedText()):
            tc.deletePreviousChar()
            self.listwidget.setHidden(True)
            self.isPinyinEditting = False

            return False
        
        tc.clearSelection()
        alpha = re.compile("[^\x01-\x7E]")
        tc = self.textCursor()
        tc.movePosition(PreviousCharacter, KeepAnchor, 1)
        if alpha.match(tc.selectedText()):
            tc.deletePreviousChar()
            self.listwidget.setHidden(True)
            self.isPinyinEditting = False

            return False
        
        other_tc = self.textCursor()                   
        other_tc.movePosition(PreviousCharacter, KeepAnchor, 2)                      
        text =  other_tc.selectedText()
        if len(text) > 1:
            if "*" in text:
                other_tc.deleteChar()
                self.split_text = self.split_text[0:-1]                                                       
            else:
                other_tc = self.textCursor()
                other_tc.deletePreviousChar()
            self.re_search()
        else:
             other_tc = self.textCursor()                   
             other_tc.movePosition(PreviousCharacter, KeepAnchor, 1)                    
             other_tc = self.textCursor()
             other_tc.deletePreviousChar()                     
             
             self.listwidget.setHidden(True)
             self.isPinyinEditting = False
 
        if other_tc.position() < self.start_pos:
            self.start_pos = other_tc.position()
        if not self.split_text:                    
       
            self.listwidget.setHidden(True)
            self.isPinyinEditting = False
                
        else:
            if self.split_text[0] == "":
           
                self.listwidget.setHidden(True)
                self.isPinyinEditting = False
        return False         
        
    elif event.key() == Qt.Key_Down:              
        if self.listwidget.isHidden():
            tc = self.textCursor()                
            tc.movePosition(Down, MoveAnchor)
            self.setTextCursor(tc)
            return False
        
        if self.listwidget.current_index < len(self.listwidget.items)-1:
            
            if self.listwidget.items[ self.listwidget.current_index + 1].text():
                self.listwidget.current_index += 1                  
    
        if self.listwidget.current_index%9 == 0 and self.listwidget.current_index != 0 and self.listwidget.current_index < len(self.listwidget.items)-1:     
            
            self.listwidget.page += 1
            #Bug, LeftToRightの時は、ScrollToItemが先頭位置へ移動しない。
            self.listwidget.scrollToItem(self.listwidget.item(self.listwidget.current_index), QListWidget.ScrollHint.PositionAtTop)
     
        self.listwidget.setCurrentRow(self.listwidget.current_index)
        return False
    
    elif event.key() == Qt.Key_Up:
        if not self.listwidget.isVisible():
            tc = self.textCursor()                
            tc.movePosition(Up, MoveAnchor)
            self.setTextCursor(tc)
            return False            
          
        if self.listwidget.current_index%9 == 0 and self.listwidget.current_index > 0:
            if self.listwidget.page > 0:
                
                self.listwidget.page -= 1
            
            self.listwidget.scrollToItem(self.listwidget.item(self.listwidget.current_index-9), QListWidget.ScrollHint.PositionAtBottom)
        if self.listwidget.current_index > 0:
            self.listwidget.current_index -= 1    
        self.listwidget.setCurrentRow(self.listwidget.current_index)
        return False
    
    elif event.key() == Qt.Key_Left:
        if self.listwidget.isHidden():
            tc = self.textCursor()                
            tc.movePosition(Left, MoveAnchor)
            self.setTextCursor(tc)
            return False
        

        return False
    elif event.key() == Qt.Key_Right:
        if self.listwidget.isHidden():
            tc = self.textCursor()                
            tc.movePosition(Right, MoveAnchor)
            self.setTextCursor(tc)
            return False
                
        return False
    
     
    elif event.key() in (Qt.Key_A, Qt.Key_B, Qt.Key_C, Qt.Key_D, Qt.Key_E, Qt.Key_F, Qt.Key_G, Qt.Key_H,
                Qt.Key_I, Qt.Key_J, Qt.Key_K, Qt.Key_L, Qt.Key_M, Qt.Key_N, Qt.Key_O, Qt.Key_P, Qt.Key_Q,
                Qt.Key_R, Qt.Key_S, Qt.Key_T, Qt.Key_U, Qt.Key_V, Qt.Key_W, Qt.Key_X, Qt.Key_Y, Qt.Key_Z):

        text = self.keyDicts[event.key()].underLeft        
        
        selectedText = ""
        tc = self.textCursor()
        pos = tc.position()                
              
        tc.insertText(text) 
        self.end_pos = tc.position()
        tc.clearSelection()
        
        other = self.textCursor()
        
        #6個のアルファベットがある状況       
        other.movePosition(PreviousCharacter, KeepAnchor, 7)
        selectedText = other.selectedText()
        selectedText_suffix = selectedText[-1]

        
        
        if reInsert(self, other, "^shuang[a-z|ü]$", f"shuang*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^chuang[a-z|ü]$", f"chuang*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^zhuang[a-z|ü]$", f"zhuang*{selectedText_suffix}", selectedText): return False
        other = self.textCursor()
        #6個のアルファベットがある状況       
        other.movePosition(PreviousCharacter, KeepAnchor, 6)
        selectedText = other.selectedText()
        selectedText_suffix = selectedText[-1]
        
        if reInsert(self, other, "^chang[a-z|ü]$", f"chang*{selectedText_suffix}", selectedText): return False        
        if reInsert(self, other, "^cheng[a-z|ü]$", f"cheng*{selectedText_suffix}", selectedText): return False            
        if reInsert(self, other, "^chuan[a-f|h-z|ü]$", f"chuan*{selectedText_suffix}", selectedText): return False 
        if reInsert(self, other, "^huang[a-z|ü]$", f"huang*{selectedText_suffix}", selectedText): return False 
        if reInsert(self, other, "^niang[a-z|ü]$", f"niang*{selectedText_suffix}", selectedText): return False 
        if reInsert(self, other, "^shang[a-z|ü]$", f"shang*{selectedText_suffix}", selectedText): return False
        
        if reInsert(self, other, "^sheng[a-z|ü]$", f"sheng*{selectedText_suffix}", selectedText): return False 
        if reInsert(self, other, "^liang[a-z|ü]$", f"liang*{selectedText_suffix}", selectedText): return False 
        if reInsert(self, other, "^jiang[a-z|ü]$", f"jiang*{selectedText_suffix}", selectedText): return False 
        if reInsert(self, other, "^giang[a-z|ü]$", f"giang*{selectedText_suffix}", selectedText): return False 
        if reInsert(self, other, "^guang[a-z|ü]$", f"guang*{selectedText_suffix}", selectedText): return False 
        if reInsert(self, other, "^xiang[a-z|ü]$", f"xiang*{selectedText_suffix}", selectedText): return False 
        if reInsert(self, other, "^zhang[a-z|ü]$", f"zhang*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^zheng[^aiueo]$", f"zheng*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^zheng[aiueo]$", f"zhen*g{selectedText_suffix}", selectedText): return False 
        if reInsert(self, other, "^zhuan[a-f|h-z|ü]$", f"zhuan*{selectedText_suffix}", selectedText): return False 
        if reInsert(self, other, "^zhong[a-z|ü]$", f"zhong*{selectedText_suffix}", selectedText): return False
        
        
        other = self.textCursor()
        other.movePosition(PreviousCharacter, KeepAnchor, 5)
        selectedText = other.selectedText()
        selectedText_suffix = selectedText[-1]
        if reInsert(self, other, "^bang[a-z|ü]$", f"bang*{selectedText_suffix}", selectedText): return False 
        if reInsert(self, other, "^biao[a-z|ü]$", f"biao*{selectedText_suffix}", selectedText): return False 
        if reInsert(self, other, "^bing[a-z|ü]$", f"bing*{selectedText_suffix}", selectedText): return False 
        if reInsert(self, other, "^bian[a-z|ü]$", f"bian*{selectedText_suffix}", selectedText): return False 
        if reInsert(self, other, "^cong[a-z|ü]$", f"cong*{selectedText_suffix}", selectedText): return False 
        if reInsert(self, other, "^ceng[a-z|ü]$", f"ceng*{selectedText_suffix}", selectedText): return False 
        if reInsert(self, other, "^chao[a-z|ü]$", f"chao*{selectedText_suffix}", selectedText): return False 
        if reInsert(self, other, "^chan[a-f|h-z|ü]$", f"chan*{selectedText_suffix}", selectedText): return False 
        if reInsert(self, other, "^chen[a-f|h-z|ü]$", f"chen*{selectedText_suffix}", selectedText): return False 
        if reInsert(self, other, "^chun[a-f|h-z|ü]$", f"chun*{selectedText_suffix}", selectedText): return False 
        if reInsert(self, other, "^dong[a-z|ü]$", f"dong*{selectedText_suffix}", selectedText): return False
        
        if reInsert(self, other, "^dian[a-z|ü]$", f"dian*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^deng[a-z|ü]$", f"deng*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^fang[a-z|ü]$", f"fang*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^fengo$", f"fen*go", selectedText): return False
        if reInsert(self, other, "^feng[a-z|ü]$", f"feng*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^hang[a-z|ü]$", f"hang*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^hong[a-z|ü]$", f"hong*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^huan[a-f|h-z|ü]$", f"huan*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^huai[a-z|ü]$", f"huai*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^huir[a-z|ü]$", f"huir*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^jian[a-f|h-z|ü]$", f"jian*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^jiao[a-z|ü]$", f"jiao*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^jing[a-z|ü]$", f"jing*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^keng[a-z|ü]$", f"keng*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^kuan[a-f|h-z|ü]$", f"kuan*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^kuai[a-z|ü]$", f"kuai*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^lang[a-z|ü]$", f"lang*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^liao[a-z|ü]$", f"liao*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^ling[a-z|ü]$", f"ling*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^leng[a-z|ü]$", f"leng*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^long[a-z|ü]$", f"long*{selectedText_suffix}", selectedText): return False

        if reInsert(self, other, "^guan[a-f|h-z|ü]$", f"guan*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^geng[a-z|ü]$", f"geng*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^gong[a-z|ü]$", f"gong*{selectedText_suffix}", selectedText): return False

        if reInsert(self, other, "^mian[a-z|ü]$", f"mian*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^meng[a-z|ü]$", f"meng*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^ming[a-z|ü]$", f"ming*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^nian[a-f|h-z|ü]$", f"nian*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^ning[a-z|ü]$", f"ning*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^nuan[a-z|ü]$", f"nuan*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^neng[a-z|ü]$", f"neng*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^nong[a-z|ü]$", f"nong*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^peng[a-z|ü]$", f"peng*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^ping[a-z|ü]$", f"ping*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^qiao[a-z|ü]$", f"qiao*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^quan[a-z|ü]$", f"quan*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^qing[a-z|ü]$", f"qing*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^rong[a-z|ü]$", f"rong*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^shao[a-z|ü]$", f"shao*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^shen[a-f|h-z|ü]$", f"shen*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^shui[a-z|ü]$", f"shui*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^shuo[a-z|ü]$", f"shuo*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^shou[a-z|ü]$", f"shou*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^song[a-z|ü]$", f"song*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^tian[a-z|ü]$", f"tian*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^tiao[a-z|ü]$", f"tiao*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^ting[a-z|ü]$", f"ting*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^tuan[a-z|ü]$", f"tuan*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^teng[a-z|ü]$", f"teng*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^tong[a-z|ü]$", f"tong*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^wang[a-z|ü]$", f"wang*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^xian[a-f|h-z|ü]$", f"xian*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^xuan[a-z|ü]$", f"xuan*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^xiao[a-z]$", f"xiao*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^xing[a-z]$", f"xing*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^ying[a-z|ü]$", f"ying*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^yong[a-z|ü]$", f"yong*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^yuan[a-z|ü]$", f"yuan*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^zong[a-z|ü]$", f"zong*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^zhan[a-f|h-z|ü]$", f"zhan*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^zhai[a-z|ü]$", f"zhai*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^zhen[a-f|h-z|ü]$", f"zhen*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^zhun[a-f|h-z|ü]$", f"zhun*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^zhou[a-z|ü]$", f"zhou*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^zhao[a-z|ü]$", f"zhao*{selectedText_suffix}", selectedText): return False
        
        other = self.textCursor()
        other.setPosition(self.end_pos, MoveAnchor)
        other.movePosition(PreviousCharacter, KeepAnchor, 4)
        selectedText = other.selectedText()
        
        if reInsert(self, other, "^ang[a-z|ü]$", f"ang*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^ban[a-f|h-z|ü]$", f"ban*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^bai[a-z|ü]$", f"bai*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^bei[a-z|ü]$", f"bei*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^ben[a-f|h-z|ü]$", f"ben*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^bao[a-z|ü]$", f"bao*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^bie[a-z|ü]$", f"bie*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^bin[a-f|h-z|ü]$", f"bin*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^cai[a-z|ü]$", f"cai*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^can[a-f|h-z]$", f"can*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^cun[a-z|ü]$", f"cun*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^cuo[a-z|ü]$", f"cuo*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^chu[b-m|o-z|ü]$", f"chu*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^chi[a-z|ü]$", f"chi*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^dao[a-z|ü]$", f"dao*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^dia[a-m|p-z|ü]$", f"dia*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^dier$", f"di*er", selectedText): return False
        if reInsert(self, other, "^die[a-m|p-z|ü]$", f"die*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^diu[a-z|ü]$", f"diu*{selectedText_suffix}", selectedText): return False

        if reInsert(self, other, "^dai[a-z|ü]$", f"dai*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^dan[a-f|h-z|ü]$", f"dan*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^den[a-f|h-z|ü]$", f"den*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^dei[a-z|ü]$", f"dei*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^dou[a-z|ü]$", f"dou*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^dui[a-z|ü]$", f"dui*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^duo[a-z|ü]$", f"duo*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^fan[a-f|h-z|ü]$", f"fan*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^fen[a-f|h-z|ü]$", f"fen*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^fei[a-z|ü]$", f"fei*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^gui[a-z|ü]$", f"gui*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^gan[a-f|h-z|ü]$", f"gan*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^gao[a-z|ü]$", f"gao*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^guo[a-z|ü]$", f"guo*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^gun[aiueo]$", f"gu*n{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^gun[a-z|ü]$", f"gun*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^gei[a-f|h-z|ü]$", f"gei*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^gen[a-f|h-z|ü]$", f"gen*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^gou[a-z|ü]$", f"gou*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^hai[a-z|ü]$", f"hai*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^hao[a-z|ü]$", f"hao*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^han[a-f|h-z|ü]$", f"han*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^hen[a-f|h-z|ü]$", f"hen*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^hou[a-z|ü]$", f"hou*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^hua[a-h|j-m|o-z|ü]$", f"hua*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^hui[a-z|ü]$", f"hui*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^hun[a-z|ü]$", f"hun*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^huo[a-z|ü]$", f"huo*{selectedText_suffix}", selectedText): return False
   
        if reInsert(self, other, "^kai[a-z|ü]$", f"kai*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^ken[a-f|h-z|ü]$", f"ken*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^kan[a-f|h-z|ü]$", f"kan*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^kao[a-z|ü]$", f"kao*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^kua[a-h|j-m|o-z|ü]$", f"kua*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^kui[a-z|ü]$", f"kui*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^kun[a-z|ü]$", f"kun*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^kou[a-z|ü]$", f"kou*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^mao[a-z|ü]$", f"mao*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^mai[a-z|ü]$", f"mai*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^mei[a-z|ü]$", f"mei*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^men[a-f|h-z|ü]$", f"men*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^niu[^aiueo|ü]$", f"niu*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^nin[^aiueog|ü]$", f"nin*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^nin[aiueo]$", f"ni*n{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^nen[a-f|h-z|ü]$", f"nen*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^pin[a-f|h-z|ü]$", f"pin*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^pei[a-z|ü]$", f"pei*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^pen[a-f|h-z|ü]$", f"pen*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^qin[a-f|h-z|ü]$", f"qie*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^qin[a-f|h-z|ü]$", f"qin*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^qiu[a-f|h-z|ü]$", f"qiu*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^que[a-z|ü]$", f"que*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^qun[a-z|ü]$", f"qun*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^ran[a-f|h-z|ü]$", f"ran*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^ren[a-f|h-z|ü]$", f"ren*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^tai[a-z|ü]$", f"tai*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^tao[a-z|ü]$", f"tao*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^tia[a-m|p-z|ü]$", f"tia*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^tie[a-z|ü]$", f"tie*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^tuo[a-z|ü]$", f"tuo*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^tou[a-z|ü]$", f"tou*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^san[a-z|ü]$", f"san*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^sen[a-z|ü]$", f"sen*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^sui[a-z|ü]$", f"sui*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^suo[a-z|ü]$", f"suo*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^sha[a-m|p-z|ü]$", f"sha*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^she[a-m|o-z|ü]$", f"she*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^shu[b-h|j-n|p-z|ü]$", f"shu*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^shi[a-z|ü]$", f"shi*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^jia[a-m|p-z|ü]$", f"jia*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^jiu[a-z|ü]$", f"jiu*{selectedText_suffix}", selectedText): return False
        
        if reInsert(self, other, "^jie[a-z|ü]$", f"jie*{selectedText_suffix}", selectedText): return False      
        if reInsert(self, other, "^jin[a-f|h-z|ü]$", f"jin*{selectedText_suffix}", selectedText): return False   
        if reInsert(self, other, "^jue[a-z|ü]$", f"jue*{selectedText_suffix}", selectedText): return False 
        if reInsert(self, other, "^jun[a-z|ü]$", f"jun*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^lao[a-z|ü]$", f"lao*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^lai[a-z|ü]$", f"lai*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^lei[a-z|ü]$", f"lei*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^liu[a-z|ü]$", f"liu*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^lia[a-m|p-z|ü]$", f"lia*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^lie[a-z|ü]$", f"lie*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^luo[a-z|ü]$", f"luo*{selectedText_suffix}", selectedText): return False        
        if reInsert(self, other, "^wan[a-f|h-z|ü]$", f"wan*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^wen[a-z|ü]$", f"wen*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^wei[a-z|ü]$", f"wei*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^xia[a-m|p-z|ü]$", f"xia*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^xie[a-z|ü]$", f"xie*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^xiu[a-z|ü]$", f"xiu*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^xin[a-f|h-z|ü]$", f"xin*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^xue[a-z|ü]$", f"xue*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^yao[a-z|ü]$", f"yao*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^you[a-z|ü]$", f"you*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^yin[^aiueog|ü]$", f"yin*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^yin[aiueo]$", f"yi*n{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^yue[a-z|ü]$", f"yue*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^yuna$", f"yu*na", selectedText): return False
        if reInsert(self, other, "^yun[b-z|ü]$", f"yun*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^zao[a-z|ü]$", f"zao*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^zai[a-z|ü]$", f"zai*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^zha[a-h|j-m|p-z|ü]$", f"zha*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^zhi[a-z|ü]$", f"zhi*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^zhu[b-m|p-z|ü]$", f"zhu*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^zuo[a-z|ü]$", f"zuo*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^zui[a-z|ü]$", f"zui*{selectedText_suffix}", selectedText): return False
        
        other = self.textCursor()
        other.setPosition(self.end_pos, MoveAnchor)
        other.movePosition(PreviousCharacter, KeepAnchor, 3)
        selectedText = other.selectedText()
        if reInsert(self, other, "^an[a-f|h-z|ü]$", f"an*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^ai[a-z|ü]$", f"ai*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^ba[a-h|j-m|p-z|ü]$", f"ba*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^bi[b-d|f-m|o-z|ü]$", f"bi*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^bu[a-z|ü]$", f"bu*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^be[a-h|j-m|o-z|ü]$", f"be*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^bo[a-z|ü]$", f"bo*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^ca[a-h|j-m|p-t|u-z|ü]$", f"ca*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^ci[a-z|ü]$", f"ci*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^co[a-m|o-z|ü]$", f"co*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^cu[a-h|j-m|p-z|ü]$", f"cu*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^ce[a-m|o-z|ü]$", f"ce*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^da[a-h|j-m|p-z|ü]$", f"da*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^di[b-d|f-m|p-t|v-z|ü]$", f"di*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^de[a-h|j-m|o-z|ü]$", f"de*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^do[a-m|p-t|v-z|ü]$", f"do*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^du[b-h|j-m|p-z|ü]$", f"du*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^er[a-z|ü]$", f"er*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^fa[a-m|o-z|ü]$", f"fa*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^fu[a-z|ü]$", f"fu*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^fe[a-h|j-m|o-z|ü]$", f"fe*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^fo[a-z|ü]$", f"fo*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^ga[a-h|j-m|p-z|ü]$", f"ga*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^gu[b-h|j-m|p-z|ü]$", f"gu*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^ge[a-h|j-m|o-z|ü]$", f"ge*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^go[a-m|o-t|v-z|ü]$", f"go*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^ha[a-h|j-m|p-z|ü]$", f"ha*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^hu[b-h|j-m|p-z|ü]$", f"hu*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^he[a-h|j-m|p-z|ü]$", f"he*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^ho[a-m|p-t|v-z|ü]$", f"ho*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^ji[b-d|f-m|o-t|v-z|ü]$", f"ji*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^ju[b-d|f-m|p-t|v-z|ü]$", f"ju*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^ka[a-h|j-m|p-z|ü]$", f"ka*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^ku[b-h|j-m|p-z|ü]$", f"ku*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^ko[a-m|o-t|v-z|ü]$", f"ko*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^ke[a-m|o-z|ü]$", f"ke*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^la[a-h|j-m|p-z|ü]$", f"la*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^li[b-d|f-m|p-t|v-z|ü]$", f"li*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^le[a-h|j-m|p-z|ü]$", f"le*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^lu[a-n|p-z|ü]$", f"lu*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^lü[a-h|j-m|p-z|ü]$", f"lü*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^lo[a-m|o-t|v-z|ü]$", f"lo*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^ma[a-h|j-m|p-t|v-z|ü]$", f"ma*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^mi[b-m|p-t|v-z|ü]$", f"mi*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^mu[a-h|j-z|ü]$", f"mu*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^me[a-h|j-m|o-z|ü]$", f"me*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^mo[a-m|o-t|v-z|ü]$", f"mo*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^na[a-m|p-t|v-z|ü]$", f"na*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^ni[b-d|f-m|o-t|v-z|ü]$", f"ni*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^nu[b-d|f-m|p-t|v-z|ü]$", f"nu*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^ne[a-h|j-m|o-t|v-z|ü]$", f"ne*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^no[a-m|o-t|v-z|ü]$", f"no*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^ou[a-z|ü]$", f"ou*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^pa[a-h|j-m|p-z|ü]$", f"pa*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^pu[a-z|ü]$", f"pu*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^pe[a-h|j-m|o-z|ü]$", f"pe*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^pi[a-d|f-m|o-z|ü]$", f"pi*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^po[a-m|o-t|v-z|ü]$", f"po*{selectedText_suffix}", selectedText): return False        
        if reInsert(self, other, "^qi[b-d|f-m|p-t|v-z|ü]$", f"qi*{selectedText_suffix}", selectedText): return False   
        if reInsert(self, other, "^qu[-d|f-m|o-z|ü]$", f"qu*{selectedText_suffix}", selectedText): return False  
        if reInsert(self, other, "^ra[a-m|p-z|ü]$", f"ra*{selectedText_suffix}", selectedText): return False  
        if reInsert(self, other, "^re[a-m|p-z|ü]$", f"re*{selectedText_suffix}", selectedText): return False  
        if reInsert(self, other, "^ro[a-m|p-z|ü]$", f"ro*{selectedText_suffix}", selectedText): return False 
        if reInsert(self, other, "^ri[a-m|o-t|v-z|ü]$", f"ri*{selectedText_suffix}", selectedText): return False 
        if reInsert(self, other, "^ru[a-h|j-m|p-z|ü]$", f"ru*{selectedText_suffix}", selectedText): return False 
        if reInsert(self, other, "^sa[a-h|j-m|p-z|ü]$", f"sa*{selectedText_suffix}", selectedText): return False 
        if reInsert(self, other, "^si[a-m|p-z|ü]$", f"si*{selectedText_suffix}", selectedText): return False 
        if reInsert(self, other, "^so[a-m|o-t|v-z|ü]$", f"so*{selectedText_suffix}", selectedText): return False 
        if reInsert(self, other, "^se[a-m|o-z|ü]$", f"se*{selectedText_suffix}", selectedText): return False 
        if reInsert(self, other, "^su[a-h|j-m|p-z|ü]$", f"su*{selectedText_suffix}", selectedText): return False 
        if reInsert(self, other, "^ta[a-h|j-m|p-z|ü]$", f"ta*{selectedText_suffix}", selectedText): return False 
        if reInsert(self, other, "^ti[b-d|f-m|o-z|ü]$", f"ti*{selectedText_suffix}", selectedText): return False 
        if reInsert(self, other, "^te[a-d|f-m|o-z|ü]$", f"te*{selectedText_suffix}", selectedText): return False 
        if reInsert(self, other, "^to[a-m|o-t|v-z|ü]$", f"to*{selectedText_suffix}", selectedText): return False 
        if reInsert(self, other, "^tu[b-h|j-m|p-t|v-z|ü]$", f"tu*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^wa[a-h|j-m|o-z|ü]$", f"wa*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^we[a-h|j-m|o-z|ü]$", f"we*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^wo[a-z|ü]$", f"wo*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^wu[a-z|ü]$", f"wu*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^xi[b-d|f-h|j-m|p-t|v-z|ü]$", f"xi*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^xu[b-d|f-h|j-m|o-z|ü]$", f"xu*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^ya[a-m|p-z|ü]$", f"ya*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^yi[a-m|p-z|ü]$", f"yi*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^yo[a-m|p-t|v-z|ü]$", f"yo*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^ye[a-z|ü]$", f"ye*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^yu[b-d|f-m|o-z|ü]$", f"yu*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^za[a-h|j-m|p-z|ü]$", f"za*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^zi[a-z|ü]$", f"zi*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^zu[a-h|j-m|p-z|ü]$", f"zu*{selectedText_suffix}", selectedText): return False
        if reInsert(self, other, "^ze[a-m|o-z|ü]$", f"ze*{selectedText_suffix}", selectedText): return False        
        if reInsert(self, other, "^zo[a-m|o-t|v-z|ü]$", f"zo*{selectedText_suffix}", selectedText): return False    
     
        other = self.textCursor()
        other.setPosition(self.end_pos, MoveAnchor)
        other.movePosition(PreviousCharacter, KeepAnchor, 2)
        
        if reInsert(self, other, "a[b-h|j-n|p-z|ü]$", f"a*{selectedText_suffix}", selectedText): return False       
        if reInsert(self, other, "b[b-d|f-h|j-n|p-t|v-z|ü]$", f"b*{selectedText_suffix}", selectedText): return False  
        if reInsert(self, other, "y[b-d|f-h|j-n|p-t|v-z|ü]$", f"y*{selectedText_suffix}", selectedText): return False  
        if reInsert(self, other, "u[a-d|f-h|j-m|p-t|u-z|ü]$", f"u*{selectedText_suffix}", selectedText): return False     
    
    if self.split_text == ['']:
        self.listwidget.setHidden(True)     
        self.isPinyinEditting = False
    elif self.split_text == []:    
        self.listwidget.setHidden(True)       
        self.isPinyinEditting = False
    self.re_search()
            
    return False
