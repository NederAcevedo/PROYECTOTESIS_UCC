
import sys
from PyQt6.QtCore import QSize, Qt, pyqtSlot
from PyQt6.QtWidgets import (QApplication, QLabel, QWidget, QLineEdit,QTextEdit, QPushButton, QGridLayout, QVBoxLayout, QMainWindow, QFileDialog)
from PyQt6.QtGui import QFont, QPixmap


from cal_general import Controller
from fig_coordenadas import AnotherWindow5

from Interfaz_final import AnotherWindow2
from ventana2_referencia import MainWindow3

import warnings
warnings.simplefilter(action='ignore', category=Warning)

class AnotherWindow(QMainWindow):
    controller = None 
    
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        
        self.setGeometry(100,100,580,300)
        self.setWindowTitle("VIGA SECCION COMPUESTA (AREAS)")
        self.setStyleSheet("background-color: #2e2e2e")
        
        self.ventana_final1 = AnotherWindow2(self.controller)
        self.referencia = MainWindow3()
        self.fig2d = AnotherWindow5(self.controller)
        
        
        fuente = QFont("Arial",11)
        fuente1 = QFont("Arial",20)
        
        
        #TITULOS
        #TITULO PRINCIPAL
        user_label = QLabel()
        user_label.setText("Información general de la viga:")
        user_label.setFont(fuente)
        
        #TITULO CONCRETO
        area_concreto = QLabel()
        area_concreto.setText("Área del Concreto: ")
        area_concreto.setFont(fuente)
        
        #TITULOS DEL ACERO
        area_acero = QLabel()
        area_acero.setText("Área del Acero Estructural: ")
        area_acero.setFont(fuente)
        
        area_acero_fig1 = QLabel()
        area_acero_fig1.setText("Figura 1")
        area_acero_fig1.setFont(fuente)
        
        area_acero_fig2 = QLabel()
        area_acero_fig2.setText("Figura 2")
        area_acero_fig2.setFont(fuente)
        
        area_acero_fig3 = QLabel()
        area_acero_fig3.setText("Figura 3")
        area_acero_fig3.setFont(fuente)
        
        #COMENTARIOS
        #CONCRETO
        area_concreto_base = QLabel()
        area_concreto_base.setText("Ancho de la sección transformada de la losa de concreto (bc) (metros)")
        area_concreto_base.setFont(fuente)
        
        area_concreto_alto = QLabel()
        area_concreto_alto.setText("Altura de concreto: (metros)")
        area_concreto_alto.setFont(fuente)

        #ACERO
        
        area_acero_fig1_base = QLabel()
        area_acero_fig1_base.setText("Ancho de acero: (metros)")
        area_acero_fig1_base.setFont(fuente)
        
        area_acero_fig1_alto = QLabel()
        area_acero_fig1_alto.setText("Altura de acero: (metros)")
        area_acero_fig1_alto.setFont(fuente)
        
        area_acero_fig2_base = QLabel()
        area_acero_fig2_base.setText("Ancho de acero: (metros)")
        area_acero_fig2_base.setFont(fuente)
        
        area_acero_fig2_alto = QLabel()
        area_acero_fig2_alto.setText("Altura de acero: (metros)")
        area_acero_fig2_alto.setFont(fuente)
        
        area_acero_fig3_base = QLabel()
        area_acero_fig3_base.setText("Ancho de acero: (metros)")
        area_acero_fig3_base.setFont(fuente)
        
        area_acero_fig3_alto = QLabel()
        area_acero_fig3_alto.setText("Altura de acero: (metros)")
        area_acero_fig3_alto.setFont(fuente)
        
        
        #ENTRADA DE DATOS
        #CONCRETO
        
        self.input_1_concreto_base = QLineEdit(self)
        self.input_1_concreto_base.setPlaceholderText(f"({self.controller.dato_transformada}) metros")
        
        self.input_1_concreto_alto = QLineEdit(self)
        self.input_1_concreto_alto.setPlaceholderText("metros")
        
        #ACERO
        
        self.input_acero_fig1_base = QLineEdit(self)
        self.input_acero_fig1_base.setPlaceholderText("metros")
        
        self.input_acero_fig1_alto = QLineEdit(self)
        self.input_acero_fig1_alto.setPlaceholderText("metros")
        
        self.input_acero_fig2_base = QLineEdit(self)
        self.input_acero_fig2_base.setPlaceholderText("metros")
        
        self.input_acero_fig2_alto = QLineEdit(self)
        self.input_acero_fig2_alto.setPlaceholderText("metros")
        
        self.input_acero_fig3_base = QLineEdit(self)
        self.input_acero_fig3_base.setPlaceholderText("metros")
        
        self.input_acero_fig3_alto = QLineEdit(self)
        self.input_acero_fig3_alto.setPlaceholderText("metros")
        
        #IMAGEN
        #self.pixmap = QPixmap("VIGAAREA.png")
        #self.imagen = QLabel(self)
        #self.imagen.setPixmap(self.pixmap)
        
        #BOTON
        self.boton_1 = QPushButton()
        self.boton_1.setText("Calcular peso muerto de la viga ")
        self.boton_1.setFont(fuente)
        self.boton_1.clicked.connect(self.calculo_areas)
        self.boton_1.setStyleSheet("QPushButton {background-color: #5c5c5c; color: #dedede;}")
        
        self.boton_sgte = QPushButton()
        self.boton_sgte.setText("Paso siguiente")
        self.boton_sgte.setFont(fuente)
        self.boton_sgte.clicked.connect(self.ventana_final)
        self.boton_sgte.setEnabled(False)
        self.boton_sgte.setStyleSheet("QPushButton {background-color: #5c5c5c; color: #9e9e9e;}")
        
        self.boton_ayuda = QPushButton()
        self.boton_ayuda.setText("Mostrar imagen de referencia")
        self.boton_ayuda.setFont(fuente)
        self.boton_ayuda.clicked.connect(self.mostrar_imagen_refencia)
        self.boton_ayuda.setStyleSheet("QPushButton {background-color: #b2af39; color: #dedede;}")
        
        self.boton_ayuda1 = QPushButton()
        self.boton_ayuda1.setText("Mostrar pintado de las coordenadas")
        self.boton_ayuda1.setFont(fuente)
        self.boton_ayuda1.clicked.connect(self.mostrar_imagen_coordenadas)
        self.boton_ayuda1.setStyleSheet("QPushButton {background-color: #b2af39; color: #dedede;}")
        
        
        
        #PANTALLA
        self.pantalla = QTextEdit(self)
        self.pantalla.setFont(fuente1)
        self.pantalla.setDisabled(True)
        
        self.error_mssg = QLabel()
        self.error_mssg.setText("")
        self.error_mssg.setFont(fuente)
        
        
        
        
        #LAYOUT
        
        self.main_grid1 = QGridLayout()
        
        #TITULOS
        self.main_grid1.addWidget(user_label,0,0,1,1)
        self.main_grid1.addWidget(area_concreto,1,0,1,1)
        self.main_grid1.addWidget(area_acero,4,0,1,1)
        self.main_grid1.addWidget(area_acero_fig1,5,0,1,1)
        self.main_grid1.addWidget(area_acero_fig2,8,0,1,1)
        self.main_grid1.addWidget(area_acero_fig3,11,0,1,1)
        #COMENTARIOS
        
        self.main_grid1.addWidget(area_concreto_base,2,0,1,1)
        self.main_grid1.addWidget(area_concreto_alto,3,0,1,1)
        self.main_grid1.addWidget(area_acero_fig1_base,6,0,1,1)
        self.main_grid1.addWidget(area_acero_fig1_alto,7,0,1,1)
        self.main_grid1.addWidget(area_acero_fig2_base,9,0,1,1)
        self.main_grid1.addWidget(area_acero_fig2_alto,10,0,1,1)
        self.main_grid1.addWidget(area_acero_fig3_base,12,0,1,1)
        self.main_grid1.addWidget(area_acero_fig3_alto,13,0,1,1)
        
        #ENTRADA DE DATOS
        
        self.main_grid1.addWidget(self.input_1_concreto_base,2,1,1,2)
        self.main_grid1.addWidget(self.input_1_concreto_alto,3,1,1,2)
        self.main_grid1.addWidget(self.input_acero_fig1_base,6,1,1,2)
        self.main_grid1.addWidget(self.input_acero_fig1_alto,7,1,1,2)
        self.main_grid1.addWidget(self.input_acero_fig2_base,9,1,1,2)
        self.main_grid1.addWidget(self.input_acero_fig2_alto,10,1,1,2)
        self.main_grid1.addWidget(self.input_acero_fig3_base,12,1,1,2)
        self.main_grid1.addWidget(self.input_acero_fig3_alto,13,1,1,2)
        
        #IMAGEN
        
        #self.main_grid1.addWidget(self.imagen,0,9,25,20)
        
        #BOTON
        
        self.main_grid1.addWidget(self.boton_1,14,0,1,2)
        self.main_grid1.addWidget(self.boton_sgte,16,0,1,2)
        self.main_grid1.addWidget(self.boton_ayuda,18,0,1,2)
        self.main_grid1.addWidget(self.boton_ayuda1,19,0,1,2)
        
        #PANTALLA
        
        self.main_grid1.addWidget(self.pantalla,15,0,1,2)
        self.main_grid1.addWidget(self.error_mssg,17,0,1,2)
       
        
        
        w = QWidget()
        w.setLayout(self.main_grid1)
        self.setCentralWidget(w)
    
    def use_label_aux1(self, texto, color="ff9156"):
        self.error_mssg.setText(texto)
        self.error_mssg.setStyleSheet(f'color: #{color};')
        
    def calculo_areas(self):
        
        if (self.input_1_concreto_base.text() == "" or self.input_1_concreto_alto.text() == "" or self.input_acero_fig1_base.text() == "" or self.input_acero_fig1_alto.text() == "" or self.input_acero_fig2_base.text() == "" or self.input_acero_fig2_alto.text() == "" or self.input_acero_fig3_base.text() == "" or self.input_acero_fig3_alto.text() == ""):
            self.use_label_aux1("Todos los campos son obligatorios!")
            
        else:
            area_concreto_base = float(self.input_1_concreto_base.text().replace(",","."))
            area_concreto_alto = float(self.input_1_concreto_alto.text().replace(",","."))
            area_acero_fig1_base = float(self.input_acero_fig1_base.text().replace(",","."))
            area_acero_fig1_alto = float(self.input_acero_fig1_alto.text().replace(",","."))
            area_acero_fig2_base = float(self.input_acero_fig2_base.text().replace(",","."))
            area_acero_fig2_alto = float(self.input_acero_fig2_alto.text().replace(",","."))
            area_acero_fig3_base = float(self.input_acero_fig3_base.text().replace(",","."))
            area_acero_fig3_alto = float(self.input_acero_fig3_alto.text().replace(",","."))
            
            
            rta = self.controller.area_general(area_concreto_base, area_concreto_alto, area_acero_fig1_base, area_acero_fig1_alto, area_acero_fig2_base, area_acero_fig2_alto, area_acero_fig3_base, area_acero_fig3_alto)
            
            self.pantalla.setText("{:.5f} kN/m".format(rta))
            
            self.use_label_aux1("Datos Cargados Correctamente", "65ff56")
            self.boton_sgte.setStyleSheet("QPushButton {background-color: #5c5c5c; color: #dedede;}")
            
            self.boton_sgte.setEnabled(True)
            
        
    def ventana_final(self, cheked):
        if self.ventana_final1.isVisible():
            self.ventana_final1.hide()
        else:
            self.hide()
            self.ventana_final1.show()
            
            
            
    def mostrar_imagen_refencia(self):
        
        if self.referencia.isVisible():
            self.referencia.hide()
        else:
            #self.hide()
            self.referencia.show()
            
            
    def mostrar_imagen_coordenadas(self):
        
        if self.fig2d.isVisible():
            self.fig2d.hide()
        else:
            #self.hide()
            self.fig2d.show()
        
    

        
        
        


