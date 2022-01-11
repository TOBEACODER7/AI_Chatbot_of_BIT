from ui.ui_look import Ui_MainWindow
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtGui import QMovie
import os
import sys

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.fun1)
        self.ui.pushButton_2.clicked.connect(self.fun2)
        self.gif = QMovie('ui/normal.gif')
        self.ui.label.setMovie(self.gif)
        self.gif.start()

    def fun1(self):
        self.gif = QMovie('ui/say.gif')
        self.ui.label.setMovie(self.gif)
        self.gif.start()
        """ os.system('activate aiproject') """
        os.system('start /b python demo_test.py')
        """ import chatbot.demo_test """
        """ cb.beg('start') """

    def fun2(self):
        
        sys.exit()
    
    




    