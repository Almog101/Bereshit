#from PySide2.QtCore import *
#from PySide2.QtGui import *
#from PySide2.QtWidgets import *

import sys

import PySide2.QtCore as QtCore
import PySide2.QtGui as QtGui
import PySide2.QtWidgets as QtWidgets

import xrandr


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setFixedSize(430, 300)

        self.is_on = True

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.allscreens_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.allscreens_checkBox.setObjectName(u"allscreens_checkBox")
        self.allscreens_checkBox.setGeometry(QtCore.QRect(250, 20, 100, 35))

        self.screens_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.screens_comboBox.setObjectName(u"screens_comboBox")
        self.screens_comboBox.setGeometry(QtCore.QRect(80, 20, 120, 35))
        # adds screens names to combo box
        self.screens_comboBox.addItems(xrandr.get_screens())

        self.BrightnessSlider = QtWidgets.QSlider(self.centralwidget)
        self.BrightnessSlider.setObjectName(u"BrightnessSlider")
        self.BrightnessSlider.setGeometry(QtCore.QRect(160, 90, 210, 20))
        self.BrightnessSlider.setOrientation(QtCore.Qt.Horizontal)
        self.BrightnessSlider.setMaximum(100)

        self.TemperatureSlider = QtWidgets.QSlider(self.centralwidget)
        self.TemperatureSlider.setObjectName(u"TemperatureSlider")
        self.TemperatureSlider.setGeometry(QtCore.QRect(160, 140, 210, 20))
        self.TemperatureSlider.setOrientation(QtCore.Qt.Horizontal)
        self.TemperatureSlider.setMinimum(1000)
        self.TemperatureSlider.setMaximum(10000)
        self.TemperatureSlider.setTickInterval(500)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QtCore.QRect(40, 90, 80, 20))

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QtCore.QRect(40, 140, 90, 20))

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QtCore.QRect(115, 190, 200, 36))

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QtCore.QRect(380, 80, 40, 34))

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QtCore.QRect(380, 130, 40, 34))

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QtCore.QRect(0, 0, 430, 32))

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")

        MainWindow.setStatusBar(self.statusbar)
        MainWindow.setMenuBar(self.menubar)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)

        #self.pushButton.clicked.connect(self.apply_changes)
        self.pushButton.clicked.connect(self.on_off_switch)

        self.connect_slider_to_textbox(self.BrightnessSlider, self.lineEdit)
        self.connect_slider_to_textbox(self.TemperatureSlider, self.lineEdit_2)

        self.connect_textbox_to_slider(self.BrightnessSlider, self.lineEdit)
        self.connect_textbox_to_slider(self.TemperatureSlider, self.lineEdit_2)

        self.BrightnessSlider.setValue(70)
        self.TemperatureSlider.setValue(3000)


        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def apply_changes(self):
        current_screen = self.screens_comboBox.currentText()
        brightness = int(self.BrightnessSlider.value())
        temperature = int(self.TemperatureSlider.value())
        
        gamma = xrandr.tuple_to_string(xrandr.temperature_to_rgb(temperature))
        #print(current_screen, a, b)
        xrandr.change_screen_details(current_screen, brightness/100, gamma)

    def connect_slider_to_textbox(self, slider, textbox):
        textbox.setText(str(slider.value()))
        slider.valueChanged.connect(lambda: textbox.setText(str(slider.value())))

    def connect_textbox_to_slider(self, slider, textbox):
        textbox.textChanged.connect(lambda: slider.setValue(int(textbox.text()) if textbox.text().isdigit() else 0))


    def on_off_switch(self):
        if self.is_on:
            self.is_on = False

            current_screen = self.screens_comboBox.currentText()
            gamma = xrandr.tuple_to_string((1,1,1))
            xrandr.change_screen_details(current_screen, 1, gamma)
        else:
            self.is_on = True
            self.apply_changes()


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtCore.QCoreApplication.translate("MainWindow", u"enter title here", None))
        self.allscreens_checkBox.setText(QtCore.QCoreApplication.translate("MainWindow", u"All Screens", None))
        self.label.setText(QtCore.QCoreApplication.translate("MainWindow", u"Brightness ", None))
        self.label_2.setText(QtCore.QCoreApplication.translate("MainWindow", u"Temperature", None))
        self.pushButton.setText(QtCore.QCoreApplication.translate("MainWindow", u"Turn ON/OFF", None))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()
