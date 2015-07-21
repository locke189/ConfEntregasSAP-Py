'''
Created on 29/12/2014

@author: Juan.Insuasti
'''

class Material(object):
    '''
    Clase que contiene la logica del manejo de un material
    de la entrega.
    '''


    def __init__(self, matnr, data):
        '''
        Constructor
        '''
        self.matnr = matnr
        self.data = data
        self.posnr = self.data.getPos(matnr)
        self.qty = self.data.getRequiredMat(matnr)
        self.txt = self.data.getTxt(matnr).encode("UTF-8")
        #cantidad actual del pedido
        self.qty_actual = 0
        self.lista_de_envio = []
        self.status = 'incompleto'
        
    
    def agregarItem(self, code):
        
        #if the delivery quantity is lower than the actual quantity
        if self.qty_actual < self.qty and self.status == "incompleto":
            
            print float(self.data.checkCodeQty(code)) + float(self.qty_actual) , float(self.qty)
            suma_futura = float(self.data.checkCodeQty(code)) + float(self.qty_actual)
            
            if suma_futura <= float(self.qty):
                print "paso"
                self.qty_actual += float(self.data.checkCodeQty(code))
                self.lista_de_envio.append(code)
            
            if self.qty == self.qty_actual:
                self.status = 'completo'
                
    def eliminarItem(self,code):
        pass
        
    
    