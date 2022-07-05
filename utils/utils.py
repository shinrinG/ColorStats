import os
import datetime
import inspect

def find_all_files(directory,extention="csv"):
    filelist=[]
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file[-3:] == extention:
                filelist.append(os.path.join(root, file))
    return filelist
def find_all_dirs(path):
    slice = len(path)
    s_dirs = [curDir[slice:] for curDir, dirs, files in os.walk(path)]
    s_dirs.remove("")
    return s_dirs

def make_dir(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    return True

def get_curtime():
    return datetime.datetime.now().strftime("%Y%m%d%H%M%S")

class logger:
    _path=""
    _bExists = True
    def __init__(self,filepath):
       self._path=filepath
       if not os.path.exists(filepath):
           self._bExists = False
    
    def bExsists(self):
        return self._bExists

    def write(self,message):
        #Get Stackframe
        stack_frame = inspect.stack()[1]
        frame = stack_frame[0]
        info = inspect.getframeinfo(frame)
        #Create LoggingLine
        linetxt = ""
        linetxt += datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S ")
        linetxt += (info.filename + " ")
        linetxt += (str(info.lineno) + " ")
        linetxt += message
        linetxt += "\n"

        #Write
        with open(self._path, "a") as f:
            f.write(linetxt)

    def writeout(self,message):
        #Get Stackframe
        stack_frame = inspect.stack()[1]
        frame = stack_frame[0]
        info = inspect.getframeinfo(frame)
        #Create LoggingLine
        linetxt = ""
        linetxt += datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S ")
        linetxt += (info.filename + " ")
        linetxt += (str(info.lineno) + " ")
        linetxt += message

        print(linetxt)
        linetxt += "\n"
        
        #Write
        with open(self._path, "a") as f:
            f.write(linetxt)

class hist:
    _path=""
    def __init__(self,filepath):
       self._path=filepath

    def write(self,message):
        #Write
        with open(self._path, "a") as f:
            linetxt =""
            linetxt += message
            f.write(linetxt)