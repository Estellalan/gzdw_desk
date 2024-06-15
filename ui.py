import sys


from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, pyqtSignal

import GetM1Result
import GetM2Result


class M2ResultWindow(QMainWindow): #运行评估结果界面
    def __init__(self,gzdw_data):
        super().__init__()
        self.gzdw_data = gzdw_data
        self.init_ui()
        self.setGeometry(100, 100, 800,500)
        self.img_DLMP = './DLMPs_'+gzdw_data+'.png'
        self.img_Loadshedding = './Loadshedding_'+gzdw_data+'.png'
        print("")
    def init_ui(self):
        self.ui = uic.loadUi("./M2ResultWindow.ui",self)

        self.button1 = self.ui.r_btn1
        self.button2 = self.ui.r_btn2


        self.label1 = self.ui.r_p1
        self.label2 = self.ui.r_p2


        self.button1.clicked.connect(self.r_run1_f)
        self.button2.clicked.connect(self.r_run2_f)


    def r_run1_f(self): #图片 负荷直接调控结果
        print(self.img_DLMP)
        pixmap = QPixmap(self.img_DLMP)
        self.label1.setPixmap(pixmap)
        self.label1.setScaledContents(True)

    def r_run2_f(self): #图片 负荷价格调控结果
        print(self.img_Loadshedding)
        pixmap = QPixmap(self.img_Loadshedding)
        self.label2.setPixmap(pixmap)
        self.label2.setScaledContents(True)



class M2Dialog1(QDialog): #导入运行数据（成功or失败）
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi("./M2Dialog1.ui",self)

class M2Dialog2(QDialog): #查看运行评估结果
    def __init__(self,gzdw_data):
        super().__init__()
        self.gzdw_data = gzdw_data
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi("./M2Dialog2.ui",self)
        self.button_show = self.ui.show_btn
        self.button_show.clicked.connect(self.show_result)
        print("")

    def show_result(self):
        self.result_window = M2ResultWindow(self.gzdw_data)
        self.result_window.show()
        print("show")


