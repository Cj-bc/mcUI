import mcpi.minecraft as minecraft
import mcpi.block as block
# import mcpi.entity as entity
from mcpi.vec3 import Vec3
import os

def get_pwd_ls():
    """get current directory's entries and return list

       Args:
            no args
       Return:
            pwd_file_list (list of dict): list of current directory's entries.
    """
    ret = []
    with os.scandir(os.getcwd()) as it:
        for f in it:
            if f.is_file():
                ret += [{"type": "file", "name": f.name}]
            elif f.is_dir():
                ret += [{"type": "dir", "name": f.name}]

    return ret


def get_schemas():
    """get list of blocks for each filetype

        Args:
            no args
        Return:
            schema (dict): key is "filetype", value is "block"
    """
    schema = {"file": block.WOOL,
              "dir": block.IRON_BLOCK}
    return schema


def write_pwd_ls(start_pos):
    """write current directory's entries to minecraft world

        Args:
            start_pos (vec3.Vec3): vec3 object which points the first position to generate
        Return:
            no return
    """
    ls = get_pwd_ls()
    schemas = get_schemas()
    counter = 0
    for obj in ls:
        if obj["type"] == "file":
            mc.setBlock(start_pos.x + counter*3, start_pos.y,
                        start_pos.z, schemas["file"])
        elif obj["type"] == "dir":
            mc.setBlock(start_pos.x + counter*3, start_pos.y,
                        start_pos.z, schemas["dir"])

        counter += 1



mc = minecraft.Minecraft()
pwd = os.getcwd()

# get player's position.
initialPlayerPos = mc.player.getPos()
objstartPos = Vec3(initialPlayerPos.x + 5,
                   initialPlayerPos.y, initialPlayerPos.z)

mc.postToChat(f'pwd: {pwd}')

write_pwd_ls(objstartPos)
