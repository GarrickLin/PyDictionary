#!/usr/bin/env python
#coding:utf-8
"""
  Author:  G.K.
  Purpose: 
  Created: 2016/3/3
"""

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from dictionary import translate
import urllib2
import ctypes
# compiler
import FixTk

icon = "dict.ico"
def center(w):
    qr = w.frameGeometry()
    cp = QtGui.QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    w.move(qr.topLeft())
    
def main():
    app = QtGui.QApplication(sys.argv)
    
    w = QtGui.QWidget()
    w.resize(500, 309) # 0.618
    #w.move(300, 300)
    center(w)
    w.setWindowTitle('Clean Dictionary')
    
    textbox = QtGui.QLineEdit(w)
    btn = QtGui.QPushButton("Query")
    
    hbox = QtGui.QHBoxLayout()
    hbox.addWidget(textbox)
    hbox.addWidget(btn)
    
    logOutput = QtGui.QTextEdit(w)
    logOutput.setReadOnly(True)
    logOutput.setLineWrapMode(QtGui.QTextEdit.NoWrap)
    
    font = logOutput.font()
    font.setFamily("Consolas") # Courier Consolas
    font.setPointSize(12)    
    
    logOutput.setCurrentFont(font)   
    textbox.setFont(font)
    p = logOutput.palette()
    p.setColor(QtGui.QPalette.Base, QtGui.QColor(255,255,255))
    logOutput.setPalette(p)
    

    vbox = QtGui.QVBoxLayout()
    vbox.addLayout(hbox)
    vbox.addWidget(logOutput)
    
    w.setLayout(vbox)
    
    def on_clicked():
        query = textbox.text()
        if query.isEmpty():
            return
        query = unicode(query).encode('utf8')
        out = translate(query)
        logOutput.setPlainText(out)
        
    btn.clicked.connect(on_clicked)
    textbox.returnPressed.connect(on_clicked)
    w.show()
    try:
        app.setWindowIcon(QtGui.QIcon(icon))
        w.setWindowIcon(QtGui.QIcon(icon))
    except:
        pass
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    myappid = u'mycompany.myproduct.subproduct.version' # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)    
    main()
