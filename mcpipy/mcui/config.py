# DON'T CUSTOM HERE{{{
import mcpi.block as block
from mcpi.vec3 import Vec3
# }}}


margin = 5 # mergin from player position to center of objects' spawing place
padding = Vec3(3, 0, 0) # padding between each objects
line_vec = Vec3(0, 3, 0) # vector to define which axis should objects follow
MAX_OBJECT_PER_LINE = 3 # How much objects could be in one line?


# File related {{{

# List of set of filetypes and extension list
# If the extension is not defined here,
# that file will be set to 'unknown'
filetype_list = {"": "text",
                 ".txt": "text",
                 ".md": "markdown",
                 ".markdown": "markdown",
                 ".sh": "shellscript",
                 ".py": "python",
                 ".rb": "ruby",
                 ".config": "config",
                 ".cfg": "config",
                 ".html": "html",
                 ".css": "css",
                 ".js": "javascript",
                 ".c": "c",
                 ".cpp": "c++",
                 ".exe": "windows-executable",
                 ".swp": "vim-swap-file",
                 ".swo": "vim-swap-file",
                 ".pyc": "python-cash"
                }

# Define what block should be used for each filetype
#
# I know the name 'schema' doesn't suit to this usage,
#  so I'll change it later
#
# Feature:  want to separate this to something like 'texture pack'
#           so that people can share their own configure like vim's
#           colorscheme
schema = {"file": block.WOOL,
          "dir": block.IRON_BLOCK,
          "text": block.WOOL_WHITE,
          "markdown": block.WOOL_ORANGE,
          "python": block.WOOL_YELLOW,
          "shellscript": block.WOOL_LIGHT_BLUE,
          "ruby": block.WOOL_MAGENTA,
          "config": block.SANDSTONE,
          "html": block.WOOL_LIME,
          "css": block.WOOL_YELLOW,
          "javascript": block.WOOL_CYAN,
          "c": block.WOOL_RED,
          "cpp": block.WOOD_PLANKS,
          "windows-executable": block.DIRT_PODZOL,
          "vim-swap-file": block.WOOD_PLANKS_ACACIA,
          "python-cash": block.WOOD_PLANKS_ACACIA,
          "unknown": block.DIRT}

# }}}
