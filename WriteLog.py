#! /usr/bin/env python
import logging

class Logger:
    def __init__(self, path, clevel = logging.NOTSET, Flevel = logging.DEBUG):
        self.logger = logging.getLogger(path)
        self.logger.setLevel(logging.DEBUG)
        fmt = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
        
        #Setting CMD log
        if (clevel != logging.NOTSET):
            sh = logging.StreamHandler()
            sh.setFormatter(fmt)
            sh.setLevel(clevel)
            self.logger.addHandler(sh)

        #Setting log file
        if (Flevel != logging.NOTSET):
            fh = logging.FileHandler(path)
            fh.setFormatter(fmt)
            fh.setLevel(Flevel)
            self.logger.addHandler(fh)
 
    def debug(self, message):
        self.logger.debug(message)
 
    def info(self, message):
        self.logger.info(message)
 
    def warn(self, message):
        self.logger.warning(message)
 
    def error(self, message):
        self.logger.error(message)
 
    def critical(self, message):
        self.logger.critical(message)
 
if __name__ =='__main__':
    logtest = Logger('test.log', logging.ERROR, logging.DEBUG)
    logtest.debug('a debug msg.')
    logtest.info('an info msg.')
    logtest.warn('a warning msg.')
    logtest.error('a error msg.')
    logtest.critical('a critical msg.')