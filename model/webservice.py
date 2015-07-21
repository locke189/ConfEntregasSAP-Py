
'''
Created on 23/12/2014

@author: Juan.Insuasti
'''

#El paquete de suds maneja las comunicaciones por WebService
from suds.client import Client


class WSHandler_InfoEntrega(object):
    '''
    Realiza la comunicacin con el WS de obtener informaci sobre entregas
    '''
    
    def __init__(self, wsdl_url,user,password):
        '''
        Constructor: Toma el la url del WSDL, el usuario y la contrase sin encriptar.
        '''
        self.url = wsdl_url
        self.user = user
        self.password = password
        self.client =  Client(self.url, username=self.user, password=self.password)
        
    def getInfo(self, vbeln):
        '''
        Invoca el mtodo ZsdDeliveryEan del webService, vbeln es el numero de entrega.
        '''
        #the ws method is ZsdDeliveryEan
        self.result = self.client.service.ZsdDeliveryEan(Vbeln = vbeln)
        # do i require a different extractor?
        return self.result
    
class WSHandler_ConfirmarEntrega(object):
    '''
    Invocaci del webservice de confirmacin de entregas
    '''
    
    def __init__(self, wsdl_url,user,password):
        '''
        Constructor
        
        '''
        self.url = wsdl_url
        self.user = user
        self.password = password
        self.client =  Client(self.url, username=self.user, password=self.password)
        
    def confirmarEntrega(self, entrega, items):
        '''
        Invoca el mtodo ZsdDeliveryEan del webService, entrega es el numero de entrega y items es una lista de diccionarios.
        
        '''
        #the ws method is ZsdDeliveryEan
       
        p_cantidades = self.client.factory.create('TABLE_OF_ZDELIV_CANTPICK')
        
        
        
        sorted(items, key=lambda item: item['POSNR'])
        
        for posicion in items:
            p_item = self.client.factory.create('ZDELIV_CANTPICK')
            p_item.VBELN = posicion['VBELN']
            p_item.POSNR = posicion['POSNR']
            p_item.MATNR = posicion['MATNR']
            p_item.PIKMG = posicion['PIKMG']
            
            p_cantidades.item.append(p_item)
        
        print p_cantidades
        
        self.result = self.client.service.ZSD_DELIVERY_CONFCANT(P_CANTIDADES = p_cantidades, P_ENTREGA = entrega)
        # do i require a different extractor?
        return self.result

if __name__ == '__main__':
    
    case = 1

    if case == 1:

        url = 'http://srvsap01.librosylibros.com.co:8003/sap/bc/srt/wsdl/flv_10002A111AD1/bndg_url/sap/bc/srt/rfc/sap/zdelivery_ean/250/zdelivery_ean/zdelivery_ean?sap-client=250'
        user = 'mpineda'
        password = '-Libros201410-'
        
        conexion = WSHandler_InfoEntrega(url,user,password)
        result = conexion.getInfo('0080000227')
        
        '''
        client = Client(url, username='mpineda', password='-Libros201410-')
        print client
        result = client.service.ZsdDeliveryEan(Vbeln = '0080000227')
        '''
        
        print result.Kostk
        
        print len(result.Itemtab.item)    
            
        for item in result.Itemtab.item:
            print item.Posnr
            
        #print result.Itemtab.item[0].Posnr

    elif case == 2:
        
        print "parte 2"
        
        url = 'http://srvsap01.librosylibros.com.co:8003/sap/bc/srt/wsdl/flv_10002A111AD1/bndg_url/sap/bc/srt/rfc/sap/zdelivery_confrmqty/250/zdelivery_confrmqty/zdelivery_confrmqty?sap-client=250'
        user = 'mpineda'
        password = '-Libros201410-'
        
        conexion = WSHandler_ConfirmarEntrega(url,user,password)
        
        print conexion.client
        
        c_cantidades = []
        i_cantidades = {}
        
        i_cantidades['VBELN'] = '0080000231'
        i_cantidades['POSNR'] = '000010'
        i_cantidades['MATNR'] = '000000011120112212'
        i_cantidades['PIKMG'] = '2'
        
        c_cantidades.append(i_cantidades)
        
        print c_cantidades
        
        i_cantidades = {}
                
        i_cantidades['VBELN'] = '0080000231'
        i_cantidades['POSNR'] = '000020'
        i_cantidades['MATNR'] = '000000011120212212'
        i_cantidades['PIKMG'] = '4'
        
        print i_cantidades
        
        c_cantidades.append(i_cantidades)
        
        print c_cantidades
        
        result = conexion.confirmarEntrega( '0080000221', c_cantidades  )
        
        print result
        
        