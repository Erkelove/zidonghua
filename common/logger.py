import logging
import os.path
import time

BASEPATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LogPath = os.path.join(BASEPATH, 'log')
if not os.path.exists(LogPath):
    os.mkdir(LogPath)

class Logger():

    def __init__(self):
        #日志记录的路径的文件
        self.logname = os.path.join(LOG_PATH, "{}.log".format(time.strftime("%Y-%m-%d")))
        #获取日志对象
        self.logger = logging.getLogger("log")
        #设置日志的级别
        self.logger.setLevel(logging.DEBUG)
        #生成日志的时间格式%(asctime)s：日志何时被创建的具体到毫秒；%(filename)s：日志是哪个模块产生的；%(lineno)d：日志在哪一行产生的
        #%(levelname)s：日志的级别；%(message)s：日志的具体信息。
        self.formater = logging.Formatter(
            '[%(asctime)s][%(filename)s %(lineno)d][%(levelname)s]: %(message)s')
        #设置日志导入的具体文件的处理器
        self.filelogger = logging.FileHandler(self.logname, mode='a', encoding="UTF-8")
        #StreamHandler 标准流处理器，将消息发送到标准输出流、错误流
        self.console = logging.StreamHandler()
        #设置日志的级别
        self.console.setLevel(logging.DEBUG)
        self.filelogger.setLevel(logging.DEBUG)
        #设置日志的具体写入格式
        self.filelogger.setFormatter(self.formater)
        self.console.setFormatter(self.formater)
        #增加日志导入的处理器，确定日志导入位置
        self.logger.addHandler(self.filelogger)
        self.logger.addHandler(self.console)