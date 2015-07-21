'''
Created on 29/12/2014

@author: Juan.Insuasti
'''
from material import Material

class Entrega(object):
    '''
    classdocs
    '''


    def __init__(self, data, delivery):
        '''
        Constructor
        '''
        self.entrega = delivery
        self.send_data = {}
        self.data = data
        self.materiales = {}
        self.picking = data.pickingCheck()
        
        for matnr in self.data.getMaterials():
            material = Material(matnr,data)
            self.materiales[matnr] = material
                    
            
    def agregarCodigo(self,codigo):
        matnr = self.data.checkCodeMat(codigo)
        if matnr in self.materiales.keys():
            self.materiales[matnr].agregarItem(codigo)
            
            print "material = ", matnr
            print "cantidad actual = ", self.materiales[matnr].qty_actual
            print "cantidad requerida = ", self.materiales[matnr].qty
            
    
    def finalizarEntrega(self):
        '''
        '''
        items = []
        
        
        
        for material in self.materiales.values():
            
            #Verificacion de que las entregas esten llenas
            
            print material.qty
            print material.qty_actual
            
            
            
            item = {}
            item['VBELN'] = self.entrega
            item['POSNR'] = self.data.getPos(material.matnr)
            item['MATNR'] = material.matnr
            item['PIKMG'] = material.qty_actual
                
            items.append(item)
            
            sorted(items, key=lambda student: student["POSNR"])
            
            print type(float(material.qty))
            print type(float(material.qty_actual))
            
            if float(material.qty) == float(material.qty_actual):
                print "Por fin!"
            else:
                items = []
                break
            
            #linea de test
        
            
        print items
        
        
            
        
        
            
        return self.entrega, items
        
    def getMateriales(self):
        return self.materiales
        