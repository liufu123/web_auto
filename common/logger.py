import logging
import time
import os

log_path = os.path.dirname(os.path.abspath('.')) + '/report'
print(log_path)

class Log():
    def __init__(self):
        self.logname = os.path.join(log_path,'%s.log'%time.strftime('%Y_%m_%d'))
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter('%(asctime)s - %(filename)s -  %(levelname)s:%(message)s')

    def console(self,level,message):
        fh = logging.FileHandler(self.logname,'a',encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)
        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)

        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        fh.close()

    def debug(self,message):
        self.console('debug',message)

    def info(self,message):
        self.console('info',message)

    def warning(self,message):
        self.console('warning',message)

    def error(self,message):
        self.console('error',message)

if __name__ == "__main__":
    log = Log()
    log.info("--测试开始--")
    log.warning('--测试结束--')