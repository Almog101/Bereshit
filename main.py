import sys
from PySide2.QtWidgets import QApplication, QMainWindow 
from gui import Ui_MainWindow, SystemTryWidgit


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    tray_icon = SystemTryWidgit()
    tray_icon.setupUi(MainWindow)
    
    ret = app.exec_()
    sys.exit(ret)


