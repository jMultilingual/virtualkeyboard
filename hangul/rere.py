from PySide6.QtCore import QTextStream, QFile
import re

t = re.compile('"\W"')
tt = re.compile('\W')
dic = {}
file = QFile("repair_dict.py")
count = 0
value = ""
if file.open(QFile.ReadOnly):
    out = QTextStream(file)

    while not out.atEnd():
        line = out.readLine()
        line = line.lstrip()
        line = line.rstrip()
        if line.startswith("if"):
            line = line.replace("if t == ", "")
            line = line.replace(":", "")
            key = line
            value = ""
            dic[key] = value
        elif line.startswith("elif"):
            line = line.replace("elif t == ", "")
            line = line.replace(":", "")
            key = line
            dic[key] = value
            
        elif line.startswith("tc"):
            line = line.replace("tc.insertText(", "")
            line = line.replace(")", "")

            value = line
            dic[key] = value
        
            
        

        count += 1
    print(dic)
file.close()
