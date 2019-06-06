# python 3.7.1

from threading import Lock
from datetime import datetime

class Verbosity:
    none    = 0
    low     = 1
    medium  = 2
    high    = 3
    values = [0,1,2,3]

class Logger():

    def __init__(self, stream, verbosity:int):
        if verbosity not in Verbosity.values:
            raise Exception('Provided verbosity value is invalid')
        self.stream = stream
        self.verbosity = verbosity
        self.lock = Lock()
    
    def log(self, msg):
        if self.verbosity == Verbosity.none:
            return
        try:
            self.lock.acquire()
            self.stream.write(str(datetime.now()) + ' || ' + msg + ' \n')
            self.stream.flush()
            self.lock.release()
        except Exception as exc:
            raise exc
    
    def logMsg(self, msg):
        if self.verbosity == Verbosity.none:
            return
        if self.verbosity == Verbosity.high:
            self.log('Recieved msg from: ' + str(msg.author))
        if self.verbosity >= Verbosity.medium:
            self.log('Content: ' + msg.content)

            


if __name__ == '__main__':
    from os import sys
    file = open('test.txt','w')
    logger = Logger(sys.stdout, 2)
    print(logger.verbosity)
    logger.log('hello, world')
