# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'final.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_XY(object):
    def setupUi(self, XY):
        XY.setObjectName(_fromUtf8("XY"))
        XY.resize(800, 600)
        self.centralwidget = QtGui.QWidget(XY)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.RectGate = QtGui.QCheckBox(self.centralwidget)
        self.RectGate.setObjectName(_fromUtf8("RectGate"))
        self.horizontalLayout.addWidget(self.RectGate)
        self.CircleGate1 = QtGui.QCheckBox(self.centralwidget)
        self.CircleGate1.setObjectName(_fromUtf8("CircleGate1"))
        self.horizontalLayout.addWidget(self.CircleGate1)
        self.CircleGate2 = QtGui.QCheckBox(self.centralwidget)
        self.CircleGate2.setObjectName(_fromUtf8("CircleGate2"))
        self.horizontalLayout.addWidget(self.CircleGate2)
        self.MousePosition = QtGui.QLabel(self.centralwidget)
        self.MousePosition.setObjectName(_fromUtf8("MousePosition"))
        self.horizontalLayout.addWidget(self.MousePosition)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.RectYield = QtGui.QLabel(self.centralwidget)
        self.RectYield.setObjectName(_fromUtf8("RectYield"))
        self.horizontalLayout_2.addWidget(self.RectYield)
        self.Circle1Yield = QtGui.QLabel(self.centralwidget)
        self.Circle1Yield.setObjectName(_fromUtf8("Circle1Yield"))
        self.horizontalLayout_2.addWidget(self.Circle1Yield)
        self.Circle2Yield = QtGui.QLabel(self.centralwidget)
        self.Circle2Yield.setObjectName(_fromUtf8("Circle2Yield"))
        self.horizontalLayout_2.addWidget(self.Circle2Yield)
        self.TotalIYield = QtGui.QLabel(self.centralwidget)
        self.TotalIYield.setObjectName(_fromUtf8("TotalIYield"))
        self.horizontalLayout_2.addWidget(self.TotalIYield)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.RectRate = QtGui.QLabel(self.centralwidget)
        self.RectRate.setObjectName(_fromUtf8("RectRate"))
        self.horizontalLayout_3.addWidget(self.RectRate)
        self.Circle1Rate = QtGui.QLabel(self.centralwidget)
        self.Circle1Rate.setObjectName(_fromUtf8("Circle1Rate"))
        self.horizontalLayout_3.addWidget(self.Circle1Rate)
        self.Circle2Rate = QtGui.QLabel(self.centralwidget)
        self.Circle2Rate.setObjectName(_fromUtf8("Circle2Rate"))
        self.horizontalLayout_3.addWidget(self.Circle2Rate)
        self.TotalRate = QtGui.QLabel(self.centralwidget)
        self.TotalRate.setObjectName(_fromUtf8("TotalRate"))
        self.horizontalLayout_3.addWidget(self.TotalRate)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        XY.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(XY)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 19))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        XY.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(XY)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        XY.setStatusBar(self.statusbar)

        self.retranslateUi(XY)
        QtCore.QMetaObject.connectSlotsByName(XY)

    def retranslateUi(self, XY):
        XY.setWindowTitle(_translate("XY", "MainWindow", None))
        self.RectGate.setText(_translate("XY", "RectGate", None))
        self.CircleGate1.setText(_translate("XY", "CircleGate1", None))
        self.CircleGate2.setText(_translate("XY", "CircleGate2", None))
        self.MousePosition.setText(_translate("XY", "MousePosition", None))
        self.RectYield.setText(_translate("XY", "RectYield", None))
        self.Circle1Yield.setText(_translate("XY", "Circle1Yield", None))
        self.Circle2Yield.setText(_translate("XY", "Circle2Yield", None))
        self.TotalIYield.setText(_translate("XY", "TotalYield", None))
        self.RectRate.setText(_translate("XY", "RectRate", None))
        self.Circle1Rate.setText(_translate("XY", "Circle1Rate", None))
        self.Circle2Rate.setText(_translate("XY", "Circle2Rate", None))
        self.TotalRate.setText(_translate("XY", "TotalRate", None))

