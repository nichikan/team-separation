# _*_coding: utf-8_*_
import sys
import re
from PyQt5.QtWidgets import (QApplication, QWidget, QTextEdit, QGridLayout, QPushButton, QLabel)

import random


def splits( strings ):
    a = re.split('[ ,、　]',strings)
    return a

def ramdomteam ( teamlists ):
    playerlist = {}
    for player in teamlists:
        count = teamlists.index(player)
        playerlist[count] = player
    random.shuffle(playerlist)
    return playerlist

usedlist = []

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("")
        self.setGeometry(400, 200, 550, 220)
        self.InportLabel = QLabel("Input")
        self.OutputLabel = QLabel("Output")
        self.sbutton = QPushButton("Shuffle")
        self.clearbutton = QPushButton("Clear")
        self.InportEdit = QTextEdit()
        self.OutputEdit = QTextEdit()
        self.sbutton.clicked.connect(self.shuffle)
        self.clearbutton.clicked.connect(self.clear)

        self.glayout = QGridLayout()
        self.glayout.setSpacing(10)
        self.glayout.addWidget(self.InportLabel, 0, 0, 1, 3)
        self.glayout.addWidget(self.OutputLabel, 0, 3, 1, 3)
        self.glayout.addWidget(self.InportEdit, 1, 0, 2, 3)
        self.glayout.addWidget(self.OutputEdit, 1, 3, 2, 3)
        self.glayout.addWidget(self.sbutton, 3, 0, 1, 1)
        self.glayout.addWidget(self.clearbutton, 3, 1, 1, 1)

        self.setLayout(self.glayout)

    def shuffle(self):

        self.In = self.InportEdit.toPlainText()
        uselist = []
        alist = splits(self.In)
        num = len(alist)
        if num%2 != 0:
            num = num-1
        teamnum = int(num / 2)
        maxnum = num * (num-1)
        while 1:
            play = []
            flug = 0
            lists = ramdomteam(alist)
            for n in range(0,num,2):
                play.append(lists[n] + "," + lists[n+1])
            for m in range(teamnum):
                if play[m] in usedlist:
                    flug = 1
            if flug == 1:
                #print("aa")
                continue
            else:
                for nm in range(0,num,2):
                    uselist.append(lists[nm] + "," + lists[nm+1])
                    usedlist.append(lists[nm] + "," + lists[nm+1])
                    usedlist.append(lists[nm+1] + "," + lists[nm])
                    if len(usedlist) == maxnum:
                        print("clered")
                        usedlist.clear()
                print(uselist)
                break


        ulist = "\n".join(uselist)

        self.OutputEdit.setPlainText(ulist)
        
    def clear(self):
        self.InportEdit.setPlainText("")
        self.OutputEdit.setPlainText("")
        usedlist.clear()

    
if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
