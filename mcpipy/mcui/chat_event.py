import re
import os
from typing import Tuple, List

import commands
from entry import Pane, Session
from util import direction, get_abspath
from mcpi.vec3 import Vec3
import mcpi.minecraft as minecraft
from mcpi.event import ChatEvent

class ChatCommand():
    """ Treat chat command from Minecraft
    """
    @staticmethod
    def run_chat_command(mc: minecraft.Minecraft, session: Session, events: List[ChatEvent], entity_id: int) -> tuple:
        """ Run detected chat command from list 'events', spoken by 'entity_id'

            Args:
                session (Session): session for this time
                events (list of event): list of events
                entity_id (list of int): entity id to recognize as command
        """
        for text in [e.message for e in events if e.entityId in entity_id]:
            words = text.split(" ")

            if words[0] == 'cat':
                return ChatCommand.cat(mc, words[1:])
            elif words[0] == 'cd':
                return ChatCommand.cd(session, words[1:])
            elif words[0] == 'cp':
                return ChatCommand.cp(session, words[1:])
            elif words[0] == 'exit':
                return ChatCommand.exit(session, words[1:])
            elif words[0] == 'help':
                return ChatCommand.help(words[1:])
            elif words[0] == 'ls':
                return ChatCommand.ls(session, words[1:])
            elif words[0] == 'man':
                return ChatCommand.man(words[1:])
            elif words[0] == 'mv':
                return ChatCommand.mv(session, words[1:])
            elif words[0] == 'pwd':
                return ChatCommand.pwd(mc, session)
            elif words[0] == 'rm':
                return ChatCommand.rm(words[1:])
            # ^ UNIX commands; v mcUI commands
            elif words[0] == 'pane':
                return ChatCommand.pane(mc, session, words[1:])
            elif words[0] == 'reload':
                return ChatCommand.reload(words[1:])
            else:
                return (None, None)


    def cat(mc: minecraft.Minecraft, pathes: List[str]) -> Tuple[Pane, bool]:
        """ Catinate 'path' files to Chat

            Args:
                pathes (list of str): required at least 1. Path to the file to cat
        """
        for path in pathes:
            if not os.path.isfile(path):
                continue
            with open(path,'r') as f:
                mc.postToChat(f.read())

        return (None, None)

    def cd(session: Session, pathes: List[str]) -> Tuple[Pane, bool]:
        """ execute 'cd' and chnage current dir
        """
        pane = session.panes[0] # TODO: shoulb be changed to support multi pane
        new_path = get_abspath(pathes[0], pane.path) if len(pathes) != 0 else pane.path

        return (Pane(path=new_path, entries=commands.ls(new_path),
                    pos=pane.pos, face_to=pane.face_to), False)


    def cp(session: Session, pathes: List[str]) -> Tuple[Pane, bool]:
        pass
        return (None, None)

    def exit(session: Session, argv: List[str]) -> Tuple[Pane, bool]:
        """ Exit mcUI process
        """
        session.is_end = True
        return (None, None)

    def help(path: List[str]) -> Tuple[Pane, bool]:
        pass
        return (None, None)

    def ls(session: Session, pathes: List[str]) -> Tuple[Pane, bool]:
        """ execute ls in 'path'

            Args:
                *pathes (list of str): optional. path to execute ls. If empty, pwd will used

            Return:
                new_pane (Pane): new(Updated) Pane
        """
        pane = session.panes[0]
        new_path = get_abspath(pathes[0], pane.path) if len(pathes) != 0 else pane.path

        return (Pane(path=new_path, entries=commands.ls(new_path),
                    pos=pane.pos, face_to=pane.face_to), True)

    def man(argv: List[str]) -> Tuple[Pane, bool]:
        pass
        return (None, None)

    def mv(session: Session, pathes: List[str]) -> Tuple[Pane, bool]:
        pass
        return (None, None)

    def pwd(mc: minecraft.Minecraft, session: Session) -> Tuple[Pane, bool]:
        """ Echo pwd to Chat
        """
        mc.postToChat(f'pwd: {session.panes[0].path}')
        return (None, None)

    def rm(pathes: List[str]) -> Tuple[Pane, bool]:
        pass
        return (None, None)

    def pane(mc: minecraft.Minecraft, session: Session, argv: List[str]) -> Tuple[Pane, bool]:
        """ Manage panes

            This command has subcommands:
                create <path>  -- create new pane with <path>
                move <pane_num> <x> <y> <z>  --- Add Vec3(x,y,z) to pane's coordinate
                deactivate <pane_num>  --- deactivate pane <pane_num> from Minecraft
                active <pane_num> --- activate pane <pane_num> in Minecraft
                list --- return list of panes
        """
        if argv[0] == "create":
            if not os.path.isdir(argv[1]):
                return (None, None)

            return (Pane(path=argv[1], entries=commands.ls(argv[1]),
                         pos=mc.player.getPos(), face_to=direction(mc.player.getRotate())), True)
        elif argv[0] == "move":
            if int(argv[1]) > len(session.panes):
                return (None, None)

            index = int(argv[1])
            x = int(argv[2])
            y = int(argv[3])
            z = int(argv[4])
            addition = Vec3(x, y, z)

            pane = session.panes[index]
            return (Pane(path=pane.path, entries=pane.entries,
                         pos=pane.pos + addition, face_to=pane.face_to), False)
        elif argv[0] == "deactivate":
            if int(argv[1]) > len(session.panes):
                return (None, None)

            index = int(argv[1])
            pane = session.panes[index]
            return (Pane(path=pane.path, entries=pane.entries,
                         pos=pane.pos, face_to=pane.face_to, active=False), False)
        elif argv[0] == "activate":
            if int(argv[1]) > len(session.panes):
                return (None, None)

            index = int(argv[1])
            pane = session.panes[index]
            return (Pane(path=pane.path, entries=pane.entries,
                         pos=pane.pos, face_to=pane.face_to, active=True), False)
        elif argv[0] == "list":
            for i, pane in  enumerate(session.panes):
                active = "Active" if pane.active else "Inactive"
                mc.postToChat(f'pane[{i}]  || path: {pane.path}  || {active}')

            return (None, None)
        else:
            return (None, None)



        return (None, None)

    def reload(argv: List[str]) -> Tuple[Pane, bool]:
        pass
        return (None, None)
