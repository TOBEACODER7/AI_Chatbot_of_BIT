""" 程序主入口 """
from ui import ui_fun
from PyQt5.QtGui import QMovie
from face_detection.test import face
import sys
import pyttsx3
import time

app = ui_fun.QtWidgets.QApplication(sys.argv)
window = ui_fun.mywindow()
window.show()
engine = pyttsx3.init()
while True:
    if face():
        engine.say('你好 点击侧面按钮即可提问')
        engine.runAndWait()
        window.gif = QMovie('ui/hello.gif')
        window.ui.label.setMovie(window.gif)
        window.gif.start()
        time.sleep(5)
        window.gif = QMovie('ui/normal.gif')
        window.ui.label.setMovie(window.gif)
        window.gif.start()
        break


sys.exit(app.exec_())
