# -*- coding: utf-8 -*-

"""
Administrator interface for RFID system 

Allows monitoring and controlling the access servers on LAN.

author: David Beaudette 
last edited: April 2015
"""

import sys
from PyQt4 import QtGui


def main():
    
    app = QtGui.QApplication(sys.argv)
    btn = QtGui.QPushButton('Find Servers')
    w = QtGui.QWidget()
    #w.resize(250, 150)
    #w.move(300, 300)
    w.setWindowTitle('RFID Admin')
    w.show()
    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
