#!/usr/bin/env python3
#
# mcUI --- minecraft based 3D UI for *nix
#
# copyright (c) 2019 Cj-bc a.k.a Cj.bc_sd
#
# (@) version: 0.0.2
# (@) usage:
# (@)   run this script while Minecraft is running.


import mcpi.minecraft as minecraft
import mcpi.block as block
# import mcpi.entity as entity
from mcpi.vec3 import Vec3
import os


# functions {{{
# get_schemas() {{{2
def get_schemas():
    """get list of blocks for each filetype

        Args:
            no args
        Return:
            schema (dict): key is "filetype", value is "block"
    """
    # TODO: remove this hardcoded data scheme
    schema = {"file": block.WOOL,
              "dir": block.IRON_BLOCK,
              "unknown": block.DIRT}
    return schema
# }}}


# ls(path) {{{2
def ls(path):
    """get current directory's entries and return list

       Args:
            path (str): POSIX path to serch files
       Return:
            files (list of dict): list of "path" entries.
            [ {"type": <file, dir>,
               "name": <file_name>},
               ...
            ]
    """
    ret = []
    with os.scandir(path) as it:
        for f in it:
            # TODO: remove this hardcoded data scheme
            if f.is_file():
                ret += [{"type": "file", "name": f.name}]
            elif f.is_dir():
                ret += [{"type": "dir", "name": f.name}]
            else:
                ret += [{"type": "unknown", "name": f.name}]

    return ret
# }}}


# write_files(start_pos, files) {{{2
def write_files(start_pos, files):
    """write "files" file entries to minecraft world
        Number of objects lay in one line is defined as MAX_OBJECT_PER_LINE

        Args:
            start_pos (vec3.Vec3): vec3 object which points the first position to generate
            files (list of dict): generated by ls(); list of 'path's entries
        Return:
            no return
    """
    schemas = get_schemas()
    counter = 0
    for obj in files:
        mc.setBlock(start_pos.x + counter*3, start_pos.y,
                    start_pos.z, schemas[obj["type"]])

        counter += 1

# }}}
# }}}


mc = minecraft.Minecraft()
pwd = os.getcwd()

# get player's position.
initialPlayerPos = mc.player.getPos()
objstartPos = Vec3(initialPlayerPos.x + 5,
                   initialPlayerPos.y, initialPlayerPos.z)

mc.postToChat(f'pwd: {pwd}')

write_files(objstartPos, ls(pwd))
