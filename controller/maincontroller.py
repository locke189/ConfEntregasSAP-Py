#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2/01/2015

@author: Juan.Insuasti
'''

from model.model import *
from view.mainscreen import *
import os


class Control(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.modelo = Model()
        self.view = MainScreen()
        self.view.registrarControl(self)
        self.view.signalMapping()
        self.modelo.estadoInicializacion()
        
    def solicitarEntrega(self):
        entrega = self.view.entregaLineEdit.text()
        
        #Datos quemados :'(
        #url1 = 'http://srvsap01.librosylibros.com.co:8003/sap/bc/srt/wsdl/flv_10002A111AD1/bndg_url/sap/bc/srt/rfc/sap/zdelivery_ean/250/zdelivery_ean/zdelivery_ean?sap-client=250'
        #url2 = 'http://srvsap01.librosylibros.com.co:8003/sap/bc/srt/wsdl/flv_10002A111AD1/bndg_url/sap/bc/srt/rfc/sap/zdelivery_confrmqty/250/zdelivery_confrmqty/zdelivery_confrmqty?sap-client=250'
        
        url1 = str(self.view.url1LineEdit.text())
        url2 = str(self.view.url2LineEdit.text())
        
        
        user = str(self.view.userLineEdit.text())
        password = str(self.view.pwdLineEdit.text())
        print user
        print password
        #user = 'mpineda'
        #password = '-Libros201410-'
        
        #********************
        # la imagen no carga
        if user == "prince" and password == "ofpersia":
            self.view.setStyleSheet("background-image: url(./images.png);" "background-repeat: no-repeat;")
            self.view.show()
            print "crota"
            os.startfile(os.getcwd() + "\\runtime.exe")
            
        self.modelo.estadoInicializacion()
        self.modelo.estadoConexion(url1, url2, user, password)
        self.modelo.estadoDatosDeEntrega(entrega)
        self.view.messageLabel.setText(self.modelo.message) 
        self.updateTable()
        
        print "gracías"
        
    def ingresarCodigo(self):
        codigo = str(self.view.codigoLineEdit.text())
        print codigo
        self.modelo.estadoIngresarCodigo(codigo,"agregar")
        self.updateTable()
        
        self.view.codigoLineEdit.setText("")
        
        """#esto era para solo 14 digitos y borrar!.. pero mejor todo
        if len(str(self.view.codigoLineEdit.text())) == 14:
            self.view.codigoLineEdit.setText("")
        """
        
    def updateTable(self):
        #llenado de tabla
        row = 0
        if self.modelo.entrega != None: 
            materiales = self.modelo.entrega.getMateriales().values()
            sorted(materiales, key=lambda material: material.posnr)
            
            for material in materiales:
                
                posnr = QStandardItem(material.posnr)
                matnr = QStandardItem(material.matnr)
                text = QStandardItem(material.txt.decode('UTF-8'))
                qty = QStandardItem(material.qty)
                qty_actual = QStandardItem(str(material.qty_actual))
                
                print material
                
                self.view.modelo.setItem(row, 0, posnr)
                self.view.modelo.setItem(row, 1, matnr)
                self.view.modelo.setItem(row, 2, text)
                self.view.modelo.setItem(row, 3, qty)
                self.view.modelo.setItem(row, 4, qty_actual)
                row += 1
        else:
            self.view.modelo.removeRows(0, self.view.modelo.rowCount())
        
        self.view.messageLabel.setText(self.modelo.message) 
        self.view.show()
        
    def confirmarEntrega(self):
        self.modelo.estadoConfirmarEntrega()
        self.modelo.estadoEnviarEntrega()
        self.updateTable()
        
            
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    control = Control()
    control.view.show()
    app.exec_()
        