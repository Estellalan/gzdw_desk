import os

import matlab.engine
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal, QThread
from PyQt5.QtWidgets import QDialog

from ui import M2Dialog1, M2Dialog2Waiting, M2Dialog2


class runWaiting:
    def openWaiting(self):
        print("runWaiting....")

        self.m2_dialog2Waiting = M2Dialog2Waiting()
        self.m2_dialog2Waiting.show()



class runMatlab(QThread):

    finished = pyqtSignal()

    def __init__(self):
        super().__init__()

    def run(self):
        print("runMatlab....")
        self.startM2ResultMain() #运行matlab
        self.finished.emit()


    def startM2ResultMain(self):
        eng = matlab.engine.start_matlab()

        # 获取当前Python脚本所在目录的绝对路径
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # 构建MATLAB文件相对于Python脚本的路径
        relative_matlab_path = './guizhou_xinyi'
        absolute_matlab_path = os.path.join(current_dir, relative_matlab_path)

        # 启动MATLAB引擎
        eng = matlab.engine.start_matlab()

        # 将MATLAB文件所在的目录添加到MATLAB的搜索路径中
        eng.addpath(absolute_matlab_path, nargout=0)

        # 调用MATLAB脚本
        eng.run('main', nargout=0)

        eng.quit()