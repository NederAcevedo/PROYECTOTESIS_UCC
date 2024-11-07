import time
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QMainWindow
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie, QRegion
from PyQt6.QtCore import Qt
import sys

class MainWindow4(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()   
        
    def initUI(self):
        
        self.setGeometry(650,100, 100, 100)
        self.setWindowTitle("IMAGEN DE REFERENCIA")
        #self.setWindowIcon(QIcon('guardianes.jpeg'))
        
        pixmap = QPixmap("Img/VIGADEFLEXION.png")
        label = QLabel(self)
        label.setPixmap(pixmap)
        label.setMask(pixmap.mask())
        #self.resize(pixmap.width(), pixmap.height())
        self.setFixedSize(pixmap.width(), pixmap.height())