import mcpi.entity as entity
from mcpi.vec3 import Vec3
from config import margin, padding, line_vec, MAX_OBJECT_PER_LINE, schema


# functions {{{
# get_schemas() {{{2
def get_schemas():
    """get list of blocks for each filetype

        Args:
            no args
        Return:
            schema (dict): key is "filetype", value is "block"
    """
    return schema
# }}}


# direction(rot) {{{2
def direction(rot):
    """ Convert Rotation data (comes from player.getRotation) into Player's direction.

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
    schemas = schema

    # Divide into few lists that have exactlly the same amount of MAX_OBJECT_PER_LINE object.
    lines = [files[i:i+MAX_OBJECT_PER_LINE]
            for i in range(0,len(files), MAX_OBJECT_PER_LINE)]

    if face_to == "north":
        coordinate_list = [ [padding.x, line_vec.x],
                            [padding.y, line_vec.y],
                            [padding.z, line_vec.z]
                          ]
        # TODO: Should be fixed when each object shape is no longer one block.
        #       Current script doesn't consider the size of each object
        oneline_length = (len(lines[0]) -1) * abs(coordinate_list[0][0]) + 1
        adjusted_pos = Vec3(start_pos.x - int(oneline_length /2), start_pos.y, start_pos.z)
        current_margin = Vec3(0, 0, -margin)
    elif face_to == "east":
        coordinate_list = [ [padding.z, line_vec.z],
                            [padding.y, line_vec.y],
                            [padding.x, line_vec.x]
                          ]
        # TODO: Should be fixed when each object shape is no longer one block.
        #       Current script doesn't consider the size of each object
        oneline_length = (len(lines[0]) -1) * abs(coordinate_list[2][0]) + 1
        adjusted_pos = Vec3(start_pos.x, start_pos.y, start_pos.z - int(oneline_length /2))
        current_margin = Vec3(margin, 0, 0)
    elif face_to == "south":
        coordinate_list = [ [-padding.x, line_vec.x],
                            [padding.y, line_vec.y],
                            [-padding.z, line_vec.z]
                          ]
        # TODO: Should be fixed when each object shape is no longer one block.
        #       Current script doesn't consider the size of each object
        oneline_length = (len(lines[0]) -1) * abs(coordinate_list[0][0]) + 1
        adjusted_pos = Vec3(start_pos.x + int(oneline_length /2), start_pos.y, start_pos.z)
        current_margin = Vec3(0, 0, margin)
    elif face_to == "west":
        coordinate_list = [ [-padding.z, line_vec.z],
                            [padding.y, line_vec.y],
                            [-padding.x, line_vec.x]
                          ]
        # TODO: Should be fixed when each object shape is no longer one block.
        #       Current script doesn't consider the size of each object
        oneline_length = (len(lines[0]) -1) * abs(coordinate_list[2][0]) + 1
        adjusted_pos = Vec3(start_pos.x, start_pos.y, start_pos.z + int(oneline_length /2))
        current_margin = Vec3(-margin, 0, 0)


    for index_line, a_line in enumerate(lines):
        for index_row, entry in enumerate(a_line):
            # I think it's not a good idea to apply margin here. But I have no idea other than that for now
            spawn_pos = Vec3(adjusted_pos.x + current_margin.x + index_row * coordinate_list[0][0]
                                                               + index_line * coordinate_list[0][1],
                                adjusted_pos.y + current_margin.y + index_row * coordinate_list[1][0]
                                                               + index_line * coordinate_list[1][1],
                                adjusted_pos.z + current_margin.z + index_row * coordinate_list[2][0]
                                                               + index_line * coordinate_list[2][1] )
            mc.setBlock(spawn_pos.x, spawn_pos.y, spawn_pos.z, schemas[entry.filetype])
            ent_id = mc.spawnEntity(entity.ARMORSTAND, spawn_pos,
                                    '{CustomName: ' + entry.filename + \
                                    ', CustomNameVisible: true, NoGravity: true, Invisible: true}')
            entry.savePos(spawn_pos)
            entry.saveNameEntityId(ent_id)
# }}}


# }}}


