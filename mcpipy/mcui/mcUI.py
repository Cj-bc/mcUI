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

import mcpi.minecraft as minecraft
from mcpi.vec3 import Vec3
from entry import Pane
from util import *
from commands import ls


mc = minecraft.Minecraft()
pwd = os.getcwd()

spawn_object_criteria = mc.player.getPos()
spawn_object_direction_criteria = direction(mc.player.getRotation())

mc.postToChat(f'pwd: {pwd}')

# TODO: WIP
pane = Pane(entries=ls(pwd), pos=spawn_object_criteria, face_to=spawn_object_direction_criteria)
write_pane(mc, pane)
