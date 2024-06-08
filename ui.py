import sys


from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, pyqtSignal

import GetM2Result


class M2ResultWindow(QMainWindow): #运行评估结果界面
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.setGeometry(100, 100, 800,500)

    def init_ui(self):
        self.ui = uic.loadUi("./M2ResultWindow.ui",self)

        self.button1 = self.ui.r_btn1
        self.button2 = self.ui.r_btn2
        self.button3 = self.ui.r_btn3

        self.label1 = self.ui.r_p1
        self.label2 = self.ui.r_p2
        self.label3 = self.ui.r_p3

        self.button1.clicked.connect(self.r_run1_f)
        self.button2.clicked.connect(self.r_run2_f)
        self.button3.clicked.connect(self.r_run3_f)


    def r_run1_f(self): #图片 负荷直接调控结果
        print("1")
        pixmap = QPixmap('./DLMPs.png')
        self.label1.setPixmap(pixmap)
        self.label1.setScaledContents(True)

    def r_run2_f(self): #图片 负荷价格调控结果
        print("2")
        pixmap = QPixmap('./ Loadshedding.png')
        self.label2.setPixmap(pixmap)
        self.label2.setScaledContents(True)

    def r_run3_f(self): #表格 负荷多元联动调控成本
        print("3")
        pixmap = QPixmap('./image/r3.png')
        self.label3.setPixmap(pixmap)
        self.label3.setScaledContents(True)

class M2Dialog1(QDialog): #导入运行数据（成功or失败）
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi("./M2Dialog1.ui",self)

class M2Dialog2(QDialog): #查看运行评估结果
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi("./M2Dialog2.ui",self)
        self.button_show = self.ui.show_btn
        self.button_show.clicked.connect(self.show_result)

    def show_result(self):
        self.result_window = M2ResultWindow()
        self.result_window.show()
        #print("show")


class M2Dialog2Waiting(QDialog):  # 等待运行评估结果
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi("./M2Dialog2Waiting.ui", self)



# 主窗口类
class M2Dialog2Waiting1(QDialog): #查看运行评估结果
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi("./M2Dialog2Waiting.ui",self)


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.setGeometry(100, 100, 800,500)

    def init_ui(self):
        self.ui = uic.loadUi("./MainWindow.ui",self)

        self.m2_dialog2 = M2Dialog2()
        #================================================
        self.button_run1 = self.ui.m1_run1
        self.button_run2 = self.ui.m1_run2

        self.button_m2_btn1 = self.ui.m2_btn1
        self.button_m2_btn2 = self.ui.m2_btn2
        self.button_m2_btn3 = self.ui.m2_btn3

        self.label1 = self.ui.m1_p1
        self.label2 = self.ui.m1_p2
        self.label3 = self.ui.m1_p3
        self.label4 = self.ui.m2_p1

        self.action1 = self.ui.action1
        self.action2 = self.ui.action2

        #===========================================
        self.action1.triggered.connect(self.open1)
        self.action2.triggered.connect(self.open2)

        self.button_run1.clicked.connect(self.m1_run1_f)
        self.button_run2.clicked.connect(self.m1_run2_f)

        self.button_m2_btn1.clicked.connect(self.m2_run1_f)
        self.button_m2_btn2.clicked.connect(self.m2_run2_f)
        self.button_m2_btn3.clicked.connect(self.m2_run3_f)

    def m2_run1_f(self): #导入电网数据
        pixmap = QPixmap('./image/img.png')
        self.label4.setPixmap(pixmap)
        self.label4.setScaledContents(True)
        #print("m2_run1")

    #显示运行数据成功窗口
    def m2_run2_f(self): #导入运行数据
        self.m2_dialog1 = M2Dialog1()
        self.m2_dialog1.show()

    def m2_run3_f(self): #运行评估
        print("run3")

        self.openM2WaitingDailog()

        self.thread_getResult = GetM2Result.runMatlab()
        self.thread_getResult.start() #开启matlab运行线程
        self.thread_getResult.finished.connect(self.openM2ResultDialog)
        #GetM2Result.startM2ResultMain()
        #self.u_thread.finished.connect(self.finishUNV)

        #self.openM2ResultDialog()

    def openM2WaitingDailog(self):
        self.m2_dialog2Waiting = M2Dialog2Waiting()
        self.m2_dialog2Waiting.show()

    def openM2ResultDialog(self):
        print("openM2ResultDialog")
        self.m2_dialog2Waiting.close()
        self.m2_dialog2 = M2Dialog2()
        self.m2_dialog2.show()

    def m1_run1_f(self):
        pixmap1 = QPixmap('./image/p1.png')  # 替换为图片文件路径
        pixmap2 = QPixmap('./image/p2.png')


        self.label1.setPixmap(pixmap1)
        self.label2.setPixmap(pixmap2)

        self.label1.setScaledContents(True)
        self.label2.setScaledContents(True)
        #print("run:1")

    def m1_run2_f(self):
        pixmap = QPixmap('./image/p3.png')
        self.label3.setPixmap(pixmap)
        self.label3.setScaledContents(True)
        #print("run:2")
    def open1(self): #打开模块1
        self.stackedWidget.setCurrentIndex(0)
        #print("11111")

    def open2(self): #打开模块2
        self.stackedWidget.setCurrentIndex(1)
        #print("22222")







# 主函数
def main():
    app = QApplication(sys.argv)
    main_window = Main()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
