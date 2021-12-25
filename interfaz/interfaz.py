# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
import random


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1055, 774)
        

        # --- Groupbox ploteo en matplotlib ---
        self.GB_PlotMat = QtWidgets.QGroupBox(Dialog)
        self.GB_PlotMat.setGeometry(QtCore.QRect(5, 20, 700, 750))
        ##self.figure = MyFigure()
        # a figure instance to plot on
        self.figure = plt.figure()
   
        # this is the Canvas Widget that 
        # displays the 'figure'it takes the
        # 'figure' instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)
        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas,Dialog)

        self.gridlayout = QtWidgets.QGridLayout(self.GB_PlotMat)
        self.gridlayout.addWidget(self.toolbar, 0, 1)
        self.gridlayout.addWidget(self.canvas, 1, 1)
        

        # --- GroupBox datos entrada ---
        self.GB_input = QtWidgets.QGroupBox(Dialog)
        self.GB_input.setGeometry(QtCore.QRect(730, 20, 301, 311))
        self.GB_input.setObjectName("GB_input")
        self.LE_ingresoBD = QtWidgets.QLineEdit(self.GB_input)
        self.LE_ingresoBD.setGeometry(QtCore.QRect(10, 50, 161, 31))
        self.LE_ingresoBD.setObjectName("LE_ingresoBD")
        self.PB_DialogButton = QtWidgets.QPushButton(self.GB_input)
        self.PB_DialogButton.setGeometry(QtCore.QRect(180, 50, 71, 31))
        self.PB_DialogButton.setObjectName("PB_DialogButton")
        self.lbl_ingresodatos = QtWidgets.QLabel(self.GB_input)
        self.lbl_ingresodatos.setGeometry(QtCore.QRect(10, 20, 201, 21))
        self.lbl_ingresodatos.setObjectName("lbl_ingresodatos")
        self.PB_plot = QtWidgets.QPushButton(self.GB_input)
        self.PB_plot.setGeometry(QtCore.QRect(10, 260, 93, 28))
        self.PB_plot.setObjectName("PB_plot")
        self.PB_plot.clicked.connect(self.plot)
        self.lbl_MediaModelo = QtWidgets.QLabel(self.GB_input)
        self.lbl_MediaModelo.setGeometry(QtCore.QRect(80, 190, 41, 21))
        self.lbl_MediaModelo.setObjectName("lbl_MediaModelo")
        self.lbl_StandarDeviationModelo = QtWidgets.QLabel(self.GB_input)
        self.lbl_StandarDeviationModelo.setGeometry(QtCore.QRect(80, 220, 121, 31))
        self.lbl_StandarDeviationModelo.setObjectName("lbl_StandarDeviationModelo")
        self.lbl_ajustemodelo = QtWidgets.QLabel(self.GB_input)
        self.lbl_ajustemodelo.setGeometry(QtCore.QRect(10, 150, 111, 21))
        self.lbl_ajustemodelo.setObjectName("lbl_ajustemodelo")
        self.CB_Scatter = QtWidgets.QCheckBox(self.GB_input)
        self.CB_Scatter.setGeometry(QtCore.QRect(10, 90, 81, 20))
        self.CB_Scatter.setObjectName("CB_Scatter")
        self.CB_Modelo = QtWidgets.QCheckBox(self.GB_input)
        self.CB_Modelo.setGeometry(QtCore.QRect(10, 120, 81, 20))
        self.CB_Modelo.setObjectName("CB_Modelo")
        self.DSB_media = QtWidgets.QDoubleSpinBox(self.GB_input)
        self.DSB_media.setGeometry(QtCore.QRect(10, 190, 62, 22))
        self.DSB_media.setObjectName("DSB_media")
        self.DSB_StandardDeviation = QtWidgets.QDoubleSpinBox(self.GB_input)
        self.DSB_StandardDeviation.setGeometry(QtCore.QRect(10, 220, 62, 22))
        self.DSB_StandardDeviation.setObjectName("DSB_StandardDeviation")

        # --- GroupBox EstadisticaActual---
        self.GB_EstadisticaActual = QtWidgets.QGroupBox(Dialog)
        self.GB_EstadisticaActual.setGeometry(QtCore.QRect(730, 340, 301, 251))
        self.GB_EstadisticaActual.setObjectName("GB_EstadisticaActual")
        self.LE_ActualMean = QtWidgets.QLineEdit(self.GB_EstadisticaActual)
        self.LE_ActualMean.setGeometry(QtCore.QRect(20, 20, 31, 21))
        self.LE_ActualMean.setObjectName("LE_ActualMean")
        self.LE_ActualStandardDeviation = QtWidgets.QLineEdit(self.GB_EstadisticaActual)
        self.LE_ActualStandardDeviation.setGeometry(QtCore.QRect(20, 50, 31, 21))
        self.LE_ActualStandardDeviation.setObjectName("LE_ActualStandardDeviation")
        self.LE_SizeData = QtWidgets.QLineEdit(self.GB_EstadisticaActual)
        self.LE_SizeData.setGeometry(QtCore.QRect(20, 80, 31, 21))
        self.LE_SizeData.setObjectName("LE_SizeData")
        self.lbl_mediaBase = QtWidgets.QLabel(self.GB_EstadisticaActual)
        self.lbl_mediaBase.setGeometry(QtCore.QRect(60, 20, 81, 16))
        self.lbl_mediaBase.setObjectName("lbl_mediaBase")
        self.lbl_StandardDeviationBase = QtWidgets.QLabel(self.GB_EstadisticaActual)
        self.lbl_StandardDeviationBase.setGeometry(QtCore.QRect(60, 50, 161, 16))
        self.lbl_StandardDeviationBase.setObjectName("lbl_StandardDeviationBase")
        self.lbl_SizeDataBase = QtWidgets.QLabel(self.GB_EstadisticaActual)
        self.lbl_SizeDataBase.setGeometry(QtCore.QRect(60, 80, 161, 16))
        self.lbl_SizeDataBase.setObjectName("lbl_SizeDataBase")
        self.LE_ActualMax = QtWidgets.QLineEdit(self.GB_EstadisticaActual)
        self.LE_ActualMax.setGeometry(QtCore.QRect(20, 110, 31, 21))
        self.LE_ActualMax.setObjectName("LE_ActualMax")
        self.LE_ActualMin = QtWidgets.QLineEdit(self.GB_EstadisticaActual)
        self.LE_ActualMin.setGeometry(QtCore.QRect(20, 140, 31, 21))
        self.LE_ActualMin.setObjectName("LE_ActualMin")
        self.lbl_ActualMaxBase = QtWidgets.QLabel(self.GB_EstadisticaActual)
        self.lbl_ActualMaxBase.setGeometry(QtCore.QRect(60, 110, 161, 16))
        self.lbl_ActualMaxBase.setObjectName("lbl_ActualMaxBase")
        self.lbl_ActualMinaBase = QtWidgets.QLabel(self.GB_EstadisticaActual)
        self.lbl_ActualMinaBase.setGeometry(QtCore.QRect(60, 140, 71, 16))
        self.lbl_ActualMinaBase.setObjectName("lbl_ActualMinaBase")
        self.PB_BaseActual = QtWidgets.QPushButton(self.GB_EstadisticaActual)
        self.PB_BaseActual.setGeometry(QtCore.QRect(170, 210, 111, 31))
        self.PB_BaseActual.setObjectName("PB_BaseActual")
        self.SB_Spacingset = QtWidgets.QSpinBox(self.GB_EstadisticaActual)
        self.SB_Spacingset.setGeometry(QtCore.QRect(150, 160, 51, 31))
        self.SB_Spacingset.setObjectName("SB_Spacingset")
        self.LE_ActualMin_2 = QtWidgets.QLineEdit(self.GB_EstadisticaActual)
        self.LE_ActualMin_2.setGeometry(QtCore.QRect(20, 170, 31, 21))
        self.LE_ActualMin_2.setObjectName("LE_ActualMin_2")
        self.lbl_percentilBase = QtWidgets.QLabel(self.GB_EstadisticaActual)
        self.lbl_percentilBase.setGeometry(QtCore.QRect(60, 170, 71, 16))
        self.lbl_percentilBase.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbl_percentilBase.setObjectName("lbl_percentilBase")
        self.lbl_SpacingSetMuestra = QtWidgets.QLabel(self.GB_EstadisticaActual)
        self.lbl_SpacingSetMuestra.setGeometry(QtCore.QRect(210, 170, 71, 16))
        self.lbl_SpacingSetMuestra.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbl_SpacingSetMuestra.setObjectName("lbl_SpacingSetMuestra")

        # -- Groupbox Modelo-- 
        self.GB_modelo = QtWidgets.QGroupBox(Dialog)
        self.GB_modelo.setGeometry(QtCore.QRect(730, 600, 301, 171))
        self.GB_modelo.setObjectName("GB_modelo")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def plot(self):
        if self.CB_Scatter.isChecked() and not self.CB_Modelo.isChecked():
            print('solo scatter activado')
            # random data
            data = [random.random() for i in range(10)]
            # clearing old figure
            self.figure.clear()
            # create an axis
            ax = self.figure.add_subplot(111, xlabel = "Spacing Set [m]", ylabel = "acumulado")
            ##ax.set_title('seda')
            # plot data
            ax.scatter(data,data)
            # refresh canvas
            self.canvas.draw()
        elif self.CB_Modelo.isChecked() and not self.CB_Scatter.isChecked():
            print('solo scatter activado')
            # random data
            data = [random.random() for i in range(10)]
            # clearing old figure
            self.figure.clear()
            # create an axis
            ax = self.figure.add_subplot(111, xlabel = "Spacing Set [m]", ylabel = "acumulado")
            ##ax.set_title('seda')
            # plot data
            ax.plot(data,data, 'r-')
            # refresh canvas
            self.canvas.draw()

        elif self.CB_Scatter.isChecked() and self.CB_Modelo.isChecked():
            print('modelo y scatter activado')
            # random data
            data = [random.random() for i in range(10)]
            # clearing old figure
            self.figure.clear()
            # create an axis
            ax = self.figure.add_subplot(111, xlabel = "Spacing Set [m]", ylabel = "acumulado")
            ##ax.set_title('seda')
            # plot data
            ax.scatter(data,data)
            ax.plot(data,data, 'r-')
            # refresh canvas
            self.canvas.draw()
        else:
            print('seleccione un checkbox')


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Distribucion LogNormal"))
        self.GB_PlotMat.setTitle(_translate("Dialog","Plot"))
        self.GB_input.setTitle(_translate("Dialog", "Input"))
        self.PB_DialogButton.setText(_translate("Dialog", "..."))
        self.lbl_ingresodatos.setText(_translate("Dialog", "Ingreso de datos:"))
        self.PB_plot.setText(_translate("Dialog", "Plot"))
        self.lbl_MediaModelo.setText(_translate("Dialog", "Media"))
        self.lbl_StandarDeviationModelo.setText(_translate("Dialog", "Desviacion estandar"))
        self.lbl_ajustemodelo.setText(_translate("Dialog", "Ajuste modelo"))
        self.CB_Scatter.setText(_translate("Dialog", "Scatter"))
        self.CB_Modelo.setText(_translate("Dialog", "Modelo"))
        self.GB_EstadisticaActual.setTitle(_translate("Dialog", "Base datos actual Muestra"))
        self.lbl_mediaBase.setText(_translate("Dialog", "Media Actual"))
        self.lbl_StandardDeviationBase.setText(_translate("Dialog", "Desviacion Estandar Actual"))
        self.lbl_SizeDataBase.setText(_translate("Dialog", "Numero de datos"))
        self.lbl_ActualMaxBase.setText(_translate("Dialog", "Máximo"))
        self.lbl_ActualMinaBase.setText(_translate("Dialog", "Mínimo"))
        self.PB_BaseActual.setText(_translate("Dialog", "Ver Base Actual"))
        self.lbl_percentilBase.setText(_translate("Dialog", "Percentil"))
        self.lbl_SpacingSetMuestra.setText(_translate("Dialog", "SpacingSet"))
        self.GB_modelo.setTitle(_translate("Dialog", "Estadistica modelo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
