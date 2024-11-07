import sys
from PyQt6.QtCore import QSize, Qt, pyqtSlot
from PyQt6.QtWidgets import (QApplication, QLabel, QWidget, QLineEdit,QTextEdit, QPushButton, QGridLayout, QMainWindow, QFileDialog)

from PyQt6.QtGui import QFont, QPixmap, QMovie

import warnings
warnings.simplefilter(action='ignore', category=Warning)

from cal_general import Controller

from Interfaz_Areas import AnotherWindow
from ventana_ayuda import MainWindow2


class MainWindow(QWidget):
    
    controller = Controller("n")
    global input_1_acero, input_2_concreto, input_3_longitud, pantalla, area_ventana, fname
    
    
    def __init__(self):
        super().__init__()
        self.inicializar_ui()
        
        self.ayuda = MainWindow2()
        
        
        
    def inicializar_ui(self):
        self.setGeometry(100,100,1100,300)
        self.setWindowTitle("VIGA SECCION COMPUESTA")
        self.setStyleSheet("background-color: #2e2e2e")
        self.generar_interfaz()
        self.show()
      

    def generar_interfaz(self):
        
        
        self.pixmap = QPixmap("Img/VIGACOMPUESTA.png")
        self.imagen = QLabel(self)
        self.imagen.setPixmap(self.pixmap)
        
        #self.pixmap1 = QPixmap("EXCEL.png")
        #self.imagen1 = QLabel(self)
        #self.imagen1.setPixmap(self.pixmap1)
        
        fuente = QFont("Arial",11)
        fuente1 = QFont("Arial",20)
                
        user_label = QLabel()
        user_label.setText("Información general de la viga: ")
        user_label.setFont(fuente)
        
        mod_elast_ace = QLabel()
        mod_elast_ace.setText("Módulo elástico del acero (MPa)")
        mod_elast_ace.setFont(fuente)
        
        mod_elast_con = QLabel()
        mod_elast_con.setText("Módulo elástico del concreto (MPa)")
        mod_elast_con.setFont(fuente)
        
        base_viga = QLabel()
        base_viga.setText("(bc) Ancho de la losa del concreto (metros)")
        base_viga.setFont(fuente)
        
        dato_nuevo = QLabel()
        dato_nuevo.setText("Ancho de la sección transformada de la losa del concreto a modificar: (bc)  ")
        dato_nuevo.setFont(fuente)
        
        self.pantalla = QTextEdit(self)
        self.pantalla.setDisabled(True)
        self.pantalla.setFont(fuente1)
        #self.pantalla.setFont(QFont("Times New Roman",12))
        
        self.input_1_acero = QLineEdit(self)
        self.input_1_acero.setPlaceholderText("MPa")
        
        self.input_2_concreto = QLineEdit(self)
        self.input_2_concreto.setPlaceholderText("MPa")
        
        self.input_3_longitud = QLineEdit(self)
        self.input_3_longitud.setPlaceholderText("metros")
        
        self.error_mssg = QLabel()
        self.error_mssg.setText("")
        self.error_mssg.setFont(fuente)
        
        
        boton_1 = QPushButton()
        boton_1.setText("Verificar")
        boton_1.setFont(QFont(fuente))
        boton_1.clicked.connect(self.convertir_palabra)
        boton_1.setStyleSheet("QPushButton {background-color: #5c5c5c; color: #dedede;}")
        
        self.boton_cargar = QPushButton()
        self.boton_cargar.setText("Cargar Archivo de Excel")
        self.boton_cargar.setFont(fuente)
        self.boton_cargar.clicked.connect(self.cargar_archivo)
        self.boton_cargar.setEnabled(False)
        self.boton_cargar.setStyleSheet("QPushButton {background-color: #5c5c5c; color: #9e9e9e;}")
        
        self.boton_sigtepaso = QPushButton()
        self.boton_sigtepaso.setText("Paso Siguiente")
        self.boton_sigtepaso.setFont(fuente)
        self.boton_sigtepaso.clicked.connect(self.ventana_areas)
        self.boton_sigtepaso.setEnabled(False)
        self.boton_sigtepaso.setStyleSheet("QPushButton {background-color: #5c5c5c; color: #9e9e9e;}")
        
        self.boton_ayuda = QPushButton()
        self.boton_ayuda.setText("¿Cómo debo cargar Excel?")
        self.boton_ayuda.setFont(fuente)
        self.boton_ayuda.clicked.connect(self.mostrar_imagen)
       
        self.boton_ayuda.setStyleSheet("QPushButton {background-color: #b2af39; color: #dedede;}")
        
        
        
        self.main_grid = QGridLayout()
        self.main_grid.addWidget(user_label,0,0,1,1)
        
        self.main_grid.addWidget(mod_elast_ace,1,0,1,1)
        self.main_grid.addWidget(mod_elast_con,2,0,1,1)
        self.main_grid.addWidget(base_viga,3,0,1,1)
        self.main_grid.addWidget(dato_nuevo,4,0,1,1)
        
        self.main_grid.addWidget(self.input_1_acero, 1, 1, 1, 12)
        self.main_grid.addWidget(self.input_2_concreto, 2, 1, 1, 12)
        self.main_grid.addWidget(self.input_3_longitud, 3, 1, 1, 12)
        
        self.main_grid.addWidget(self.pantalla, 5, 0, 1, 12)
        
        self.main_grid.addWidget(boton_1,6,0,1,12)
        self.main_grid.addWidget(self.boton_cargar,7,0,1,12)
        self.main_grid.addWidget(self.boton_sigtepaso,8,0,1,12)
        
        self.main_grid.addWidget(self.error_mssg,10,0,1,12)
        
        self.main_grid.addWidget(self.boton_ayuda,12,0,1,12)
        
        
        self.main_grid.addWidget(self.imagen,0,13,25,20)
        
        
        self.setLayout(self.main_grid)
    
    def use_label_aux(self, texto, color="ff9156"):
        self.error_mssg.setText(texto)
        self.error_mssg.setStyleSheet(f'color: #{color};')
    
    def convertir_palabra(self):
        if(self.input_1_acero.text() == "" or self.input_2_concreto.text()=="" or self.input_3_longitud.text()==""):
            self.use_label_aux("Todos los campos son obligatorios!")
        else:
            cal_acero = float(self.input_1_acero.text().replace(",","."))
            cal_con = float(self.input_2_concreto.text().replace(",","."))
            cal_longitud = float(self.input_3_longitud.text().replace(",","."))
            
            self.controller.transformada_general(cal_acero, cal_con, cal_longitud)
            self.pantalla.setText("{:.5f} m".format(self.controller.dato_transformada))
            self.use_label_aux("Datos Cargados Correctamente", "65ff56")
            self.boton_cargar.setStyleSheet("QPushButton {background-color: #5c5c5c; color: #dedede;}")
            
            self.boton_cargar.setEnabled(True)
            
            
        
    @pyqtSlot()    
    def cargar_archivo(self):
        file_excel = QFileDialog.getOpenFileName(
            self,
            "Open File",
            "${HOME}",
            "Excel File (*.xlsx *.xls)",)
        
        if (len(file_excel[0]) > 0 ):
            self.controller.GLOBAL, _ = file_excel
            self.area_ventana = AnotherWindow(self.controller)
            self.boton_sigtepaso.setEnabled(True)
            #print(f"NOMBRE: {self.controller.GLOBAL}")
            
            self.use_label_aux("Archivo excel cargado!", "65ff56")
            self.boton_sigtepaso.setStyleSheet("QPushButton {background-color: #5c5c5c; color: #dedede;}")
            
        else: 
            self.use_label_aux("Archivo excel es requerido!")
        
        
    def ventana_areas(self, cheked):
        if self.area_ventana.isVisible():
            self.area_ventana.hide()
        else:
            self.hide()
            self.area_ventana.show()
            
    def mostrar_imagen(self):
        
        if self.ayuda.isVisible():
            self.ayuda.hide()
        else:
            #self.hide()
            self.ayuda.show()
        
        
        
        
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()



        
        
        
