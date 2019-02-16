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

# configs(should be in config.py) {{{
margin = 5 # mergin from player position to center of objects' spawing place
padding = Vec3(3, 0, 0) # padding between each objects
line_vec = Vec3(0, 0, 3) # vector to define which axis should objects follow
MAX_OBJECT_PER_LINE = 6 # how much objects could be in one line?
# }}}


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


# direction(rot) {{{2
def direction(rot):
    """ Convert Rotation data (comes from player.getRotation) into direction.

        Args:
            rot (floot): Rotation. Comes from minecraft.Minecraft().player.getRotation()

        Return:
            direction (string): direction of 'rot'. One of north/south/east/west
    """
    if -180.00 <= rot < -135.00:
        return "north"
    elif -135.00 <= rot < -45.00:
        return "east"
    elif -45.00 < rot <= 45.00:
        return "south"
    elif 45.00 <= rot < 135.00:
        return "west"
    elif 135.00 <= rot < 180.00:
        return "north"
    else:
        return ""
# }}}


# write_files(start_pos, files) {{{2
def write_files(start_pos, face_to, files):
    """write "files" file entries to minecraft world
        Number of objects lay in one line is defined as MAX_OBJECT_PER_LINE

        Args:
            start_pos (vec3.Vec3): vec3 object which points the first position to generate
            face_to (string): Direction all objects will face to
            files (list of dict): generated by ls(); list of 'path's entries
        Return:
            no return
    """
    schemas = get_schemas()

    if face_to == "north":
        coordinate_list = [ [padding.x, line_vec.x],
                            [padding.y, line_vec.y],
                            [padding.z, line_vec.z]
                          ]
        current_margin = Vec3(0, 0, -margin)
    elif face_to == "east":
        coordinate_list = [ [padding.z, line_vec.z],
                            [padding.y, line_vec.y],
                            [padding.x, line_vec.x]
                          ]
        current_margin = Vec3(-margin, 0, 0)
    elif face_to == "south":
        coordinate_list = [ [padding.x, line_vec.x],
                            [padding.y, line_vec.y],
                            [padding.z, line_vec.z]
                          ]
        current_margin = Vec3(0, 0, margin)
    elif face_to == "west":
        coordinate_list = [ [padding.z, line_vec.z],
                            [padding.y, line_vec.y],
                            [padding.x, line_vec.x]
                          ]
        current_margin = Vec3(-margin, 0, 0)


    # Divide into few lists that have exactlly the same amount of MAX_OBJECT_PER_LINE object.
    lines = [files[i:i+MAX_OBJECT_PER_LINE]
            for i in range(0,len(files), MAX_OBJECT_PER_LINE)]
    for index_line, a_line in enumerate(lines):
        for index_row, obj in enumerate(a_line):
            # TODO: should i make function?
            # TODO: I'm not sure whether this code works
            mc.setBlock(start_pos.x + current_margin.x + index_row * coordinate_list[0][0]
                                                       + index_line * coordinate_list[0][1],
                        start_pos.y + current_margin.y + index_row * coordinate_list[1][0]
                                                       + index_line * coordinate_list[1][1],
                        start_pos.z + current_margin.z + index_row * coordinate_list[2][0]
                                                       + index_line * coordinate_list[2][1],
                        schemas[obj["type"]])
# }}}
# }}}


mc = minecraft.Minecraft()
pwd = os.getcwd()

spawn_object_criteria = mc.player.getPos()
spawn_object_direction_criteria = direction(mc.player.getRotation())

mc.postToChat(f'pwd: {pwd}')

# TODO: WIP
write_files(spawn_object_criteria, spawn_object_direction_criteria,ls(pwd))
