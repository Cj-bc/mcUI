#!/usr/bin/env python3
class Entry:
    """ file, directory, etc

        Args:
            parent (Entry): parent directory.
            type (string): filetype. e.g. "file"/"dir"/"markdown"/"python"
            name (string): filename.
            permission (int): permission of given entry.
    """
    # TODO: how to define 'parent'?
    def __init__(self, parent, _type="file", name="temp", permission=755):
        self.parent = parent
        self.type = _type
        self.name = name
        self.permission = permission

    def savePos(self, pos):
        """ set entry's position (in Minecraft) to pos.
            This doesn't spawn itself, just saving where they're spawned

            Args:
                pos (Vec3): the position to save
        """
        self.pos = pos

    def getPos(self):
        """ get entry's position (in Minecraft.)
        """
        return self.pos


