import os

import matlab.engine

def startM2ResultMain():
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

    # 调用MATLAB函数
    eng.main()

    eng.quit()

if __name__ == '__main__':
    startM2ResultMain()