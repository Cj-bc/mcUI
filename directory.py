#
#   Directory class for mcUI 
# 


# import mc from upper dir. I'm not sure about detail
import sys,os
sys.path.append(os.pardir)
from mc import *
import commonerror

class directory:

    path
    dirname
    childrens

    def __init__(self,world,parent):
        try
            path = parent if os.path.exists(parent) else raise UnexistError
        except UnexistError
           path = None
           raise
