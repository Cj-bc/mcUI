# wrapper script of mcUI (for python2)

import os
import subprocess

mcUI_path = os.path.dirname(os.path.abspath(__file__)) + "/mcui/mcUI.py"
subprocess.call(["/usr/local/bin/python3", mcUI_path])
