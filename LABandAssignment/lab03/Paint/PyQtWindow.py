'''
By Muhammad Umar Anzar
'''

import PyQt5.QtCore as QtCore
from PyQt5 import QtWidgets
#from PyQt5.QtOpenGL import QGLWidget
import GL_window

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self) -> QtWidgets.QMainWindow:
        super().__init__()
        
        self.windowSetting()
        
        #self.GL_window = GL_window
        self.windowObject()
        self.GL_window.show()
        self.setCentralWidget(self.central_widget)

        #For multiThreading
        self.timer = QtCore.QTimer()
        self.animate = True

        #Button functions
        self.Btn_inc.clicked.connect(self.GL_window.lineWidthInc)
        self.Btn_dec.clicked.connect(self.GL_window.lineWidthDec)

        self.animation()

    def windowSetting(self) -> None:
        self.setWindowTitle("B19102104 M UMAR ANZAR PAINT")
        self.resize(800,600)
        self.center()

    def center(self) -> None:
        #Determines the center of screen
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        x,y = cp.x() , cp.y()
        #Center the window
        x = x - self.width()//2
        y = y - self.height()//2
        #apply new axis
        self.move(x,y)


    def windowObject(self) -> None:
       
        self.central_widget = QtWidgets.QWidget(self)
        self.GL_window = GL_window.GLWidget(self.central_widget)
        self.Btn_inc = QtWidgets.QPushButton("Line Width++",self.central_widget)
        self.Btn_dec= QtWidgets.QPushButton("Line Width--",self.central_widget)

        self.verticalLayout1 = QtWidgets.QVBoxLayout(self.central_widget)
        self.horizontalLayout1 = QtWidgets.QHBoxLayout()

        self.verticalLayout1.addWidget(self.GL_window)
        self.verticalLayout1.addLayout(self.horizontalLayout1)
        self.horizontalLayout1.addWidget(self.Btn_inc)
        self.horizontalLayout1.addWidget(self.Btn_dec)

    def animation(self):
        #Function That uses Qtimer multiThreading to Animated The OpenGl Widget
        if self.animate:
            print("Animation ON")
            self.timer.timeout.connect(self.GL_window.animate) #Updating OpenGl Widget
            
            #Starts or restarts the timer with a timeout interval of msec milliseconds. Like setting FPS
            self.timer.start(30)
            self.animate = False
        

    def closeEvent(self, event): # WHEN window is closed Automatically Qtimer is stopped.
        if not self.animate:
            print("Animation OFF")
        self.animate = True
        self.timer.stop()
        self.timer = QtCore.QTimer() #Re initialize so that it won't get ++ start()
