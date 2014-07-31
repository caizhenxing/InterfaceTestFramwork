# -*- coding:utf-8 -*-
__author__ = 'kiven'

import sys
from PyQt4 import QtCore,QtGui

class MyWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setWindowTitle('Test')
        self.resize(300,200)
        # 添加标签
        lable = QtGui.QLabel('hello world')
        lable.setAlignment(QtCore.Qt.AlignCenter)
        self.setCentralWidget(lable)

app = QtGui.QApplication(sys.argv)
mywindow = MyWindow()
mywindow.show()
app.exec_()