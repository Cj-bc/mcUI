import mcpi.entity as entity
from mcpi.vec3 import Vec3
import mcpi.block as block
from config import margin, padding, line_vec, MAX_OBJECT_PER_LINE, schema


# get_schemas() {{{
def get_schemas():
    """get list of blocks for each filetype

        Args:
            no args
        Return:
            schema (dict): key is "filetype", value is "block"
    """
    return schema
# }}}


# direction(rot) {{{
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


# write_pane(start_pos, files) {{{
def write_pane(mc, pane):
    """write "files" file entries to minecraft world
        Number of objects lay in one line is defined as MAX_OBJECT_PER_LINE

        Args:
            mc (mcpi.minecraft.Minecraft): minecraft object
            pane (Pane): pane object to write
        Return:
            no return
    """
    schemas = schema
    if pane.active != True:
        return

    for entry in pane.entries:
        mc.setBlock(entry.pos.x, entry.pos.y, entry.pos.z, schemas[entry.filetype])
        ent_id = mc.spawnEntity(entity.ARMORSTAND, entry.pos,
                                '{CustomName: ' + entry.filename + \
                                ', CustomNameVisible: true, NoGravity: true, Invisible: true}')
        entry.saveNameEntityId(ent_id)
# }}}


def calc_entries_coordinate(pane, padding, line_vector, line_max):
    """ calculate entries coordinate in Minecraft

        Args:
            pane (Pane): pane that contains entries to calclate coordinate
            padding (vec3.Vec3): Define how many blanks are required around each Entity in Minecraft. config: padding
            line_vector (vec3.Vec3): Define which direction the next line appears. config: line_vec
            line_max (int): Max amount of each line. config: MAX_OBJECT_PER_LINE

        Return:
            list_of_vec (list of vec3.Vec3): list of vec3 values
    """
    # Divide into few lists that have exactlly the same amount of MAX_OBJECT_PER_LINE object.
    lines = [pane.entries[i:i+line_max]
            for i in range(0,len(pane.entries), line_max)]

    if pane.face_to == "north":
        coordinate_list = [ [padding.x, line_vec.x],
                            [padding.y, line_vec.y],
                            [padding.z, line_vec.z]
                          ]
        # TODO: Should be fixed when each object shape is no longer one block.
        #       Current script doesn't consider the size of each object
        oneline_length = (len(lines[0]) -1) * abs(coordinate_list[0][0]) + 1
        adjusted_pos = Vec3(pane.pos.x - int(oneline_length /2), pane.pos.y, pane.pos.z)
        current_margin = Vec3(0, 0, -margin)
    elif pane.face_to == "east":
        coordinate_list = [ [padding.z, line_vec.z],
                            [padding.y, line_vec.y],
                            [padding.x, line_vec.x]
                          ]
        # TODO: Should be fixed when each object shape is no longer one block.
        #       Current script doesn't consider the size of each object
        oneline_length = (len(lines[0]) -1) * abs(coordinate_list[2][0]) + 1
        adjusted_pos = Vec3(pane.pos.x, pane.pos.y, pane.pos.z - int(oneline_length /2))
        current_margin = Vec3(margin, 0, 0)
    elif pane.face_to == "south":
        coordinate_list = [ [-padding.x, line_vec.x],
                            [padding.y, line_vec.y],
                            [-padding.z, line_vec.z]
                          ]
        # TODO: Should be fixed when each object shape is no longer one block.
        #       Current script doesn't consider the size of each object
        oneline_length = (len(lines[0]) -1) * abs(coordinate_list[0][0]) + 1
        adjusted_pos = Vec3(pane.pos.x + int(oneline_length /2), pane.pos.y, pane.pos.z)
        current_margin = Vec3(0, 0, margin)
    elif pane.face_to == "west":
        coordinate_list = [ [-padding.z, line_vec.z],
                            [padding.y, line_vec.y],
                            [-padding.x, line_vec.x]
                          ]
        # TODO: Should be fixed when each object shape is no longer one block.
        #       Current script doesn't consider the size of each object
        oneline_length = (len(lines[0]) -1) * abs(coordinate_list[2][0]) + 1
        adjusted_pos = Vec3(pane.pos.x, pane.pos.y, pane.pos.z + int(oneline_length /2))
        current_margin = Vec3(-margin, 0, 0)


    ret = []
    for index_line, a_line in enumerate(lines):
        for index_row, entry in enumerate(a_line):
            # I think it's not a good idea to apply margin here. But I have no idea other than that for now
            spawn_pos = Vec3(adjusted_pos.x + current_margin.x + index_row * coordinate_list[0][0]
                                                               + index_line * coordinate_list[0][1],
                                adjusted_pos.y + current_margin.y + index_row * coordinate_list[1][0]
                                                               + index_line * coordinate_list[1][1],
                                adjusted_pos.z + current_margin.z + index_row * coordinate_list[2][0]
                                                               + index_line * coordinate_list[2][1] )
            ret.append(spawn_pos)

    return ret


def remove_pane(mc, pane):
    """ Remove 'pane' from Minecraft

        Args:
            mc  (mcpi.minecraft.Minecraft): minecraft object
            pane (Pane): pane to remove
    """

    for ent in pane.get_entries():
        mc.setBlock(ent.pos.x, ent.pos.y, ent.pos.z, block.AIR)
        mc.removeEntity(ent.nameEntityId)


def reload_pane(mc, pane):
    """ Re-construct pane in Minecraft

        Args:
            mc  (mcpi.minecraft.Minecraft): minecraft object
            pane (Pane): pane to reload
    """

    remove_pane(mc, pane)
    write_pane(mc, pane)


# get_abspath(path, base_path){{{
def get_abspath(path, base_path):
    """ Return absolute path of 'path'

        If 'path' is already absolute path, Return 'path' itself
        If 'path' contains '~', expand it and return absolute path

        Args:
            path (str): path to get absolute path
            base_path (str): base path(pwd)

        Returns:
            abspath (str): absolute path for 'path'
    """
    regex_abspath = r'^/.*'
    regex_fromhome = r'^~/.*'
    if re.match(regex_abspath, path) or re.match(regex_fromhome, path):
        return os.path.expanduser(path)
    else:
        return base_path + '/' + path
# }}}
