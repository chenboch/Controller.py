from Database_UI import Ui_MainWindow
import pymysql
from functools import partial
from PyQt5.Qt import QWidget
from PyQt5 import QtGui,QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QFrame,QApplication,QDialog, QDialogButtonBox,
        QMessageBox,QVBoxLayout, QLineEdit,QTableWidgetItem,QTableWidget,QHBoxLayout)

class Database_Controller(QtWidgets.QMainWindow):
    def __init__(self):
        # in python3, super(Class, self).xxx = super().xxx
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 資料庫設定
        # host:MySql服務器地址
        # port:MySql服務器port
        # user:用戶名
        # passwd:密碼
        # db:數據庫名稱
        # charst:連結編碼
        db_settings = {
            "host": "127.0.0.1",
            "port": 3306,
            "user": "root",
            "password": "123456",
            "db": "project",
            "charset": "utf8"
        }
        # 建立Connection物件
        conn = pymysql.connect(**db_settings)
        # 獲取遊標、資料
        cursor = conn.cursor()
        sql = "SELECT * FROM project.test"
        cursor.execute(sql)

        # 資料列名
        col_lst = [tup[0] for tup in cursor.description]

        # 獲取資料庫的大小
        data = cursor.fetchall()
        row = len(data)
        col = len(data[0])

        # 設定表格大小
        self.ui.tableWidget.setRowCount(row)
        self.ui.tableWidget.setColumnCount(col)

        # 設定字型
        font = QtGui.QFont('微軟雅黑', 10)
        self.ui.tableWidget.horizontalHeader().setFont(font)

        #按鈕設定
        self.ui.Connect.clicked.connect(partial(self.Connect,cursor,conn,data,row,col,col_lst))  #連線按紐
        self.ui.Disconnect.clicked.connect(partial(self.Disconnect,cursor,conn))  #斷連結按鈕

        self.ui.Add_button.clicked.connect(partial(self.add_data,cursor,conn))  #新增表格按鈕
        self.ui.Delete_button.clicked.connect(partial(self.del_data,cursor,conn))   #刪除資料按鈕
        self.ui.Save_button.clicked.connect(partial(self.save_data,cursor,conn,col_lst))  #新增資料按鈕
        self.ui.Exit_option.triggered.connect(self.close)

    def Connect(self,cursor,conn,data,row,col,col_lst):



        self.ui.Connect_condition.setText("Connect")
        self.ui.Connect_condition.setStyleSheet("color:green")

        # 設定標頭
        self.ui.tableWidget.setHorizontalHeaderLabels(col_lst)

        # 連線成功對話方塊
        con_s = QMessageBox.information(self, 'Message', 'Successfully connected' )

        # 構建表格插入資料
        for i in range(row):
            for j in range(col):
                temp_data = data[i][j]  # 臨時記錄，不能直接插入表格
                data1 = QtWidgets.QTableWidgetItem(str(temp_data))  # 轉換後可插入表格
                self.ui.tableWidget.setItem(i, j, data1)

        self.ui.Connect.setEnabled(False)   #設定連線資料庫按鈕不可按
        self.ui.Disconnect.setEnabled(True) #設定斷開資料庫按鈕可按

    # 新增空表格
    def add_data(self, cur, db):
        # 獲取行數
        cur_row = self.ui.tableWidget.rowCount()
        # 在末尾插入一空行
        self.ui.tableWidget.insertRow(cur_row)

    #新增資料
    def save_data(self, cursor, conn,col_lst):
        #獲取當前行數
        cur_row = self.ui.tableWidget.rowCount()

        #資料收集
        value_lst = []
        for i in range(len(col_lst)):
            if (len(self.ui.tableWidget.item(cur_row - 1, i).text()) == 0):
                value_lst.append(None)
            else:
                value_lst.append(self.ui.tableWidget.item(cur_row - 1, i).text())

        # 插入語句
        sql = "INSERT INTO test (name, sex,age,height,weight) VALUES (%s, %s, %s, %s, %s)"

        # 在資料庫刪除資料
        cursor.execute(sql,value_lst)
        conn.commit()

        # 新增成功對話方塊
        ins_s = QMessageBox.information(self, 'Message', 'Successfully inserted '+ value_lst[0] + '!')

    # 刪除
    def del_data(self, cur, db):
        # 所點選的那行
        row_select = self.ui.tableWidget.currentRow()
        del_d = self.ui.tableWidget.item(row_select, 0).text()

        # 是否刪除資料的對話方塊
        reply = QMessageBox.question(self, 'Message', 'Are you sure to delete '+del_d+' ?', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            #在資料庫刪除資料
            cur.execute("DELETE FROM test WHERE name = '" + del_d + "'")
            db.commit()

            # 刪除表格
            self.ui.tableWidget.removeRow(row_select)

        #刪除成功對話方塊
        del_s = QMessageBox.information(self,'Message', 'Successfully deleted '+del_d)

    #斷開連結
    def Disconnect(self,cursor,conn,col_lst):

        # 連線成功對話方塊
        dis_s = QMessageBox.information(self, 'Message', 'Successfully disconnected')
        conn.close()
        self.ui.Connect_condition.setText("Disconnect")
        self.ui.Connect_condition.setStyleSheet("color:red")
        self.ui.tableWidget.clear()
        self.ui.Connect.setEnabled(True)    #設定連線資料庫按鈕可按
        self.ui.Disconnect.setEnabled(False)#設定斷開資料庫按鈕不可按