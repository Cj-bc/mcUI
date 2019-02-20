import re
import os
import commands
from entry import Pane
from util import direction

class ChatCommand():
    """ Treat chat command from Minecraft
    """
    @staticmethod
    def run_chat_command(mc, session, events, entity_id):
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


    def cat(mc, pathes):
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

    def cd(session, *pathes):
        pass
        return (None, None)

    def cp(session, *pathes):
        pass
        return (None, None)

    def exit(session, *argv):
        """ Exit mcUI process
        """
        session.is_end = True
        return (None, None)

    def help(*path):
        pass
        return (None, None)

    def ls(session, pathes):
        """ execute ls in 'path'

            Args:
                *pathes (list of str): optional. path to execute ls. If empty, pwd will used

            Return:
                new_pane (Pane): new(Updated) Pane
        """
        pane = session.panes[0]
        if len(pathes) != 0:
            regex_abspath = r'^/.*'
            regex_fromhome = r'^~/.*'
            if re.match(regex_abspath, pathes[0]) or re.match(regex_fromhome, pathes[0]):
                new_path = os.path.expanduser(pathes[0])
            else:
                new_path = pane.path + '/' + pathes[0]
        else:
            new_path = pane.path

        return (Pane(path=new_path, entries=commands.ls(new_path),
                    pos=pane.pos, face_to=pane.face_to), True)

    def man(*argv):
        pass
        return (None, None)

    def mv(session, pathes):
        pass
        return (None, None)

    def pwd(mc, session):
        """ Echo pwd to Chat
        """
        mc.postToChat(f'pwd: {session.panes[0].path}')
        return (None, None)

    def rm(*pathes):
        pass
        return (None, None)

    def pane(mc, session, argv):
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
            if argv[1] > len(session.panes):
                return (None, None)

            index = argv[1]
            x = argv[2]
            y = argv[3]
            z = argv[4]
            addition = Vec3(x, y, z)

            pane = session.panes[index]
            return (Pane(path=pane.path, entries=pane.entries,
                         pos=pane.pos + addition, face_to=pane.face_to), False)
        elif argv[0] == "deactiavte":
            if argv[1] > len(session.panes):
                return (None, None)

            pane = session.panes[index]
            return (Pane(path=pane.path, entries=pane.entries,
                         pos=pane.pos, face_to=pane.face_to, active=False))
        elif argv[0] == "activate":
            if argv[1] > len(session.panes):
                return (None, None)

            pane = session.panes[index]
            return (Pane(path=pane.path, entries=pane.entries,
                         pos=pane.pos, face_to=pane.face_to, active=True))
        elif argv[0] == "list":
            mc.postToChat(f'panes: {session.panes}')
            return (None, None)
        else:
            return (None, None)



        return (None, None)

    def reload(*argv):
        pass
        return (None, None)
