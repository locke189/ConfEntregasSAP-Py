#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2/01/2015

@author: Juan.Insuasti
'''

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import controller
from win32netcon import PASSWORD_EXPIRED

class MainScreen(QTabWidget):
    '''
    classdocs
    '''


    def __init__(self,parent=None):
        '''
        Constructor
        '''
        super(MainScreen, self).__init__(parent)
        
        #conexion con el controller
        
        self.control = None
        self.setWindowTitle('Confirmación de entregas v0.4'.decode('UTF-8'))
        #Label estatico
        
        #mod_user_pwd
        userLabel = QLabel("Usuario")
        pwdLabel = QLabel("Password") 
        url1Label = QLabel("URL zdelivery_ean")
        url2Label = QLabel("URL zdelivery_confrmqty")
        #end mod
        
        
        
        entregaLabel = QLabel("Entrega")
        codigoLabel = QLabel("Cod. de Barras")
        estadoLabel = QLabel("Estado:")
        self.messageLabel = QLabel("...")
        #Input boxes dinamicas
        
        #mod_user_pwd
        self.userLineEdit = QLineEdit("")
        self.pwdLineEdit = QLineEdit("")
        self.pwdLineEdit.setEchoMode(QLineEdit.Password)
        self.url1LineEdit = QLineEdit("http://srvsap01.librosylibros.com.co:8003/sap/bc/srt/wsdl/flv_10002A111AD1/bndg_url/sap/bc/srt/rfc/sap/zdelivery_ean/250/zdelivery_ean/zdelivery_ean?sap-client=250")
        self.url2LineEdit = QLineEdit("http://srvsap01.librosylibros.com.co:8003/sap/bc/srt/wsdl/flv_10002A111AD1/bndg_url/sap/bc/srt/rfc/sap/zdelivery_confrmqty/250/zdelivery_confrmqty/zdelivery_confrmqty?sap-client=250")
        #endmod
        
        self.entregaLineEdit = QLineEdit("")
        self.codigoLineEdit = QLineEdit("")
        #Botones dinamicos
        self.entregaPushButton =  QPushButton("Traer Entrega")
        self.codigoPushButton =   QPushButton("Ingresar Cod.")
        self.confirmarPushButton = QPushButton("Confirmar Entrega")
        
        #Tabla
        self.matTableView = QTableView()
        
        #Tabla - self.modelo
        
        self.modelo = QStandardItemModel(0,5)
        self.modelo.setHeaderData(0, Qt.Horizontal, "Pos")
        self.modelo.setHeaderData(1, Qt.Horizontal, "Material")
        self.modelo.setHeaderData(2, Qt.Horizontal, "Descripcion")
        self.modelo.setHeaderData(3, Qt.Horizontal, "Req.")
        self.modelo.setHeaderData(4, Qt.Horizontal, "Cant")
                
        self.matTableView.setModel(self.modelo)
        
        #Tamano de las columnas
        
        self.matTableView.setColumnWidth(0,60)
        self.matTableView.setColumnWidth(1,120)
        self.matTableView.setColumnWidth(2,120)
        self.matTableView.setColumnWidth(3,40)
        self.matTableView.setColumnWidth(4,40)
        
        #Tabla ingresar datos
        
        #w = QStandardItem("000010")
        #x = QStandardItem("000000011120112212")
        #y = QStandardItem("10")
        #z = QStandardItem("5")
        #zz = QStandardItem("9")
        
        #self.modelo.setItem(0, 0, w)
        #self.modelo.setItem(0, 1, x)
        #self.modelo.setItem(0, 2, y)
        #self.modelo.setItem(0, 3, z)
        #self.modelo.setItem(0, 3, zz)
        

        
        #La tabla debe ser no editable
        self.matTableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        print self.matTableView.NoEditTriggers
        
        #GRID
        
        
        grid = QGridLayout()
        grid.addWidget(entregaLabel, 0, 0)
        grid.addWidget(self.entregaLineEdit, 0, 1)
        grid.addWidget(self.entregaPushButton, 0, 2)
        grid.addWidget(codigoLabel,1, 0)
        grid.addWidget(self.codigoLineEdit, 1, 1)
        grid.addWidget(self.codigoPushButton, 1, 2)
        grid.addWidget(self.matTableView,2,0,1,4)
        grid.addWidget(estadoLabel,3,0)
        grid.addWidget(self.messageLabel,3,1,1,2)
        grid.addWidget(self.confirmarPushButton,3,2)
        #grid.addWidget(userLabel,0,0)
        #grid.addWidget(self.userLineEdit,0,1)
        #grid.addWidget(pwdLabel,1,0)
        #grid.addWidget(self.pwdLineEdit,1,1)
        
        #self.setLayout(grid)
       
        
       
        grid2 = QGridLayout()
        grid2.addWidget(userLabel,0,0,Qt.AlignTop)
        grid2.addWidget(self.userLineEdit,0,1)
        grid2.addWidget(pwdLabel,1,0)
        grid2.addWidget(self.pwdLineEdit,1,1)
        grid2.addWidget(url1Label,2,0)
        grid2.addWidget(self.url1LineEdit,2,1)
        grid2.addWidget(url2Label,3,0)
        grid2.addWidget(self.url2LineEdit,3,1)
        #self.setLayout(grid2)
        
        #tabs
        
        tab_app = QWidget()
        tab_conf = QWidget()
        
        tab_app.setLayout(grid)
        tab_conf.setLayout(grid2)
        #tab = QTabWidget()
        
        
        #pallete?
        """
        palette = QPalette()
        
        self.setPalette( palette );
        self.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.483, cy:0.522727, radius:0.341, fx:0.477636, fy:0.522, stop:0.471591 rgba(202, 38, 223, 255), stop:0.579545 rgba(202, 38, 223, 255), stop:0.931818 rgba(0, 0, 0, 255));")
        palette.setColor( QPalette.Window, QColor( "light blue" ) );
        
        #self.setLayout(tab)
        """
        self.addTab(tab_conf, "Config." )
        self.addTab(tab_app, "Entregas" )
        


        
    def registrarControl(self,control):
        #registro del control
        self.control = control
        
    def signalMapping(self):
        #Mapeo de senales
        self.connect(self.entregaPushButton, SIGNAL("clicked()"),self.control.solicitarEntrega)
        self.connect(self.entregaLineEdit, SIGNAL("returnPressed()"),self.control.solicitarEntrega)
        
        self.connect(self.codigoPushButton, SIGNAL("clicked()"),self.control.ingresarCodigo)
        self.connect(self.codigoLineEdit, SIGNAL("returnPressed()"),self.control.ingresarCodigo)
        
        
        self.connect(self.confirmarPushButton, SIGNAL("clicked()"),self.control.confirmarEntrega)
        
        
if __name__ == '__main__':        
    app = QApplication(sys.argv)
    form = MainScreen()
    form.show()
    app.exec_()
        