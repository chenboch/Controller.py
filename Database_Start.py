from PyQt5 import QtWidgets

from Database_Controller import Database_Controller

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Database_Controller()
    window.show()
    sys.exit(app.exec_())