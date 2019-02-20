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
            words = list(filter(lambda x: x != ' ',re.findall(r'([^ ]*])', text)))

            if words[0] == 'cat':
                self.cat(words[1:])
            elif words[0] == 'cd':
                self.cd(words[1:])
            elif words[0] == 'cp':
                self.cp(words[1:])
            elif words[0] == 'exit':
                self.exit(words[1:])
            elif words[0] == 'help':
                self.help(words[1:])
            elif words[0] == 'ls':
                self.ls(words[1:])
            elif words[0] == 'man':
                self.man(words[1:])
            elif words[0] == 'mv':
                self.mv(words[1:])
            elif words[0] == 'pwd':
                self.pwd()
            elif words[0] == 'rm':
                self.rm(words[1:])
            # ^ UNIX commands; v mcUI commands
            elif words[0] == 'create':
                self.create(words[1:])
            elif words[0] == 'reload':
                self.reload(words[1:])


    def cat(mc, *path):
        """ Catinate 'path' files to Chat

            Args:
                *path (list of str): required at least 1. Path to the file to cat
        """
        for path in *path:
            continue if not os.path.isfile(path)
            with open(path,'r') as f:
                mc.player.postToChat(f.read())


    def ls(session, *path, is_new=False):
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


    def exit(session):
        """
        """
        session.is_end = True

