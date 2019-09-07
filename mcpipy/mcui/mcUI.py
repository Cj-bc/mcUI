#!/usr/bin/env python3
#
# mcUI --- minecraft based 3D UI for *nix
#
# copyright (c) 2019 Cj-bc a.k.a Cj.bc_sd
#
# (@) version: 0.3.2
# (@) usage:
# (@)   run this script while Minecraft is running.

import os
import time

import mcpi.minecraft as minecraft
from mcpi.vec3 import Vec3
from entry import Pane
from util import *
from commands import ls
from chat_event import ChatCommand
from config import margin, padding, line_vec, MAX_OBJECT_PER_LINE
from entry import Session
from Render import Renderer


# Initialize
mc = minecraft.Minecraft()
pwd = os.getcwd()
spawn_object_criteria = mc.player.getPos()
player_allowed_use_command = mc.getPlayerEntityIds()
spawn_object_direction_criteria = direction(mc.player.getRotation())

mc.postToChat(f'pwd: {pwd}')

the_session = Session()
the_session.add_pane(Pane(path=pwd, entries=ls(pwd), pos=spawn_object_criteria, face_to=spawn_object_direction_criteria))

renderer = Renderer(mc, the_session)


while not the_session.is_end:
    # Update Minecraft condition
    renderer.render()

    # Those codes below should be moved to Renderer.render
    #
    # for pane in the_session.gabage:
    #     remove_pane(mc, pane)

    # for pane in the_session.panes:
    #     for entry, pos in zip(pane.entries,
    #                           calc_entries_coordinate(pane, padding, line_vec, MAX_OBJECT_PER_LINE)):
    #         entry.savePos(pos)

    #     reload_pane(mc, pane)


    # Wait 'till user input
    user_input = []
    while user_input == []:
        user_input = mc.events.pollChatPosts()
        time.sleep(1)

    ret_pane, is_new, pane_id = ChatCommand.run_chat_command(mc, the_session, user_input, player_allowed_use_command)
    if ret_pane is not None:
        if is_new:
            the_session.add_pane(ret_pane)
        elif not is_new:
            the_session.update_pane(pane_id, ret_pane)


mc.postToChat('removing mcUI...')
for pane in the_session.panes:
    remove_pane(mc, pane)

mc.postToChat('Done.')
