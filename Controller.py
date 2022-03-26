from UI import Ui_MainWindow
import cv2            # 引入 OpenCV 的模組，製作擷取攝影機影像之功能
import sys, time      # 引入 sys 跟 time 模組
import numpy as np    # 引入 numpy 來處理讀取到得影像矩陣
from functools import partial
from PyQt5.Qt import QWidget
from PyQt5 import QtGui,QtWidgets,QtCore
from PyQt5.QtWidgets import (QFrame,QApplication,QDialog, QDialogButtonBox,
        QMessageBox,QVBoxLayout, QLineEdit,QTableWidgetItem,QTableWidget,QHBoxLayout)
from Database_Controller import Database_Controller
import  limbstretch as ls

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow_controller, self).__init__(parent)
        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)

        # 設定 Frame Rate 的參數
        self.frame_num = 0

        # 設定相機功能
        self.ProcessCam = Camera()  # 建立相機物件

        if self.ProcessCam.connect:
            #self.debugBar(&#039;Connection!!!&#039;)
            # 連接影像訊號 (rawdata) 至 getRaw()

            self.ProcessCam.rawdata.connect(self.getRaw)  # 槽功能：取得並顯示影像
            # 攝影機啟動按鈕的狀態：ON
            self.ui.Open_button.setEnabled(True)
        else:
            #self.debugBar( &  # 039;Disconnection!!!&#039;)
            # 攝影機啟動按鈕的狀態：OFF
            self.ui.Open_button.setEnabled(False)
           #self.ui.Screen.setPixmap(QtGui.QPixmap(""))
            # 攝影機的其他功能狀態：OFF
        self.ui.Close_button.setEnabled(False)

        self.ui.Database_option.triggered.connect(self.Open_database)
        self.ui.Exit_option.triggered.connect(self.close)
        self.ui.Open_button.clicked.connect(self.Open_cam)
        self.ui.Close_button.clicked.connect(self.Close_cam)
    def getRaw(self, data):  # data 為接收到的影像
        """ 取得影像 """
        self.showData(data)  # 將影像傳入至 showData()

    def Open_cam(self):
        """ 啟動攝影機的影像讀取 """
        if self.ProcessCam.connect:  # 判斷攝影機是否可用
            self.ProcessCam.open()   # 影像讀取功能開啟
            self.ProcessCam.start()  # 在子緒啟動影像讀取
            # 按鈕的狀態：啟動 OFF、暫停 ON、視窗大小 ON
            self.ui.Open_button.setEnabled(False)
            self.ui.Close_button.setEnabled(True)

    def Close_cam(self):
        """ 凍結攝影機的影像 """
        if self.ProcessCam.connect:  # 判斷攝影機是否可用
            self.ProcessCam.stop()# 影像讀取功能關閉
            time.sleep(1)
            self.ProcessCam.terminate()
            #self.ui.Screen.clear()
            # 按鈕的狀態：啟動 ON、暫停 OFF、視窗大小 OFF
            self.ui.Open_button.setEnabled(True)
            self.ui.Close_button.setEnabled(False)

    #開啟資料庫視窗
    def Open_database(self):
        Database_window = Database_Controller()
        Database_window.show()

    def showData(self, img):
        try:
            """ 顯示攝影機的影像 """
            self.Ny, self.Nx, _ = img.shape  # 取得影像尺寸

            # 建立 Qimage 物件 (RGB格式)
            qimg = QtGui.QImage(img.data, self.Nx, self.Ny, QtGui.QImage.Format_RGB888)

            ### 將 Qimage 物件設置到 Screen 上
            self.ui.Screen.setPixmap(QtGui.QPixmap.fromImage(qimg))

            # Frame Rate 計算並顯示到狀態欄上
            if self.frame_num == 0:
                self.time_start = time.time()
            if self.frame_num >= 0:
                self.frame_num += 1
                self.t_total = time.time() - self.time_start
                if self.frame_num % 100 == 0:
                    self.frame_rate = float(self.frame_num) / self.t_total
        except Exception as ex:
            print (ex)



class Camera(QtCore.QThread):  # 繼承 QtCore.QThread 來建立 Camera 類別
    rawdata = QtCore.pyqtSignal(np.ndarray)  # 建立傳遞信號，需設定傳遞型態為 np.ndarray

    def __init__(self, parent=None):
        super().__init__(parent)
        """ 初始化
            - 執行 QtCore.QThread 的初始化
            - 建立 cv2 的 VideoCapture 物件
            - 設定屬性來確認狀態
              - self.connect：連接狀態
              - self.running：讀取狀態
        """

        # 建立 cv2 的攝影機物件
        self.cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.cam.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
        self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

        # 判斷攝影機是否正常連接
        if self.cam is None or not self.cam.isOpened():
            self.connect = False
            self.running = False
        else:
            self.connect = True
            self.running = False

    def run(self):
        """ 執行多執行緒
            - 讀取影像
            - 發送影像
            - 簡易異常處理
        """
        # 當正常連接攝影機才能進入迴圈
        while self.running and self.connect:
            try:
                ret, img = self.cam.read()  # 讀取影像
                if ret:
                    #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                    img = ls.basic_Process(img)
                    self.rawdata.emit(img)  # 發送影像
                else:  # 例外處理
                    print("Warning!!!")
                    self.connect = False
            except Exception as ex:
                print(ex)

    def open(self):
        """ 開啟攝影機影像讀取功能 """
        if self.connect:
            self.running = True  # 啟動讀取狀態

    def stop(self):
        """ 暫停攝影機影像讀取功能 """
        if self.connect:
            self.running = False  # 關閉讀取狀態

    def close(self):
        """ 關閉攝影機功能 """
        if self.connect:
            self.running = False  # 關閉讀取狀態
            time.sleep(1)
            self.cam.release()  # 釋放攝影機