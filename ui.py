import sys


from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

# 主窗口类
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.setGeometry(100, 100, 800,500)

    def init_ui(self):
        self.ui = uic.loadUi("./MainWindow.ui",self)


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
        self.action1.triggered.connect(self.open1)

        self.action2 = self.ui.action2
        self.action2.triggered.connect(self.open2)



        self.button_run1.clicked.connect(self.m1_run1_f)
        self.button_run2.clicked.connect(self.m1_run2_f)

        self.button_m2_btn1.clicked.connect(self.m2_run1_f)
        self.button_m2_btn2.clicked.connect(self.m2_run2_f)
        self.button_m2_btn3.clicked.connect(self.m2_run3_f)

    def m2_run1_f(self):
        pixmap = QPixmap('./image/img.png')
        self.label4.setPixmap(pixmap)
        self.label4.setScaledContents(True)

    def m2_run2_f(self):
        print("2222")

    def m2_run3_f(self):
        print("3333")


    def m1_run1_f(self):
        pixmap1 = QPixmap('./image/p1.png')  # 替换为您的图片文件路径
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
    def open1(self):
        self.stackedWidget.setCurrentIndex(0)
        #print("11111")

    def open2(self):
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
