#!/usr/bin/env python3
import os
from config import filetype_list
from typing import List
from mcpi.vec3 import Vec3
import mcpi.minecraft as minecraft

def ftdetection(filename: str) -> str:
    """ detect filetype from filename(extention)

        This function is devided so that we can add
        other methods to detect filetype(e.g. detect
        filetype based on file contents)

        Args:
            filename (string): filename

        Return:
            filetype (string):filetype
    """
    _, ext = os.path.splitext(filename)
    ret = filetype_list[ext] if ext in filetype_list else "unknown"
    return ret

class Entry:
    """ file, directory, etc

        Args:
            parent (Entry): parent directory.
            filetype (string): filetype. e.g. "file"/"dir"/"markdown"/"python"
            filename (string): filename.
            permission (int): permission of given entry.
            symlink (bool): True if entry is symbolik link
    """
    # TODO: how to define 'parent'?
    def __init__(self, DirEntry: os.DirEntry) -> None:
        """ Initialize Entry.

            Args:
                DirEntry (os.DirEntry): DirEntry to convert to Entry
        """
        self.nameEntityId = 0
        self.symlink = True if DirEntry.is_symlink() else False
        self.filename = DirEntry.name

        if DirEntry.is_dir():
            self.filetype = "dir"
        elif DirEntry.is_file():
            self.filetype = ftdetection(self.filename)

        self.parent = ""
        self.permission = ""


    def savePos(self, pos: Vec3) -> None:
        """ set entry's position (in Minecraft) to pos.
            This doesn't spawn itself, just saving where they're spawned

            Args:
                pos (Vec3): the position to save
        """
        self.pos = pos


    def getPos(self) -> Vec3:
        """ get entry's position (in Minecraft.)
        """
        return self.pos


    def saveNameEntityId(self, id: int) -> None:
        """ Save armorstand entity(for displaying filename) id

            Args:
                id (int): entitiy id
        """
        self.nameEntityId = id



class Pane:
    """ Pane object that store Entity for one path
        Plese imagine tmux pane

        Args:
            id (int): Pane ID that is unique to all panes
            entries (list of Entry): entries that is sotred in the pane
            pos (Vec3): Vec3 that poits where is the left bottom of this pane.
            face_to (string): direction taht Pane face to. north/south/west/east
            path (string): path of parent directory of entries
            active (bool): Whether this pane will be displayed in Minecraft
    """
    
    def __init__(self, _id: int, path: str, entries: List[Entry], pos: Vec3, face_to: str, active: bool=True) -> None:
        """ Initialize Pane
            
            Args:
                entries (list of Entry): entries that is sotred in the pane
                pos (Vec3): Vec3 that poits where is the left bottom of this pane.
                face_to (string): direction taht Pane face to. north/south/west/east
                path (string): path of parent directory of entries
        """
        self.id = _id
        self.path = path
        self.entries = entries
        self.pos = pos
        self.face_to = face_to
        self.active = active

    def __eq__(self, other):
        return self.id == other.id

    def get_entries(self) -> None:
        """ generator for Entries
        """
        for ent in self.entries:
            yield ent




class Session:
    """ Manage all state of mcUI

        This should be created only once

        Args:
            panes (list of Pane): contains panes
            is_end (bool): False while the session is alive
            gabage (list of Pane): gabage panes(should be removed in next remove_pane)
    """

    def __init__(self) -> None:
        """ Initialize session
        """
        self.panes = []
        self.gabage = []
        self.is_end = False


    def add_pane(self, pane: Pane) -> None:
        """ Add pane 'pane' to session's pane

            Args:
                pane (Pane): pane to add
        """
        self.panes += [pane]

    def update_pane(self, index: int, pane: Pane) -> None:
        """ Update panes['index'] to 'pane'

            Args:
                pane (Pane): pane object to update to
                index (int): index of pane to update
        """
        self.gabage += [self.panes[index]]
        self.panes[index] = pane
