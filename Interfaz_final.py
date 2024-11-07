import sys
from PyQt6.QtCore import QSize, Qt, pyqtSlot
from PyQt6.QtWidgets import (QApplication, QLabel, QWidget, QLineEdit,QTextEdit, QPushButton, QGridLayout, QVBoxLayout, QMainWindow, QFileDialog)

from PyQt6.QtGui import QFont, QPixmap


from cal_general import Controller
from ventana3_referencia import MainWindow4

import warnings
warnings.simplefilter(action='ignore', category=Warning)

class AnotherWindow2(QMainWindow):
    
    controller = None

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.load_excel()
        self.referencia1 = MainWindow4()
        
        self.setGeometry(100,100,500,300)
        self.setWindowTitle("VIGA SECCION COMPUESTA (DEFLEXION)")
        self.setStyleSheet("background-color: #2e2e2e")
        
        fuente = QFont("Arial",11)
        fuente1 = QFont("Arial",20)
        
        #TITULOS
        #TITULO PRINCIPAL
        user_label = QLabel()
        user_label.setText("Información general de la viga:")
        user_label.setFont(fuente)
        
        
        #COMENTARIOS
        
        longitud_total = QLabel()
        longitud_total.setText("(X) Longitud total de la viga: (metros)")
        longitud_total.setFont(fuente)
        
        carga_1 = QLabel()
        carga_1.setText("(C1) Carga 1: (kN)")
        carga_1.setFont(fuente)
        
        longitud_x1 = QLabel()
        longitud_x1.setText("(X1) Longitud correspondiente: (metros)")
        longitud_x1.setFont(fuente)
        
        carga_2 = QLabel()
        carga_2.setText("(C2) Carga 2: (kN)")
        carga_2.setFont(fuente)
        
        longitud_x2 = QLabel()
        longitud_x2.setText("(X2) Longitud correspondiente: (metros)")
        longitud_x2.setFont(fuente)
        
        self.error_mssg = QLabel()
        self.error_mssg.setText("")
        self.error_mssg.setFont(fuente)
        
        
        
        #ENTRADA DE DATOS
        #CONCRETO
        
        self.input_longitud_total = QLineEdit(self)
        self.input_longitud_total.setPlaceholderText("metros")
        
        self.input_1_carga1 = QLineEdit(self)
        self.input_1_carga1.setPlaceholderText("kN")
        
        self.input_1_longitudx1 = QLineEdit(self)
        self.input_1_longitudx1.setPlaceholderText("metros")
        
        self.input_2_carga2 = QLineEdit(self)
        self.input_2_carga2.setPlaceholderText("kN")
        
        self.input_2_longitudx2 = QLineEdit(self)
        self.input_2_longitudx2.setPlaceholderText("metros")
        
        
        #BOTON
        boton_deflexion = QPushButton()
        boton_deflexion.setText("Calcular la deflexión de la viga compuesta ")
        boton_deflexion.setFont(fuente)
        boton_deflexion.clicked.connect(self.calculo_deflexion)
        boton_deflexion.setStyleSheet("QPushButton {background-color: #5c5c5c; color: #dedede;}")
        
        
        self.boton_ayuda = QPushButton()
        self.boton_ayuda.setText("Mostrar imagen de referencia")
        self.boton_ayuda.setFont(fuente)
        self.boton_ayuda.clicked.connect(self.mostrar_imagen_refencia)
        self.boton_ayuda.setStyleSheet("QPushButton {background-color: #b2af39; color: #dedede;}")
        
        
        #PANTALLA
        self.pantalla = QTextEdit(self)
        self.pantalla.setFont(fuente1)
        self.pantalla.setDisabled(True)
        
        
        #IMAGEN
        #self.pixmap = QPixmap("VIGADEFLEXION.png")
        #self.imagen = QLabel(self)
        #self.imagen.setPixmap(self.pixmap)
        
        #LAYOUT
        
        self.main_grid2 = QGridLayout()
        
        #TITULOS
        self.main_grid2.addWidget(user_label,0,0,1,1)
        
        
        #COMENTARIOS
        self.main_grid2.addWidget(longitud_total,1,0,1,1)
        self.main_grid2.addWidget(carga_1,2,0,1,1)
        self.main_grid2.addWidget(longitud_x1,3,0,1,1)
        self.main_grid2.addWidget(carga_2,4,0,1,1)
        self.main_grid2.addWidget(longitud_x2,5,0,1,1)
        
        
        #ENTRADA DE DATOS
        
        self.main_grid2.addWidget(self.input_longitud_total,1,2,1,2)
        self.main_grid2.addWidget(self.input_1_carga1,2,2,1,2)
        self.main_grid2.addWidget(self.input_1_longitudx1,3,2,1,2)
        self.main_grid2.addWidget(self.input_2_carga2,4,2,1,2)
        self.main_grid2.addWidget(self.input_2_longitudx2,5,2,1,2)
        
        #BOTON
        
        self.main_grid2.addWidget(boton_deflexion,6,0,1,3)
        self.main_grid2.addWidget(self.boton_ayuda,9,0,1,3)
        
        #PANTALLA
        
        self.main_grid2.addWidget(self.pantalla,7,0,1,3)
        
        #IMAGEN
        
        #self.main_grid2.addWidget(self.imagen,0,20,25,25)
        
        self.main_grid2.addWidget(self.error_mssg,8,0,1,3)
        
        w = QWidget()
        w.setLayout(self.main_grid2)
        self.setCentralWidget(w)
        
    def use_label_aux1(self, texto, color="ff9156"):
        self.error_mssg.setText(texto)
        self.error_mssg.setStyleSheet(f'color: #{color};')
        
    def calculo_deflexion(self):
        if (self.input_longitud_total.text() == "" or self.input_1_carga1.text() == "" or self.input_1_longitudx1.text() == "" or self.input_2_carga2.text() == "" or self.input_2_longitudx2.text() == ""):
            self.use_label_aux1("Todos los campos son obligatorios!")
            
        else:    
            longitud_total = float(self.input_longitud_total.text().replace(",","."))
            carga1 = float(self.input_1_carga1.text().replace(",","."))
            longitudx1 = float(self.input_1_longitudx1.text().replace(",","."))
            carga2 = float(self.input_2_carga2.text().replace(",","."))
            longitudx2 = float(self.input_2_longitudx2.text().replace(",","."))
            
            
            rta1 = self.controller.deflexion_general(longitud_total, carga1, longitudx1, carga2, longitudx2)
            self.pantalla.setText("{:.5f} m".format(rta1))
            self.use_label_aux1("Datos Cargados Correctamente", "65ff56")
        
    def load_excel(self):
        fname = self.controller.GLOBAL
        self.controller.cargar_archivoxlsx(fname=fname)
        #print(f"La ruta del file es {fname}")
        #print(f"CÁLCULO DE INERCIA TOTAL {self.controller.cargar_archivoxlsx(fname=fname)}")
        #print(self.controller.df)
        #self.controller.GLOBAL = fname
        
    def mostrar_imagen_refencia(self):
        
        if self.referencia1.isVisible():
            self.referencia1.hide()
        else:
            #self.hide()
            self.referencia1.show()
        