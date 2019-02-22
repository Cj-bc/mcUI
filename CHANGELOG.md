# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

# [version] - YYYY/MM/DD

# 0.3.0 - 2019/02/21
## Added
	* chat_event.py -- contains ChatCommand class
	* util.py -- contains utlity functions
	* command.py -- contains functions related to shell
	* Make main loop so that we can continue program
	* remove_pane()  -- Remove pane from Minecraft
	* reload_pane()  -- reload pane state
	* calc_entries_coordinate()  -- calculate coordinate of Entry
	* get_abspath()  -- Get absolute path [WIP]
	* 'Pane' class to store 'Entry's in entry.py
	* 'Session' class to store 'Pane's and mcUI state; in entry.py
	* 'Entry.nameEntityId' to store armor_stand entity id which displays filename
	* 'ChatCommand' class that have functions for each chat command
		* ChatCommand.ls() -- Execute 'ls' and returns new pane of given path
		* ChatCommand.cat() -- catinate 'path' file to Chat
		* ChatCommand.cd() -- Execute 'cd' for pane 0
		* ChatCommand.exit() -- Exit mcUI. Remove all blocks/entites made by mcUI
		* ChatCommand.ls() -- Make new pane for 'path'
		* ChatCommand.pwd() -- Echo pwd to Chat
		* ChatCommand.pane() -- manage pane objects. please refer to comments for subcommands
	* Docs  -- `current progress` section

## Changed
	* Use 'Pane' to store&manage 'Entry'es
	* Use 'Session' to store&manage 'Pane's
	* Move exist functions into util.py/command.py
	* write_file() -> write_pane()
	* Don't draw pane if Pane.active is False
	* Use 'type hints' to write functions

# 0.2.0 - 2019/02/18
## Added
	* Display filename using invisible armor_stand
	* Detect file type from extention
	* Use different block for each filetype
	* Customizable schema in config.py
	* 'Entry' class for storing what entry is displayed

## Changed
	* Move all related files(including mcpi dir) into mcui directory
	* ls() returns list of 'Entry' objects
	* move config values into mcui/config.py
		* margin, padding, line_vec, MAX_OBJECT_PER_LINE
		* filetype_list
		* schema


# 0.1.0 - 2019/02/17
## Added
	* Spawn objects in front of user
	* Adjust coordinate of objects so that user stands at the center of objects line
	* File: 2mcUI.py   --- mcUI wrapper for python2

# 0.0.2 - 2019/02/14
## Changed
	* Improve code quality


# 0.0.1 - 2019/02/14
## Added
	* set blocks in Minecraft based on pwd's files
	* blocks are placed in one way, parallel to axis x
	* directories are IRON_BLOCK
	* files are WOOL

------
vim: ft=changelog
