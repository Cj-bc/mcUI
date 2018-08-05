#
#   main for mcUI 
# 


# import mc from upper dir. I'm not sure about detail
import sys,os
sys.path.append(os.pardir)
from mc import *
import commonerror,watcher,initialize,config

world = Minecraft() # connect to minecraft

# initialize
initialize.initialize.playerinit(world)
