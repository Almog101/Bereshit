import PySide2.QtGui as QtGui
import PySide2.QtWidgets as QtWidgets 
import PySide2.QtCore as QtCore
import xrandr

ICON_PATH = "./src/icon.png"

WIDTH = 430
HEIGHT = 260

MIN_BRIGHTNESS = 30
MAX_BRIGHTNESS = 100

MIN_TEMPERATURE = 2000
MAX_TEMPERATURE = 5000

class SystemTryWidgit:
    def setupUi(self, MainWindow, app):
        self.tray = QtWidgets.QSystemTrayIcon()
        self.tray.setIcon(QtGui.QIcon(ICON_PATH))
        self.tray.setVisible(True)
        self.tray.activated.connect(lambda: MainWindow.show())

        # Creating the options
        self.menu = QtWidgets.QMenu()
        self.oepn = QtWidgets.QAction("Open")
        self.quit = QtWidgets.QAction("Quit")
        
        self.quit.triggered.connect(app.quit)
        self.oepn.triggered.connect(lambda: MainWindow.show())

        self.menu.addAction(self.oepn)
        self.menu.addAction(self.quit)

        self.tray.setContextMenu(self.menu)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setFixedSize(WIDTH, HEIGHT)
        self.is_on = False
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.allscreens_check_box = QtWidgets.QCheckBox(self.centralwidget)
        self.allscreens_check_box.setGeometry(QtCore.QRect(250, 20, 100, 35))

        self.screens_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.screens_comboBox.setGeometry(QtCore.QRect(80, 20, 120, 35))
        self.screens_comboBox.addItems(xrandr.get_screens())

        self.brightness_slider = QtWidgets.QSlider(self.centralwidget)
        self.brightness_slider.setGeometry(QtCore.QRect(160, 90, 210, 20))
        self.brightness_slider.setOrientation(QtCore.Qt.Horizontal)
        self.brightness_slider.setRange(MIN_BRIGHTNESS, MAX_BRIGHTNESS)
        
        self.temperature_slider = QtWidgets.QSlider(self.centralwidget)
        self.temperature_slider.setGeometry(QtCore.QRect(160, 140, 210, 20))
        self.temperature_slider.setOrientation(QtCore.Qt.Horizontal)
        self.temperature_slider.setRange(MIN_TEMPERATURE, MAX_TEMPERATURE)

        self.brightness_label = QtWidgets.QLabel(self.centralwidget)
        self.brightness_label.setGeometry(QtCore.QRect(40, 90, 80, 20))

        self.temperature_label = QtWidgets.QLabel(self.centralwidget)
        self.temperature_label.setGeometry(QtCore.QRect(40, 140, 90, 20))

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(115, 190, 200, 36))

        self.brightness_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.brightness_line_edit.setGeometry(QtCore.QRect(380, 80, 40, 34))

        self.temperature_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.temperature_line_edit.setGeometry(QtCore.QRect(380, 130, 40, 34))

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 430, 32))

        self.statusbar = QtWidgets.QStatusBar(MainWindow)

        MainWindow.setStatusBar(self.statusbar)
        MainWindow.setMenuBar(self.menubar)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)

        self.pushButton.clicked.connect(self.on_off_switch)

        self.connect_slider_and_textbox(self.brightness_slider, self.brightness_line_edit)
        self.connect_slider_and_textbox(self.temperature_slider, self.temperature_line_edit)

        self.brightness_slider.setValue(MAX_BRIGHTNESS)
        self.temperature_slider.setValue(MAX_TEMPERATURE)

        self.brightness_slider.valueChanged.connect(lambda: self.apply_changes())
        self.temperature_slider.valueChanged.connect(lambda: self.apply_changes())

        self.allscreens_check_box.stateChanged.connect(lambda: self.screens_comboBox.setEnabled(not self.allscreens_check_box.isChecked()))


        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def apply_changes(self):
        if not self.is_on:
            return

        if self.allscreens_check_box.isChecked():
            screens = [self.screens_comboBox.itemText(i) for i in range(self.screens_comboBox.count())]
        else:
            screens = [self.screens_comboBox.currentText()]

        brightness = int(self.brightness_slider.value())
        temperature = int(self.temperature_slider.value())
        gamma = xrandr.tuple_to_string(xrandr.temperature_to_rgb(temperature))
        
        for screen in screens:
            xrandr.change_screen_details(screen, brightness/100, gamma)

    def connect_slider_and_textbox(self, slider, textbox):
        textbox.textChanged.connect(lambda: slider.setValue(int(textbox.text()) if textbox.text().isdigit() else 0))
        slider.valueChanged.connect(lambda: textbox.setText(str(slider.value())))
        textbox.setText(str(slider.value()))

    def on_off_switch(self):
        if self.is_on:
            self.is_on = False

            current_screen = self.screens_comboBox.currentText()
            gamma = xrandr.tuple_to_string((1, 1, 1))
            xrandr.change_screen_details(current_screen, 1, gamma)

            print("OFF")
        else:
            self.is_on = True
            self.apply_changes()

            print("ON")

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtCore.QCoreApplication.translate("MainWindow", u"Bereshit", None))
        self.allscreens_check_box.setText(QtCore.QCoreApplication.translate("MainWindow", u"All Screens", None))
        self.brightness_label.setText(QtCore.QCoreApplication.translate("MainWindow", u"Brightness ", None))
        self.temperature_label.setText(QtCore.QCoreApplication.translate("MainWindow", u"Temperature", None))
        self.pushButton.setText(QtCore.QCoreApplication.translate("MainWindow", u"Turn ON/OFF", None))
