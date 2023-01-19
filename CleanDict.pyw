#!/usr/bin/env python
# coding:utf-8
"""
  Author:  G.K.
  Purpose: 
  Created: 2016/3/3
"""

import sys
from PyQt5 import QtGui, QtWidgets
from PyQt5 import QtCore, QtWidgets
from dictionary import translate
import platform
if platform.system() == "Windows":
    # compiler
    import FixTk

icon = "dict.ico"


def center(w):
    qr = w.frameGeometry()
    cp = QtWidgets.QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    w.move(qr.topLeft())


def main():
    app = QtWidgets.QApplication(sys.argv)

    screen = app.primaryScreen()
    size = screen.size()
    w = QtWidgets.QWidget()
    w.resize(size.width()//4, size.height()//4)  # 0.618
    # w.move(300, 300)
    center(w)
    w.setWindowTitle('Clean Dictionary')

    textbox = QtWidgets.QLineEdit(w)
    btn = QtWidgets.QPushButton("Query")

    hbox = QtWidgets.QHBoxLayout()
    hbox.addWidget(textbox)
    hbox.addWidget(btn)

    logOutput = QtWidgets.QTextEdit(w)
    logOutput.setReadOnly(True)
    logOutput.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)

    font = logOutput.font()
    if platform.system() == "Darwin":
        font.setFamily("Menlo")
        font.setPointSize(13)
    else:
        # Courier Consolas
        font.setFamily("Consolas")
        font.setPointSize(12)

    logOutput.setCurrentFont(font)
    textbox.setFont(font)
    p = logOutput.palette()
    p.setColor(QtGui.QPalette.Base, QtGui.QColor(255, 255, 255))
    logOutput.setPalette(p)

    vbox = QtWidgets.QVBoxLayout()
    vbox.addLayout(hbox)
    vbox.addWidget(logOutput)

    w.setLayout(vbox)

    def on_clicked():
        query = textbox.text()
        if not query:
            return
        query = query.encode('utf8')
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
    if platform.system() == "Windows":
        import ctypes
        myappid = u'mycompany.myproduct.subproduct.version'  # arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    main()
