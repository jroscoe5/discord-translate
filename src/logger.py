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
    
    def log_msg(self, msg):
        if self.verbosity == Verbosity.none:
            return
        if self.verbosity == Verbosity.high:
            self.log(str(msg.author) + ' in channel ' + str(msg.channel) + ':  ' + msg.content)
        elif self.verbosity == Verbosity.medium:
            self.log(str(msg.author) + ': ' + msg.content)
    
    def log_trans(self, trans):
        pass
    
    def log_exc(self, exc):
        pass