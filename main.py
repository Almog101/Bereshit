import sys
from PySide2.QtWidgets import QApplication, QMainWindow 
from main_window import Ui_MainWindow
from systemtray import SystemTryWidgit


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()
