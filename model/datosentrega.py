'''
Created on 29/12/2014

@author: Juan.Insuasti
'''

class DatosDeEntrega(object):
    '''
    Clase que administra la informacion proveniente del sistema fuente
    referente a la entrega solicitada.
    '''


    def __init__(self, raw_data):
        '''
        Constructor
        '''
        self.picking  = raw_data.Kostk
        self.mat_pos = {}
        self.mat_qnt = {}
        self.cod_mat = {}
        self.cod_matqnt = {}
        self.mat_txt = {}
        
        if self.picking == 'X':
            self.message = 'Picking Confirmado'
        
        else:
            for item in raw_data.Itemtab.item:
                self.mat_pos[item.Matnr] = item.Posnr
                self.mat_qnt[item.Matnr] = item.Lfimg
                self.cod_matqnt[item.EanUn] = item.ContUn
                self.cod_matqnt[item.EanCaja] = item.ContCaja 
                self.cod_mat[item.EanUn] = item.Matnr
                self.cod_mat[item.EanCaja] = item.Matnr
                self.mat_txt[item.Matnr] = item.Arktx
                
    def pickingCheck(self):
        '''
        
        '''
        return self.picking
    
    def getRequiredMat(self,matnr):
        return self.mat_qnt[matnr]
    
    def checkCodeMat(self,code):
        return self.cod_mat[code] 

    def checkCodeQty(self,code):
        return self.cod_matqnt[code]        
    
    def getMaterials(self):
        return self.mat_qnt.keys()   
    
    def getPos(self,matnr):
        return self.mat_pos[matnr]
    
    def getTxt(self,matnr):
        return self.mat_txt[matnr]
    