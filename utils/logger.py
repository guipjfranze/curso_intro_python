import time
import os

class Logger():
    def __init__(self,fileName):
        self.fileName = fileName
        self.time = "{} ".format(time.strftime('<%Y-%m-%d %H:%M:%S>', time.gmtime()))
        self.file = open(fileName,'a+')


    def info(self,text):
        txt = (self.time+"[INFO] "+ "{}\n".format(text))
        print(txt)
        self.file.write(txt)
    def warning(self,text):
        txt = (self.time+"[WARNING] "+"{}\n".format(text))
        print(txt)
        self.file.write(txt)
    def error(self,text):
        txt = (self.time+"[ERROR] "+"{}\n".format(text))
        print(txt)
        self.file.write(txt)
    def done(self,text):
        txt = (self.time+"[DONE] "+"{}\n".format(text))
        print(txt)
        self.file.write(txt)
    def result(self,text):
        txt = (self.time+"[RESULT] "+"{}\n".format(text))
        print(txt)
        self.file.write(txt)
    def close(self):
        self.file.close()

