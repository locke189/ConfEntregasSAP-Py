'''
Created on 23/12/2014

@author: Juan.Insuasti
'''

from controller.maincontroller import Control
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    control = Control()
    control.view.show()
    app.exec_()
