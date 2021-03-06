# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Database_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1013, 767)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Top_box = QtWidgets.QHBoxLayout()
        self.Top_box.setObjectName("Top_box")
        self.Name_label = QtWidgets.QLabel(self.centralwidget)
        self.Name_label.setObjectName("Name_label")
        self.Top_box.addWidget(self.Name_label)
        self.Name_text = QtWidgets.QLineEdit(self.centralwidget)
        self.Name_text.setObjectName("Name_text")
        self.Top_box.addWidget(self.Name_text)
        self.Sex_label = QtWidgets.QLabel(self.centralwidget)
        self.Sex_label.setObjectName("Sex_label")
        self.Top_box.addWidget(self.Sex_label)
        self.Sex_text = QtWidgets.QLineEdit(self.centralwidget)
        self.Sex_text.setObjectName("Sex_text")
        self.Top_box.addWidget(self.Sex_text)
        self.Age_label = QtWidgets.QLabel(self.centralwidget)
        self.Age_label.setObjectName("Age_label")
        self.Top_box.addWidget(self.Age_label)
        self.Age_text = QtWidgets.QLineEdit(self.centralwidget)
        self.Age_text.setObjectName("Age_text")
        self.Top_box.addWidget(self.Age_text)
        self.Height_label = QtWidgets.QLabel(self.centralwidget)
        self.Height_label.setObjectName("Height_label")
        self.Top_box.addWidget(self.Height_label)
        self.Height_text = QtWidgets.QLineEdit(self.centralwidget)
        self.Height_text.setObjectName("Height_text")
        self.Top_box.addWidget(self.Height_text)
        self.Weight_label = QtWidgets.QLabel(self.centralwidget)
        self.Weight_label.setObjectName("Weight_label")
        self.Top_box.addWidget(self.Weight_label)
        self.Weight_text = QtWidgets.QLineEdit(self.centralwidget)
        self.Weight_text.setObjectName("Weight_text")
        self.Top_box.addWidget(self.Weight_text)
        self.verticalLayout.addLayout(self.Top_box)
        self.Middle_box = QtWidgets.QHBoxLayout()
        self.Middle_box.setObjectName("Middle_box")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.tableWidget.setFont(font)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.Middle_box.addWidget(self.tableWidget)
        self.verticalLayout.addLayout(self.Middle_box)
        self.Bottom_box = QtWidgets.QHBoxLayout()
        self.Bottom_box.setObjectName("Bottom_box")
        self.Connect_condition = QtWidgets.QLabel(self.centralwidget)
        self.Connect_condition.setMinimumSize(QtCore.QSize(100, 23))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Connect_condition.setFont(font)
        self.Connect_condition.setObjectName("Connect_condition")
        self.Bottom_box.addWidget(self.Connect_condition)
        self.Connect = QtWidgets.QPushButton(self.centralwidget)
        self.Connect.setObjectName("Connect")
        self.Bottom_box.addWidget(self.Connect)
        self.Disconnect = QtWidgets.QPushButton(self.centralwidget)
        self.Disconnect.setObjectName("Disconnect")
        self.Bottom_box.addWidget(self.Disconnect)
        self.Add_button = QtWidgets.QPushButton(self.centralwidget)
        self.Add_button.setObjectName("Add_button")
        self.Bottom_box.addWidget(self.Add_button)
        self.Save_button = QtWidgets.QPushButton(self.centralwidget)
        self.Save_button.setObjectName("Save_button")
        self.Bottom_box.addWidget(self.Save_button)
        self.Delete_button = QtWidgets.QPushButton(self.centralwidget)
        self.Delete_button.setObjectName("Delete_button")
        self.Bottom_box.addWidget(self.Delete_button)
        self.Search_button = QtWidgets.QPushButton(self.centralwidget)
        self.Search_button.setObjectName("Search_button")
        self.Bottom_box.addWidget(self.Search_button)
        self.verticalLayout.addLayout(self.Bottom_box)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1013, 21))
        self.menubar.setObjectName("menubar")
        self.Menu_file = QtWidgets.QMenu(self.menubar)
        self.Menu_file.setObjectName("Menu_file")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.Exit_option = QtWidgets.QAction(MainWindow)
        self.Exit_option.setObjectName("Exit_option")
        self.Menu_file.addAction(self.Exit_option)
        self.menubar.addAction(self.Menu_file.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Database"))
        self.Name_label.setText(_translate("MainWindow", "Name"))
        self.Sex_label.setText(_translate("MainWindow", "Sex"))
        self.Age_label.setText(_translate("MainWindow", "Age"))
        self.Height_label.setText(_translate("MainWindow", "Height"))
        self.Weight_label.setText(_translate("MainWindow", "Weight"))
        self.Connect_condition.setText(_translate("MainWindow", "Disconnect"))
        self.Connect_condition.setStyleSheet("color:red")
        self.Connect.setText(_translate("MainWindow", "Connect"))
        self.Disconnect.setText(_translate("MainWindow", "Disconnect"))
        self.Disconnect.setEnabled(False)
        self.Add_button.setText(_translate("MainWindow", "Add"))
        self.Save_button.setText(_translate("MainWindow", "Save"))
        self.Delete_button.setText(_translate("MainWindow", "Delete"))
        self.Search_button.setText(_translate("MainWindow", "Serach"))
        self.Menu_file.setTitle(_translate("MainWindow", "File"))
        self.Exit_option.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
