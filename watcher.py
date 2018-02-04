#
#   watcher class for mcUI
#
#   description:
#       this class aimed to output logs

class watcher:

    def __init__(self,mc):  # mc should mc.Minecraft()
        world = mc # get minecraft world itself


    def log(text): # simply, send log to minecraft
        world.postToChat("[Log]: " + text)
