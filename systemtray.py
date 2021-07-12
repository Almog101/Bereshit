import PySide2.QtGui as QtGui
import PySide2.QtWidgets as QtWidgets 

ICON_PATH = "./src/icon.png"

class SystemTryWidgit:
    def setupUi(self):
        app = QtWidgets.QApplication([])
        app.setQuitOnLastWindowClosed(False)
        
        # Adding item on the menu bar
        self.tray = QtWidgets.QSystemTrayIcon()
        self.tray.setIcon(QtGui.QIcon(ICON_PATH))
        self.tray.setVisible(True)
        
        # Creating the options
        self.menu = QtWidgets.QMenu()
        self.add_option("test1", lambda: print(1))
        self.add_option("test2", lambda: print(2))
        self.add_option("quit", app.quit)

        """
        option1 = QtWidgets.QAction("Geeks for Geeks")
        option2 = QtWidgets.QAction("GFG")

        option1.triggered.connect(lambda: print(1))

        self.menu.addAction(option1)
        self.menu.addAction(option2)
        
        self.add_new_option("asda",1)

        # To quit the app
        quit = QtWidgets.QAction("Quit")
        quit.triggered.connect(app.quit)
        self.menu.addAction(quit)
        """

        # Adding options to the System Tray
        self.tray.setContextMenu(self.menu)
        
        app.exec_()

    def add_option(self, option_name, function):
        pass
        #option = QtWidgets.QAction(option_name)
        #option.triggered.connect(function)
        #self.menu.addAction(option)

if __name__ == "__main__":
    SystemTryWidgit().setupUi()
 