# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

# [version] - YYYY/MM/DD

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
