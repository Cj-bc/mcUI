import re
import os
import commands

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
                return ChatCommand.cat(words[1:])
            elif words[0] == 'cd':
                return ChatCommand.cd(words[1:])
            elif words[0] == 'cp':
                return ChatCommand.cp(words[1:])
            elif words[0] == 'exit':
                return ChatCommand.exit(words[1:])
            elif words[0] == 'help':
                return ChatCommand.help(words[1:])
            elif words[0] == 'ls':
                return ChatCommand.ls(session, words[1:])
            elif words[0] == 'man':
                return ChatCommand.man(words[1:])
            elif words[0] == 'mv':
                return ChatCommand.mv(words[1:])
            elif words[0] == 'pwd':
                return ChatCommand.pwd()
            elif words[0] == 'rm':
                return ChatCommand.rm(words[1:])
            # ^ UNIX commands; v mcUI commands
            elif words[0] == 'create':
                return ChatCommand.create(words[1:])
            elif words[0] == 'reload':
                return ChatCommand.reload(words[1:])


    def cat(mc, *pathes):
        """ Catinate 'path' files to Chat

            Args:
                *pathes (list of str): required at least 1. Path to the file to cat
        """
        for path in pathes:
            if not os.path.isfile(path):
                continue
            with open(path,'r') as f:
                mc.player.postToChat(f.read())

    def cd(session, *pathes):
        pass
        return (None, None)

    def cp(session, *pathes):
        pass
        return (None, None)

    def exit(session):
        """
        """
        session.is_end = True
        return (None, None)

    def help(*path):
        pass
        return (None, None)

    def ls(session, pathes):
        """ execute ls in 'path'

            Args:
                *path (list of str): optional. path to execute ls. If empty, pwd will used

            Return:
                new_pane (Pane): new(Updated) Pane
        """
        pane = session.panes[0]
        new_path = pane.path + path[0]
        return (Pane(path=new_path, entries=commands.ls(nwe_path),
                    pos=pane.pos, face_to=pane.face_to), is_new)
    def man(*argv):
        pass
        return (None, None)

    def mv(*pathes):
        pass
        return (None, None)

    def pwd(self):
        pass
        return (None, None)

    def rm(*pathes):
        pass
        return (None, None)

    def create(*argv):
        pass
        return (None, None)

    def reload(*argv):
        pass
        return (None, None)
