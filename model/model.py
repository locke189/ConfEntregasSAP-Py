'''
Created on 29/12/2014


@author: Juan.Insuasti
'''


from datosentrega import DatosDeEntrega
from entrega import Entrega
from webservice import WSHandler_InfoEntrega, WSHandler_ConfirmarEntrega


class Model(object):
    '''
    classdocs
    '''
        

    def __init__(self):
        '''
        Constructor
        '''
        self.estadoInicializacion()
        
    def estadoInicializacion(self):
        #estos datos se deberan tomar de alguna parte por ahora van quemados
        self.state = "Inicializacion"
        self.message = ""
        self.conexion = None
        self.entrega = None
        self.conexion2 = None
    
    def estadoConexion(self, url_entrega, url_confirm, user, password):
        '''
        Cambio de estado inicializacion a estado conexion, se crean las conexiones a los Web services.
        '''
        if self.state == "Inicializacion":
            
            try:
                self.conexion = WSHandler_InfoEntrega(url_entrega,user,password)
                self.conexion2 = WSHandler_ConfirmarEntrega(url_confirm,user,password)
                self.state = "Conexion"
            except:
                self.estadoInicializacion()
                self.message = "Error al crear la conexion"
                
                
                
    def estadoDatosDeEntrega(self,entrega):
        '''
        Si se esta en el estado conexion, busca un numero de entrega y trae la informacion de SAP 
        '''
        if self.state == "Conexion":
            
            '''
            result = self.conexion.getInfo(entrega)
            print result
            data = DatosDeEntrega(result)
            self.entrega = Entrega(data,entrega)
            self.state = "Entrega Lista"

                
            if  self.entrega.picking == 'X':
                self.estadoInicializacion()
                self.message = "Error: Entrega con Picking"
                
            else:
                self.message = "Entrega = " + entrega

            
            '''
            try:
                result = self.conexion.getInfo(entrega)
                print result
                data = DatosDeEntrega(result)
                self.entrega = Entrega(data,entrega)
                self.state = "Entrega Lista"

                
                if  self.entrega.picking == 'X':
                    self.estadoInicializacion()
                    self.message = "Error: Entrega con Picking"
                
                else:
                    self.message = "Entrega = " + entrega
                
            except:
                self.estadoInicializacion()
                self.message = "Error: No se puede realizar la conexion con el servidor"
                    
            
            
    def estadoIngresarCodigo(self,codigo,modo):
        '''
        Aqui se ingresan los Codigos de barra y se suman las cantidades
        '''
        if self.state == "Entrega Lista": 
            
            try:
                #print self.state
                if modo == "agregar": 
                    self.entrega.agregarCodigo(codigo)
            
            except:
                self.message = "Error: Codigo incorrecto"
        
    def estadoConfirmarEntrega(self):
        '''
        Se prepara el paquete a ser enviado por web service a SAP
        '''
        if self.state == "Entrega Lista":
            
            try:
                self.numero_entrega , self.items_entrega  = self.entrega.finalizarEntrega()
                
                
                if self.items_entrega == []:
                    raise Exception
                else:
                    self.state = "Paquete Listo"
            except:
                self.message = "Error: no se pueden preparar los datos de la entrega" 
                
                
                
    def estadoEnviarEntrega(self):
        '''
        Se envia el paquete por webservice a SAP.
        '''
        if self.state == "Paquete Listo":
            try:
                result = self.conexion2.confirmarEntrega(self.numero_entrega, self.items_entrega)
                
                if result.OKDATA == 'X':
                    self.message = "Error: La entrega " + str(self.numero_entrega) + " se debe confirmar de manera manual"
                else:
                    self.estadoInicializacion()
                    self.message = "Entrega Confirmada"
            except:
                self.message = "Error: no se puede comunicar con el servidor"
                
        
if __name__ == '__main__':
        
        url1 = 'http://srvsap01.librosylibros.com.co:8003/sap/bc/srt/wsdl/flv_10002A111AD1/bndg_url/sap/bc/srt/rfc/sap/zdelivery_ean/250/zdelivery_ean/zdelivery_ean?sap-client=250'
        url2 = 'http://srvsap01.librosylibros.com.co:8003/sap/bc/srt/wsdl/flv_10002A111AD1/bndg_url/sap/bc/srt/rfc/sap/zdelivery_confrmqty/250/zdelivery_confrmqty/zdelivery_confrmqty?sap-client=250'
        user = 'mpineda'
        password = '-Libros201410-'
        
        modelo = Model()
        modelo.estadoInicializacion()
        print modelo.state, modelo.message
        modelo.estadoConexion(url_entrega = url1, url_confirm = url2, user = user, password = password)
        print modelo.state, modelo.message
        modelo.estadoDatosDeEntrega('0080000230')
        print modelo.state, modelo.message
        modelo.estadoIngresarCodigo("97895872418221","agregar")
        print modelo.state, modelo.message
        modelo.estadoIngresarCodigo("9789587241952","agregar")
        print modelo.state, modelo.message
        modelo.estadoIngresarCodigo("9789587241969","agregar")
        print modelo.state, modelo.message
        modelo.estadoConfirmarEntrega()
        print modelo.state, modelo.message
        #modelo.estadoEnviarEntrega()
        #print modelo.state, modelo.message
        #modelo.estadoConfirmarEntrega()
        
        