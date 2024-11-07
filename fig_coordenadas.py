import pandas as pd
import sys
from PyQt6.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication, QLabel)
from PyQt6.QtGui import QFont, QPainter, QBrush, QPen, QColor, QPixmap
from PyQt6.QtCore import Qt

from cal_general import Controller

#df = pd.read_excel(fname)

#coordenadas_x = list(df["X"]*10000)
#coordenadas_y = list(df["Y"]*10000)

import warnings
warnings.simplefilter(action='ignore', category=Warning)


class AnotherWindow5(QWidget):
    
    controller, coordenadas_x, coordenadas_y = None, None, None
    
    def __init__(self, controller):
        super().__init__()
        
        self.controller = controller
        
        self.initUI()
        

    def initUI(self):
        self.setGeometry(1000, 100, 300, 500)
        #self.setGeometry(100, 100, 100, 100)
        self.setWindowTitle('FIGURA COMPUESTA')
        #print("Esto va dentro de fig_coordenardas")
        #print(self.controller.df)
        self.cargar_data()
        self.setFixedSize(400, 600)
        
        #self.show()   
    
    
    #def cargar_archivoxlsx(fname):   
        
        # = pd.read_excel("Libro1.xlsx")

    def cargar_data(self):
        scale = 10000
        self.coordenadas_x = self.controller.df["X"]*scale
        self.coordenadas_y = self.controller.df["Y"]*scale
       

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setPen(QPen(QColor("red"),  10, ))
       
        #painter.scale(0.15 , 0.15)
        painter.scale(0.085 , 0.085)
        
        
        painter.rotate(180)
        #painter.translate(-1000,-2800)
        painter.translate(-1500,-5800)
        
            
               
        for i in range(len(self.coordenadas_x)-1):
            
            painter.drawLine(int(self.coordenadas_x[i]), int(self.coordenadas_y[i]), int(self.coordenadas_x[i+1]), int(self.coordenadas_y[i+1]))
                
        painter.end()
        
        
        
              

        
        
              

        
        
        

        
        
              
