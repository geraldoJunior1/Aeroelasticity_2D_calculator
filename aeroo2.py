# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu_aeroelast.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

import numpy as np
import copy
import os
import sys
import t2Dsol
import matplotlib.pyplot as plt
from numpy.linalg import inv
from numpy import linalg as LA
import matplotlib.pyplot as plt
from matplotlib.backends.qt_compat import QtCore, QtWidgets, is_pyqt5

if is_pyqt5():
    from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
else:
    from matplotlib.backends.backend_qt4agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1160, 699)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(840, 550, 301, 101))
        self.textBrowser.setObjectName("textBrowser")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(430, 550, 61, 16))
        self.label_19.setObjectName("label_19")
        self.textEdit_axismax = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax.setGeometry(QtCore.QRect(480, 570, 61, 25))
        self.textEdit_axismax.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax.setObjectName("textEdit_axismax")
        self.textEdit_axismin = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismin.setGeometry(QtCore.QRect(410, 570, 61, 25))
        self.textEdit_axismin.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismin.setObjectName("textEdit_axismin")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(500, 550, 61, 16))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(320, 570, 71, 20))
        self.label_21.setObjectName("label_21")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(10, 580, 201, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(10, 550, 271, 41))
        self.label_13.setObjectName("label_13")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 220, 281, 81))
        self.groupBox_3.setObjectName("groupBox_3")
        self.textEdit_8 = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit_8.setGeometry(QtCore.QRect(138, 50, 131, 25))
        self.textEdit_8.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_8.setObjectName("textEdit_8")
        self.textEdit_7 = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit_7.setGeometry(QtCore.QRect(138, 20, 131, 25))
        self.textEdit_7.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_7.setObjectName("textEdit_7")
        self.label_23 = QtWidgets.QLabel(self.groupBox_3)
        self.label_23.setGeometry(QtCore.QRect(10, 50, 111, 16))
        self.label_23.setObjectName("label_23")
        self.label_22 = QtWidgets.QLabel(self.groupBox_3)
        self.label_22.setGeometry(QtCore.QRect(10, 20, 111, 16))
        self.label_22.setObjectName("label_22")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 310, 281, 231))
        self.groupBox_2.setObjectName("groupBox_2")
        self.textEdit_14 = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit_14.setGeometry(QtCore.QRect(140, 110, 131, 25))
        self.textEdit_14.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_14.setObjectName("textEdit_14")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(10, 50, 111, 16))
        self.label_11.setObjectName("label_11")
        self.textEdit_13 = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit_13.setGeometry(QtCore.QRect(140, 80, 131, 25))
        self.textEdit_13.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_13.setObjectName("textEdit_13")
        self.textEdit_31 = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit_31.setGeometry(QtCore.QRect(140, 170, 131, 25))
        self.textEdit_31.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_31.setObjectName("textEdit_31")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(10, 20, 111, 16))
        self.label_9.setObjectName("label_9")
        self.label_14 = QtWidgets.QLabel(self.groupBox_2)
        self.label_14.setGeometry(QtCore.QRect(10, 170, 81, 16))
        self.label_14.setObjectName("label_14")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(10, 110, 111, 16))
        self.label_8.setObjectName("label_8")
        self.textEdit_11 = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit_11.setGeometry(QtCore.QRect(140, 20, 131, 25))
        self.textEdit_11.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_11.setObjectName("textEdit_11")
        self.label_18 = QtWidgets.QLabel(self.groupBox_2)
        self.label_18.setGeometry(QtCore.QRect(10, 140, 61, 16))
        self.label_18.setObjectName("label_18")
        self.textEdit_12 = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit_12.setGeometry(QtCore.QRect(140, 50, 131, 25))
        self.textEdit_12.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_12.setObjectName("textEdit_12")
        self.textEdit_32 = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit_32.setGeometry(QtCore.QRect(140, 200, 131, 25))
        self.textEdit_32.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_32.setObjectName("textEdit_32")
        self.label_15 = QtWidgets.QLabel(self.groupBox_2)
        self.label_15.setGeometry(QtCore.QRect(10, 200, 81, 16))
        self.label_15.setObjectName("label_15")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(10, 80, 111, 16))
        self.label_10.setObjectName("label_10")
        self.textEdit_24 = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit_24.setGeometry(QtCore.QRect(140, 140, 131, 25))
        self.textEdit_24.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_24.setObjectName("textEdit_24")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 10, 281, 201))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label_7.setGeometry(QtCore.QRect(10, 170, 111, 16))
        self.label_7.setObjectName("label_7")
        self.textEdit_1 = QtWidgets.QTextEdit(self.groupBox_4)
        self.textEdit_1.setGeometry(QtCore.QRect(140, 20, 131, 25))
        self.textEdit_1.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_1.setObjectName("textEdit_1")
        self.textEdit_6 = QtWidgets.QTextEdit(self.groupBox_4)
        self.textEdit_6.setGeometry(QtCore.QRect(138, 170, 131, 25))
        self.textEdit_6.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_6.setObjectName("textEdit_6")
        self.textEdit_5 = QtWidgets.QTextEdit(self.groupBox_4)
        self.textEdit_5.setGeometry(QtCore.QRect(138, 140, 131, 25))
        self.textEdit_5.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_5.setObjectName("textEdit_5")
        self.textEdit_4 = QtWidgets.QTextEdit(self.groupBox_4)
        self.textEdit_4.setGeometry(QtCore.QRect(138, 110, 131, 25))
        self.textEdit_4.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_4.setObjectName("textEdit_4")
        self.label_2 = QtWidgets.QLabel(self.groupBox_4)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 111, 16))
        self.label_2.setObjectName("label_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.groupBox_4)
        self.textEdit_3.setGeometry(QtCore.QRect(138, 80, 131, 25))
        self.textEdit_3.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 111, 16))
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label_6.setGeometry(QtCore.QRect(10, 140, 111, 16))
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setGeometry(QtCore.QRect(10, 110, 111, 16))
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(10, 80, 111, 16))
        self.label_4.setObjectName("label_4")
        self.textEdit_2 = QtWidgets.QTextEdit(self.groupBox_4)
        self.textEdit_2.setGeometry(QtCore.QRect(138, 50, 131, 25))
        self.textEdit_2.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(670, 550, 161, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(670, 620, 161, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QtCore.QRect(310, 20, 831, 521))
        self.groupBox.setObjectName("groupBox")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(680, 590, 151, 20))
        self.checkBox.setObjectName("checkBox")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(320, 600, 81, 20))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(320, 630, 81, 20))
        self.label_25.setObjectName("label_25")
        self.textEdit_axismin_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismin_2.setGeometry(QtCore.QRect(410, 600, 61, 25))
        self.textEdit_axismin_2.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismin_2.setObjectName("textEdit_axismin_2")
        self.textEdit_axismax_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_2.setGeometry(QtCore.QRect(480, 600, 61, 25))
        self.textEdit_axismax_2.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_2.setObjectName("textEdit_axismax_2")
        self.textEdit_axismin_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismin_3.setGeometry(QtCore.QRect(410, 630, 61, 25))
        self.textEdit_axismin_3.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismin_3.setObjectName("textEdit_axismin_3")
        self.textEdit_axismax_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_axismax_3.setGeometry(QtCore.QRect(480, 630, 61, 25))
        self.textEdit_axismax_3.setMaximumSize(QtCore.QSize(16777215, 35))
        self.textEdit_axismax_3.setObjectName("textEdit_axismax_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1160, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.plotFigLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.plot_static_canvas = FigureCanvas(Figure(figsize=(2, 2)))
        self.plotFigLayout.addWidget(self.plot_static_canvas)
        self.A =[]
        self.outro = 0
        try:
            fileID = open('./inputs.txt','r')
            self.A= fileID.read().splitlines()
            print(self.A)
            fileID.close()
            self.textEdit_1.insertPlainText(self.A[0])
            self.textEdit_2.insertPlainText(self.A[1])
            self.textEdit_3.insertPlainText(self.A[2])
            self.textEdit_4.insertPlainText(self.A[3])
            self.textEdit_5.insertPlainText(self.A[4])
            self.textEdit_6.insertPlainText(self.A[5])
            self.textEdit_7.insertPlainText(self.A[6])
            self.textEdit_8.insertPlainText(self.A[7])
            self.textEdit_11.insertPlainText(self.A[8])
            self.textEdit_12.insertPlainText(self.A[9])
            self.textEdit_13.insertPlainText(self.A[10])
            self.textEdit_14.insertPlainText(self.A[11])
            self.textEdit_24.insertPlainText(self.A[12])
            self.textEdit_31.insertPlainText(self.A[13])
            self.textEdit_32.insertPlainText(self.A[14])
            self.textEdit_axismin.insertPlainText(self.A[15])
            self.textEdit_axismax.insertPlainText(self.A[16])
        except:
            pass


        self.fig_canvas = self.plot_static_canvas
        self.fig = self.fig_canvas.figure
        self.pushButton.clicked.connect(lambda:self.creat('flutter'))
        self.pushButton_2.clicked.connect(lambda:self.creat('rev'))
        self.checkBox.stateChanged.connect(lambda x:self.lig('outro',x))

        '''
        self.pushButton_ana.clicked.connect(lambda:self.flutter())
        self.pushButton.clicked.connect(lambda:self.plot())
        #self.textEdit_axismin.textChanged.connect(lambda:self.plot())
        #self.textEdit_axismax.textChanged.connect(lambda:self.plot())
        self.legonoff = True
        '''
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_19.setText(_translate("MainWindow", "Min"))
        self.label_20.setText(_translate("MainWindow", "Max"))
        self.label_21.setText(_translate("MainWindow", "Velocity (m/s)"))
        self.label_12.setText(_translate("MainWindow", "Contact: thiacene@gmail.com"))
        self.label_13.setText(_translate("MainWindow", "Developed by: Geraldo Majella Nunes Junior"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Control sup."))
        self.label_23.setText(_translate("MainWindow", "Control sup. beta (ยบ)"))
        self.label_22.setText(_translate("MainWindow", "Control sup. chord  (m)"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Structure data"))
        self.label_11.setText(_translate("MainWindow", "Freq. 2 (Hz)"))
        self.label_9.setText(_translate("MainWindow", "Freq. 1 (Hz)"))
        self.label_14.setText(_translate("MainWindow", "CG position (m)"))
        self.label_8.setText(_translate("MainWindow", "Ka"))
        self.label_18.setText(_translate("MainWindow", "Mass unity"))
        self.label_15.setText(_translate("MainWindow", "EC position (m)"))
        self.label_10.setText(_translate("MainWindow", "Kh"))
        self.groupBox_4.setTitle(_translate("MainWindow", "General data"))
        self.label_7.setText(_translate("MainWindow", "RHO (kg/m^2)"))
        self.label_2.setText(_translate("MainWindow", "CA position (m)"))
        self.label_3.setText(_translate("MainWindow", "Chord (m)"))
        self.label_6.setText(_translate("MainWindow", "a1 coeff."))
        self.label_5.setText(_translate("MainWindow", "aw coeff."))
        self.label_4.setText(_translate("MainWindow", "Wingspan (m)"))
        self.pushButton.setText(_translate("MainWindow", "Plot: v-g-f diagram"))
        self.pushButton_2.setText(_translate("MainWindow", "Plot: Control eff."))
        self.groupBox.setTitle(_translate("MainWindow", "Plot"))
        self.checkBox.setText(_translate("MainWindow", "Alternative flutter method"))
        self.label_24.setText(_translate("MainWindow", "Frequency (Hz)"))
        self.label_25.setText(_translate("MainWindow", "Damping"))


    def creat(self,aaa):
        if True:
            if True:
                try: 
                    self.amortminX = float(self.textEdit_axismin_3.toPlainText())
                except : 
                    self.amortminX =-0.1
                    self.textEdit_axismin_3.insertPlainText(str(self.amortminX))
                try: 
                    self.amortmaxX = float(self.textEdit_axismax_3.toPlainText())
                except : 
                    self.amortmaxX = 0.1
                    self.textEdit_axismax_3.insertPlainText(str(self.amortmaxX))
                try: 
                    self.freqmaxX = float(self.textEdit_axismax_2.toPlainText())
                except : 
                    self.freqmaxX = 50
                    self.textEdit_axismax_2.insertPlainText(str(self.freqmaxX))
                try: 
                    self.freqminN = float(self.textEdit_axismin_2.toPlainText())
                except : 
                    self.freqminN = 0
                    self.textEdit_axismin_2.insertPlainText(str(self.freqminN))
                try: 
                    self.velmaxX = float(self.textEdit_axismax.toPlainText())
                except : 
                    self.velmaxX = 40
                    self.textEdit_axismax.insertPlainText(str(self.velmaxX))

                try: 
                    self.velminN = float(self.textEdit_axismin.toPlainText())
                except : 
                    self.velminN = 0
                    self.textEdit_axismin.insertPlainText(str(self.velminN))

        try:

            self.A= [None] * 17
            self.A[0] = self.textEdit_1.toPlainText()
            self.A[1] = self.textEdit_2.toPlainText()
            self.A[2] = self.textEdit_3.toPlainText()
            self.A[3] = self.textEdit_4.toPlainText()
            self.A[4] = self.textEdit_5.toPlainText()
            self.A[5] = self.textEdit_6.toPlainText()
            self.A[6] = self.textEdit_7.toPlainText()
            self.A[7] = self.textEdit_8.toPlainText()
            self.A[8] = self.textEdit_11.toPlainText()
            self.A[9] = self.textEdit_12.toPlainText()
            self.A[10] = self.textEdit_13.toPlainText()
            self.A[11] = self.textEdit_14.toPlainText()
            self.A[12] = self.textEdit_24.toPlainText()
            self.A[13] = self.textEdit_31.toPlainText()
            self.A[14] = self.textEdit_32.toPlainText()
            self.A[15] = self.textEdit_axismin.toPlainText()
            self.A[16] = self.textEdit_axismax.toPlainText()


            self.B=[]
            for i in range(len(self.A)):
                self.B.append(float(self.A[i]))

            fileID=open('./inputs.txt','w')
            for i in range (len(self.A)):
                e = float(self.A[i])
                fileID.write("%s \n" % str(e))
            self.plot(aaa)
        except: 
            pass


    def lig(self,a,x):
        try:
            if a == 'outro':
                self.outro = x
        except:
            pass

    def plot(self, aaa):
        #self.legonoff = self.checkBox.isChecked()
        try: self.fig.clf()
        except: pass

        self.fig_canvas = self.plot_static_canvas
        self.fig = self.fig_canvas.figure

        if aaa == 'flutter':
            self.ax = self.fig.add_subplot(211)
            self.ax2 = self.fig.add_subplot(212)
            box1 = self.ax.get_position()
            box2 = self.ax2.get_position()
            if self.outro != 0:
                self.vel, self.amort1, self.vel2, self.amort2,self.vel1, self.freq1, self.vel12, self.freq2 = t2Dsol.autovalorcomplex(self.B[13], self.B[14], self.B[2], self.B[5], self.B[0], self.B[12],self.B[8], self.B[9], self.B[16])
            else:
                self.vel, self.amort1, self.vel2, self.amort2,self.vel1, self.freq1, self.vel12, self.freq2 = t2Dsol.nestacionario(self.B[13], self.B[14], self.B[2], self.B[5], self.B[0], self.B[12],self.B[8], self.B[9])

        
            self.vel11=copy.deepcopy(self.vel)
            #self.vel11.append(0)
            self.vel22=copy.deepcopy(self.vel2)
            #self.vel22.append(0)
            self.ax.plot(self.vel,self.freq1, color='red')
            self.ax.plot(self.vel2,self.freq2, color='blue')
            self.ax.set_xlim(self.velminN,self.velmaxX)
            self.ax.set_ylim(self.freqminN,self.freqmaxX)
            self.ax.set_ylabel('Frequência (Hz)')
            self.ax.set_title('Diagrama vgf')
            self.ax.grid()
            self.ax2.plot(self.vel11[2:],self.amort1[2:],color='red')
            self.ax2.plot(self.vel22[2:],self.amort2[2:],color='blue')
            self.ax2.set_xlabel('Velocidade (m/s)')
            self.ax2.set_ylabel('Amortecimento')
            self.ax2.grid()
            self.ax2.set_xlim(self.velminN,self.velmaxX)
            self.ax2.set_ylim(self.amortminX,self.amortmaxX)
            '''
            try: self.textBrowser.clear()
            except: pass
            a=str("{:.2f}".format(self.U_flutter))
            b = 'Velocidade de flutter:'+' '+a+' '+'m/s'
            self.textBrowser.append(b)
            '''
        else:
            vel, eff, U_rev, U_div = t2Dsol.effcontrol(self.B[5], self.B[3], self.B[7],self.B[0],self.B[14],self.B[10],self.B[6])
            self.ax = self.fig.add_subplot(111)
            for i in range(len(eff)):
                eff[i]=eff[i]*100
            self.ax.plot(vel, eff, color ='black')
            self.ax.set_title('Eficiência de comandos')
            self.ax.set_xlim(left=0,right=None)
            self.ax.set_ylim(0,100)
            self.ax.set_xlabel('Velocidade (m/s)')
            self.ax.set_ylabel('Eficiência (%)')
            self.ax.set_xlim(self.velminN,self.velmaxX)
            self.ax.set_ylim(0,100)
            
            try: self.textBrowser.clear()
            except: pass
            a=str("{:.2f}".format(U_rev))
            c=str("{:.2f}".format(U_div))
            b = 'Velocidade de reversão de controle:'+' '+a+' '+'m/s'
            d = 'Velocidade de divergência:'+' '+c+' '+'m/s'
            self.textBrowser.append(b)
            self.textBrowser.append(d)
            self.ax.grid()
        #self.ax2.set_xlim(self.amortminX,self.amortmaxX)
        #self.ax2.set_ylim(self.amortminY,self.amortmaxY)
        self.fig_canvas.draw()

        
#if __name__ == "__main__":
def RODCANENGAST():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
