import pandas as pd

import warnings
warnings.simplefilter(action='ignore', category=Warning)

class Controller():
    
    GLOBAL = "N"
    dato_transformada = 0
    mod_acero = 0
    df = None
    INERCIA_TOTAL = 0
    
    def __init__(self, fname) -> None:
        self.GLOBAL = fname
    

    def transformada_general(self, cal_acero, cal_con, cal_longitud):
        
        #modulo de elasticidad del acero
        self.mod_acero=cal_acero
        
        #modulo de resistencia del concreto
        mod_concreto=cal_con
        
        #base de la viga de concreto
        base_longitud=cal_longitud
        
        n=self.mod_acero/mod_concreto
        
        #print("La relacion de modulos es",n)

        self.dato_transformada=base_longitud/n
        #print("Su sección transformada de la viga en concreto es de ", BT,"para modificar en el excel")
        #return dato_transformada




    def cargar_archivoxlsx(self, fname):
        self.df = pd.read_excel(fname)
        #print(self.df)

        n = len(self.df["X"])
        lista = [None]*n

        self.df["AREA"] = pd.Series(lista)
        #print(self.df)

        for i in range(len(self.df["X"])):
            if (i == len(self.df["X"])-1):
                self.df["AREA"][i] = self.df["Y"][i]
            else:
                self.df["AREA"][i] = (self.df["X"][i] * self.df["Y"][i+1]) - (self.df["X"][i+1] * self.df["Y"][i])
            
        #print(self.df)

        total=self.df["AREA"].sum()
        #print("el total del area del poligono es de", total)



        #CY.COLIMNA1

        self.df["CY1"] = pd.Series(lista)
        #print(self.df)

        for i in range(len(self.df["X"])):
            if (i == len(self.df["X"])-1):
                self.df["CY1"][i] = self.df["Y"][i]
            else:
                self.df["CY1"][i] = (self.df["X"][i] * self.df["Y"][i] * self.df["Y"][i+1])
            
        #print(self.df)

        total1=self.df["CY1"].sum()
        #print("el total del area del poligono es de", total1)


        #CY.COLIMNA2

        self.df["CY2"] = pd.Series(lista)
        #print(self.df)

        for i in range(len(self.df["X"])):
            if (i == len(self.df["X"])-1):
                self.df["CY2"][i] = self.df["Y"][i]
            else:
                self.df["CY2"][i] = (self.df["X"][i+1] * (self.df["Y"][i])**2)
                
            
        #print(self.df)

        total2=self.df["CY2"].sum()
        #print("el total del area del poligono es de", total2)

        #CY.COLIMNA3

        self.df["CY3"] = pd.Series(lista)
        #print(self.df)

        for i in range(len(self.df["X"])):
            if (i == len(self.df["X"])-1):
                self.df["CY3"][i] = self.df["Y"][i]
            else:
                self.df["CY3"][i] = (self.df["X"][i] * (self.df["Y"][i+1])**2)
                
            
        #print(self.df)
        total3=self.df["CY3"].sum()
        #print("el total del area del poligono es de", total3)

        #CY.COLIMNA4

        self.df["CY4"] = pd.Series(lista)
        #print(self.df)

        for i in range(len(self.df["X"])):
            if (i == len(self.df["X"])-1):
                self.df["CY4"][i] = self.df["Y"][i]
            else:
                self.df["CY4"][i] = (self.df["X"][i+1] * self.df["Y"][i] * self.df["Y"][i+1])
                
            
        #print(self.df)
        total4=self.df["CY4"].sum()
        #print("el total del area del poligono es de", total4)




        #Ix.COLUMNA1

        self.df["IX1"] = pd.Series(lista)
        #print(self.df)

        for i in range(len(self.df["X"])):
            if (i == len(self.df["X"])-1):
                self.df["IX1"][i] = self.df["Y"][i]
            else:
                self.df["IX1"][i] = (self.df["X"][i] * (self.df["Y"][i])**2 * self.df["Y"][i+1])
                
            
        #print(self.df)
        total5=self.df["IX1"].sum()
        #print( total5)

        #Ix.COLUMNA2

        self.df["IX2"] = pd.Series(lista)
        #print(self.df)

        for i in range(len(self.df["X"])):
            if (i == len(self.df["X"])-1):
                self.df["IX2"][i] = self.df["Y"][i]
            else:
                self.df["IX2"][i] = (self.df["X"][i] * (self.df["Y"][i]) * (self.df["Y"][i+1])**2)
                
            
        #print(self.df)
        total6=self.df["IX2"].sum()
        #print( total6)

        #Ix.COLUMNA3

        self.df["IX3"] = pd.Series(lista)
        #print(self.df)

        for i in range(len(self.df["X"])):
            if (i == len(self.df["X"])-1):
                self.df["IX3"][i] = self.df["Y"][i]
            else:
                self.df["IX3"][i] = (self.df["X"][i] * (self.df["Y"][i+1])**3)
                
            
        #print(self.df)
        total7=self.df["IX3"].sum()
        #print( total7)

        #Ix.COLUMNA4

        self.df["IX4"] = pd.Series(lista)
        #print(self.df)

        for i in range(len(self.df["X"])):
            if (i == len(self.df["X"])-1):
                self.df["IX4"][i] = self.df["Y"][i]
            else:
                self.df["IX4"][i] = (self.df["X"][i+1] * (self.df["Y"][i])**3)
                
            
        #print(self.df)
        total8=self.df["IX4"].sum()
        #print( total8)

        #Ix.COLUMNA5

        self.df["IX5"] = pd.Series(lista)
        #print(self.df)

        for i in range(len(self.df["X"])):
            if (i == len(self.df["X"])-1):
                self.df["IX5"][i] = self.df["Y"][i]
            else:
                self.df["IX5"][i] = (self.df["X"][i+1] * (self.df["Y"][i])**2*(self.df["Y"][i+1]))
                
            
        #print(self.df)
        total9=self.df["IX5"].sum()
        #print( total9)

        #Ix.COLUMNA6

        self.df["IX6"] = pd.Series(lista)
        #print(self.df)

        for i in range(len(self.df["X"])):
            if (i == len(self.df["X"])-1):
                self.df["IX6"][i] = self.df["Y"][i]
            else:
                self.df["IX6"][i] = (self.df["X"][i+1] * (self.df["Y"][i])*(self.df["Y"][i+1])**2)
                
        #print(self.df)

        total10=self.df["IX6"].sum()
        #print( total10)

        AREA1=total*0.5
        #print("El area total es de",AREA1)

        CENTROIDEY=(1/(6*AREA1)*(total1-total2+total3-total4))
        inerciaX=((0.0833333333)*(total5+total6+total7-total8-total9-total10))
        self.INERCIA_TOTAL=(inerciaX-AREA1*CENTROIDEY**2)

        
        
        
        
        return self.INERCIA_TOTAL




    def area_general(self, area_concreto_base, area_concreto_alto, area_acero_fig1_base, area_acero_fig1_alto, area_acero_fig2_base, area_acero_fig2_alto, area_acero_fig3_base, area_acero_fig3_alto):
        
        global area_total
        #area total del concreto
        area_concreto_base = area_concreto_base
        
        area_concreto_alto = area_concreto_alto
        
        area_total_concreto = 23.544*(area_concreto_base * area_concreto_alto)
        
        #area total fig1 acero
        
        area_acero_fig1_base = area_acero_fig1_base
        
        area_acero_fig1_alto = area_acero_fig1_alto
        
        area_total_fig1 = area_acero_fig1_base * area_acero_fig1_alto
        
        #area total fig2 acero
        
        area_acero_fig2_base = area_acero_fig2_base
        
        area_acero_fig2_alto = area_acero_fig2_alto
        
        area_total_fig2 = area_acero_fig2_base * area_acero_fig2_alto
        
        #area total fig3 acero
        
        area_acero_fig3_base = area_acero_fig3_base
        
        area_acero_fig3_alto = area_acero_fig3_alto
        
        area_total_fig3 = area_acero_fig3_base * area_acero_fig3_alto
        
        #area total del acero todas las figuras
        
        area_total_acero = 76.518 * (area_total_fig1 + area_total_fig2 + area_total_fig3)
        
        
        
        area_total = area_total_concreto + area_total_acero
        
        
        
        return area_total

        


    def deflexion_general(self, longitud_total, carga1, longitudx1, carga2, longitudx2):

        
        #print("Ingrese la longitud de la viga")
        #LV= float(input())#
        LV=longitud_total
        D3=LV/2
        #print("Ingrese la primera carga (KN)")
        #W1= float(input())#
        W1=carga1
        #print("Ingrese la distancia mas corta de donde esta la primera carga")
        #D1= float(input())#
        D1=longitudx1
        #print("Ingrese la segunda carga (KN)")
        #W2= float(input())#
        W2=carga2
        #print("Ingrese la distancia mas larga de donde esta la segunda carga")
        #D2= float(input())#
        D2=longitudx2
        W3=area_total*LV
        #print("La carga puntual es",W3)

        Ma=(-W1*D1)-(W3*D3)-(W2*D2)
        #print("El momento es",Ma)

        By=(-Ma/LV)
        Fy=-(-W1-W3-W2+By)
        #print("La fuerza es",By)
        #print("La fuerza es",Fy)

        #print("Tramo 1")

        Ms=-((area_total)/2)
        Ms1=-(-Fy)
        #print("Momento total",Ms,Ms1)

        #print("Tramo 2")

        Ms2=W1
        Ms3=-(W1*-D1)
        Ms4=(-area_total/2)
        Ms5=-Fy
        Ms6=-(Ms2+(Ms5))


        #print("Momento total",Ms4,Ms6,Ms3)

        #print("Tramo 3")

        M2=W2
        M2a=W2*-D2
        M2b=W1
        M2c=W1*-D1
        M2d=area_total/2
        M2e=-Fy

        #OPERACIONES#

        MT2=-(M2+(M2b)+(M2e))
        MT2a=-(M2a+(M2c))
        M2d1=-(M2d)
        #print("Momento total",M2d1,MT2,MT2a)

        #DOBLE INTEGRACIÓN# (A-B) 

        #print("tramo 1")

        EIy=Ms/3
        EIy1=Ms1/2

        EIya=EIy/4
        EIyb=EIy1/3

        #print("Es",EIya,EIyb)

        #print("tramo 2")

        EIys=Ms4/3
        EIyj=Ms6/2
        EIyñ=Ms3/2

        EIyS1=EIys/4
        EIyJ1=EIyj/3

        #print("es",EIyS1,EIyJ1,EIyñ)

        #print("tramo 3")

        EIy23=M2d1/3
        EIy3k=MT2/2
        EIy3l=MT2a/2

        EIyf=EIy23/4
        EIyg=EIy3k/3

        #print("Es",EIyf, EIyg,EIy3l)

        #HALLAR CONSTANTES#


        #print("TRAMO1")
        a=0
        C2=EIy*(a)**4+EIy1*(a)**3

        #print("La constante C1 es",C2)

        C1C3a=EIy*(D1)**3+EIy1*(D1)**2
        C1C3b=EIys*(D1)**3+EIyj*(D1)**2+Ms3*(D1)
        C1C3=(C1C3b-C1C3a)
        #print("La constante C1-C3 es",C1C3)

        Ca=EIya*(D1)**4+EIyb*(D1)**3
        Cb=(EIyS1*(D1)**4)+(EIyJ1*(D1)**3)+(EIyñ*(D1)**2)
        #print(Ca,Cb)


        Ca1=-Cb+Ca
        C4=D1*C1C3+Ca1
        #print("La constante C4 es",C4)

        #"TRAMO 2"

        #PRINCIPIO DE CONTINUIDAD# 2 Y 3

        Cb1=(EIys*(D2)**3)+(EIyj*(D2)**2)+(Ms3*(D2))
        Cb2=(EIy23*(D2)**3)+(EIy3k*(D2)**2)+(MT2a*(D2))
        C3C5=Cb2-Cb1
        #print("La constante C3-C5 es",C3C5)


        d1=(EIyS1*(D2)**4)+(EIyJ1*(D2)**3)+(EIyñ*(D2)**2)+(C4)
        d2=(EIyf*(D2)**4)+(EIyg*(D2)**3)+(EIy3l*(D2)**2)
                                        
        #print(d1,d2)

        Ca2=-d1+d2
        C6=D2*(C3C5)-Ca2
        #print("La constante C4 es",C6)


        #"TRAMO 3"
        E1=(EIyf*(LV)**4)+(EIyg*(LV)**3)+(EIy3l*(LV)**2)+(C6)
        C5=-E1/LV
        #print("La constante C5 es",C5)

        C3=C3C5+(C5)

        #print("La constante C3 es",C3)

        C1=C1C3+(C3)

        #print("La constante C1 es",C1)

        #"PARA CENTRO DE LUZ"

        EJ1=(EIyS1*(D3)**4)+(EIyJ1*(D3)**3)+(EIyñ*(D3)**2)+(C3*(D3))+(C4)

        #print("La constante EJ1 es",EJ1)

        #YCL=(EJ1/((INERCIATOTAL*es)))
        
        
        YCL=(EJ1/((self.INERCIA_TOTAL*(self.mod_acero*1000))))
        
        return YCL


        #print("LA DEFLEXIÓN EN EL CENTRO DE LUZ ES",YCL)
        
        
        