# 主窗口类


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.statusbar = None
        self.gzdw_data = "xinyi"

        self.init_ui()
        self.setGeometry(100, 100, 800,500)

    def init_ui(self):
        self.ui = uic.loadUi("./MainWindow.ui",self)

        self.statusbar = self.ui.statusbar

        self.m2_dialog2 = M2Dialog2(self.gzdw_data)
        #================================================
        self.button_run1 = self.ui.m1_run1
        #self.button_run2 = self.ui.m1_run2

        self.button_m2_btn1 = self.ui.m2_btn1
        self.button_m2_btn2 = self.ui.m2_btn2
        self.button_m2_btn3 = self.ui.m2_btn3

        self.label1 = self.ui.m1_p1
        self.label2 = self.ui.m1_p2
        self.label3 = self.ui.m1_p3
        self.label4 = self.ui.m2_p1

        self.action1 = self.ui.action1
        self.action2 = self.ui.action2
        #data_select_xinyin
        self.action_data_select_xinyi = self.ui.data_select_xinyi
        self.action_data_select_yinshan = self.ui.data_select_yinshan

        #===========================================
        self.action1.triggered.connect(self.open1)
        self.action2.triggered.connect(self.open2)
        self.action_data_select_xinyi.triggered.connect(lambda: self.select_data("xinyi"))
        self.action_data_select_yinshan.triggered.connect(lambda: self.select_data("yinshan"))

        self.button_run1.clicked.connect(self.m1_run1_f)
        #self.button_run2.clicked.connect(self.m1_run2_f)

        self.button_m2_btn1.clicked.connect(self.m2_run1_f)
        self.button_m2_btn2.clicked.connect(self.m2_run2_f)
        self.button_m2_btn3.clicked.connect(self.m2_run3_f)

    def select_data(self,data):
        self.gzdw_data = data
        print("using data: "+self.gzdw_data)
    def m2_run1_f(self): #导入电网数据
        self.gzdw_data_img_path = "image/"+self.gzdw_data+".png"
        self.gzdw_data_img = QPixmap(self.gzdw_data_img_path)
        self.label4.setPixmap(self.gzdw_data_img)
        self.label4.setScaledContents(True)
        #print("m2_run1")

    #显示运行数据成功窗口
    def m2_run2_f(self): #导入运行数据
        self.m2_dialog1 = M2Dialog1()
        self.m2_dialog1.show()

    def m2_run3_f(self): #运行评估
        print("run3")

        #self.getM2Result = GetM2Result(self,self.gzdw_data)

        self.thread_m2_matlab = GetM2Result.runMatlab(self.gzdw_data)
        #self.showStateBarMessgeM2ResultFinished()
        self.thread_m2_matlab.start()
        self.thread_m2_matlab.begin.connect(self.showStateBarMessgeM2ResultRuning)
        self.thread_m2_matlab.finished.connect(self.showStateBarMessgeM2ResultFinished)

        #self.thread_getResult = GetM2Result_xinyi.runMatlab()
        #self.thread_getResult.start() #开启matlab运行线程
        #self.thread_getResult.begin.connect(self.showStateBarMessgeM2ResultRuning)
        #self.thread_getResult.finished.connect( self.showStateBarMessgeM2ResultFinished)


        #self.openM2ResultDialog()

    def showStateBarMessgeM2ResultRuning(self):
            self.statusbar.showMessage("matlab程序正在运行，耗时较长，请稍等")

    def showStateBarMessgeM2ResultFinished(self):
            self.statusbar.showMessage("运行成功！请查看结果！")
            self.openM2ResultDialog()
            print("")
    def openM2ResultDialog(self):

        self.m2_dialog2 = M2Dialog2(self.gzdw_data)
        self.m2_dialog2.show()
        print("")

    def m1_run1_f(self): # 新能源消纳|线路传输容量
        self.thread_run_m1_matlab = GetM1Result.runMatlab(self.gzdw_data)
        #self.showStateBarMessgeM1ResultFinished() #直接显示图片，测试时使用
        self.thread_run_m1_matlab.start() #开启matlab运行线程
        self.thread_run_m1_matlab.begin.connect(self.showStateBarMessgeM1ResultRuning)
        self.thread_run_m1_matlab.finished.connect(self.showStateBarMessgeM1ResultFinished)



    def showStateBarMessgeM1ResultRuning(self):
            self.statusbar.showMessage("matlab程序正在运行，耗时较长，请稍等")

    def showStateBarMessgeM1ResultFinished(self):
            self.statusbar.showMessage("运行成功！请查看结果！")
            self.img_LC_path = 'LC_'+self.gzdw_data+'.png'
            self.img_REC_path = 'REC_'+self.gzdw_data+'.png'
            self.img_REC_change_path = 'REC_change_'+self.gzdw_data+'.png'

            print(self.img_LC_path+" "+self.img_REC_path+" "+self.img_REC_change_path)

            img_LC = QPixmap(self.img_LC_path)
            img_REC = QPixmap(self.img_REC_path)
            img_REC_change = QPixmap(self.img_REC_change_path)

            self.label1.setPixmap(img_LC)
            self.label2.setPixmap(img_REC)
            self.label3.setPixmap(img_REC_change)

            self.label1.setAlignment(Qt.AlignCenter)
            self.label2.setAlignment(Qt.AlignCenter)
            self.label3.setAlignment(Qt.AlignCenter)

            self.label3.setScaledContents(True)
            self.label1.setScaledContents(True)
            self.label2.setScaledContents(True)


    def open1(self): #打开模块1
        self.stackedWidget.setCurrentIndex(0)


    def open2(self): #打开模块2
        self.stackedWidget.setCurrentIndex(1)








# 主函数
def main():
    app = QApplication(sys.argv)
    main_window = Main()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
