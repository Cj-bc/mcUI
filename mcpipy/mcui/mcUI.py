#!/usr/bin/env python3
#
# mcUI --- minecraft based 3D UI for *nix
#
# copyright (c) 2019 Cj-bc a.k.a Cj.bc_sd
#
# (@) version: 0.2.0
# (@) usage:
# (@)   run this script while Minecraft is running.

import os
import time

import mcpi.minecraft as minecraft
from mcpi.vec3 import Vec3
from entry import Pane
from util import *
from commands import ls
from config import margin, padding, line_vec, MAX_OBJECT_PER_LINE
from entry import Session


# Initialize
mc = minecraft.Minecraft()
pwd = os.getcwd()
spawn_object_criteria = mc.player.getPos()
player_allowed_use_command = mc.getPlayerEntityIds()
spawn_object_direction_criteria = direction(mc.player.getRotation())

mc.postToChat(f'pwd: {pwd}')

the_session = Session()
the_session.add_pane(Pane(path=pwd, entries=ls(pwd), pos=spawn_object_criteria, face_to=spawn_object_direction_criteria))

while not the_session.is_end:
    for entry, pos in zip(the_session.panes[0].entries,
                          calc_entries_coordinate(the_session.panes[0], padding, line_vec, MAX_OBJECT_PER_LINE)):
        entry.savePos(pos)

    for pane in the_session.panes:
        write_pane(mc, pane)


    time.sleep(1)

mc.postToChat('removing mcUI...')
for pane in the_session.panes:
    remove_pane(mc, pane)

mc.postToChat('Done.')
