import sys
from PySide2.QtWidgets import QApplication, QMainWindow 
from gui import Ui_MainWindow, SystemTryWidgit


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    MainWindow = QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()

    tray_icon = SystemTryWidgit()
    tray_icon.setupUi(MainWindow, app)
    
    app.exec_()


