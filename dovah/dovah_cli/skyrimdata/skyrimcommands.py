skyrim_commands = {
# 	0:{'BASE': 'animcam', 'PARAMS': None, 'DETAILS': 'Toggle animator camera'},
# 	1:{'BASE': 'psb', 'PARAMS': None, 'DETAILS': 'Player Spell Book'},
# 	2:{'BASE': 's1st', 'PARAMS': None, 'DETAILS': 'Shows 1st person model in 3rd person'},
# 	3:{'BASE': 'sucsm ', 'PARAMS': ['<number>'], 'DETAILS': 'Changes the speed of the free-flying camera (UFO cam)'},
# 	4:{'BASE': 'tai', 'PARAMS': None, 'DETAILS': 'Toggle AI'},
# 	5:{'BASE': 'tb', 'PARAMS': None, 'DETAILS': 'Toggle Borders'},
# 	6:{'BASE': 'tc', 'PARAMS': None, 'DETAILS': 'Toggle controls driven'},
# 	7:{'BASE': 'tcai', 'PARAMS': None, 'DETAILS': 'Toggle Combat AI'},
# 	8:{'BASE': 'tcl', 'PARAMS': None, 'DETAILS': 'Toggle collision (clipping, noclip)'},
# 	9:{'BASE': 'tdetect', 'PARAMS': None, 'DETAILS': 'Toggle AI Detection'},
# 	10:{'BASE': 'teofis', 'PARAMS': None, 'DETAILS': 'Toggle End-Of-Frame ImageSpace'},
# 	11:{'BASE': 'tfc ', 'PARAMS': ['<1>'], 'DETAILS': 'Freeflying camera'},
# 	12:{'BASE': 'tfow', 'PARAMS': None, 'DETAILS': 'Toggle Fog of War'},
# 	13:{'BASE': 'tg', 'PARAMS': None, 'DETAILS': 'Toggle grass'},
# 	14:{'BASE': 'tgm', 'PARAMS': None, 'DETAILS': 'Toggle god mode'},
# 	15:{'BASE': 'tim', 'PARAMS': None, 'DETAILS': 'Toggle immortal mode'},
# 	16:{'BASE': 'tll', 'PARAMS': None, 'DETAILS': 'Toggle LOD'},
# 	17:{'BASE': 'tm', 'PARAMS': None, 'DETAILS': 'Toggle menus (HUD)'},
# 	18:{'BASE': 'tmm ', 'PARAMS': ['<show?>(,', '<discovered?>,', '<includehidden?>)'], 'DETAILS': 'Show/hide all map markers'},
# 	19:{'BASE': 'ts', 'PARAMS': None, 'DETAILS': 'Toggle sky'},
# 	20:{'BASE': 'tscr', 'PARAMS': None, 'DETAILS': 'Toggle script processing.'},
# 	21:{'BASE': 'tt', 'PARAMS': None, 'DETAILS': 'Toggle trees'},
# 	22:{'BASE': 'twf', 'PARAMS': None, 'DETAILS': 'Toggle wireframe'},
# 	23:{'BASE': 'tws', 'PARAMS': None, 'DETAILS': 'Toggle water system'},
	
# 	24:{'BASE': 'additem ', 'PARAMS': ['<item ID> ', '<count> ', '<flag (optional)>'], 'DETAILS': 'Give a character the specified amount of an item'},
# 	25:{'BASE': 'addperk ', 'PARAMS': ['<perk ID>'], 'DETAILS': 'Give a character the selected perk'},
	27:{'BASE': 'addfac/addtofaction ', 'PARAMS': ['<faction ID> ', '<faction rank>'], 'DETAILS': 'Add a character to a faction.'},
	28:{'BASE': 'advlevel', 'PARAMS': None, 'DETAILS': "Advance a character's level by one."},
	29:{'BASE': 'AdvSkill ', 'PARAMS': ['<skill> ', '<nn>'], 'DETAILS': 'Advance the specified skill.'},
	26:{'BASE': 'addspell ', 'PARAMS': ['<spell ID>'], 'DETAILS': "Add a specific spell to a character's available arsenal."},
	30:{'BASE': 'completequest ', 'PARAMS': ['<quest ID>'], 'DETAILS': 'Complete the quest instantly.'},
	31:{'BASE': 'DamageActorValue ', 'PARAMS': ['<attribute> ', '<nn>'], 'DETAILS': 'Damage value of attribute by <nn> amount'},
	32:{'BASE': 'disable', 'PARAMS': None, 'DETAILS': "Don't render the selected object (includes actors.)"},
	33:{'BASE': 'dispelallspells', 'PARAMS': None, 'DETAILS': 'Dispel all temporary spell effects on target'},
	34:{'BASE': 'drop', 'PARAMS': None, 'DETAILS': "Force drop items from a character's inventory"},
	35:{'BASE': 'duplicateallitems ', 'PARAMS': ['<target>'], 'DETAILS': 'Duplicate all items in the targeted container and places them in the given container.'},
	36:{'BASE': 'enable', 'PARAMS': None, 'DETAILS': 'Render the selected object (includes actors.)'},
	37:{'BASE': 'equipitem ', 'PARAMS': ['<Item baseID> ', '<0/1> ', '<left/right>'], 'DETAILS': 'Equip selected NPC with Item'},
	38:{'BASE': 'equipspell ', 'PARAMS': ['<Spell ID> ', '<Casting Sources>'], 'DETAILS': 'Equipping the given spell on a particular casting source.'},
	39:{'BASE': 'equipshout ', 'PARAMS': ['<Shout ID>'], 'DETAILS': 'Equipping the given shout.'},
	40:{'BASE': 'forceAV ', 'PARAMS': ['<attribute> ', '<nn>'], 'DETAILS': 'Force to modify the value of attribute'},
	41:{'BASE': 'getAV ', 'PARAMS': ['<attribute>'], 'DETAILS': 'Get value of attribute'},
	#42:{'BASE': 'getAVinfo ', 'PARAMS': ['<attribute>'], 'DETAILS': 'Get value information of attribute'},
	#43:{'BASE': 'getlevel ', 'PARAMS': ['<target>'], 'DETAILS': 'Get level of target'},
	#44:{'BASE': 'GetLocationCleared ', 'PARAMS': ['<locationID>'], 'DETAILS': "Check an area's clear code."},
	#45:{'BASE': 'getrelationshiprank ', 'PARAMS': ['<target>'], 'DETAILS': 'Get the relationship rank of two actors.'},
	#46:{'BASE': 'getstage ', 'PARAMS': ['<quest ID>'], 'DETAILS': 'Show the current active quest stage.'},
	#47:{'BASE': 'hasperk ', 'PARAMS': ['<perk ID>'], 'DETAILS': 'Check if the selected actor has a perk with the selected ID'},
	#48:{'BASE': 'incPCS ', 'PARAMS': ['<skill name>'], 'DETAILS': 'Increase the given skill to the next level.'},
	#49:{'BASE': 'kill ', 'PARAMS': ['<Actor ID (optional)>'], 'DETAILS': 'Kill the selected actor (NOT the optional Actor ID).'},
	#50:{'BASE': 'lock ', 'PARAMS': ['<level>'], 'DETAILS': 'Lock targeted object (i.e. door, container) with a difficulty of <level>.'},
	#51:{'BASE': 'MarkForDelete', 'PARAMS': None, 'DETAILS': 'Delete an object.'},
	#52:{'BASE': 'modAV ', 'PARAMS': ['<attribute> ', '<nn>'], 'DETAILS': 'Modify value of attribute by <nn> amount'},
	#53:{'BASE': 'moveto ', 'PARAMS': ['<actor ID>'], 'DETAILS': 'Move a character to specified actor and vice versa.'},
	#54:{'BASE': 'movetoqt ', 'PARAMS': ['<quest ID>'], 'DETAILS': 'Move to quest target'},
	#55:{'BASE': 'openactorcontainer 1', 'PARAMS': None, 'DETAILS': "Open a character's inventory."},
	#56:{'BASE': 'paycrimegold (', 'PARAMS': ['<jail?> ', '<confiscate?> ', '<faction ID>)'], 'DETAILS': 'Pay the bounty.'},
	57:{'BASE': 'placeatme ', 'PARAMS': ['<actor/object ID>'], 'DETAILS': 'Spawn specified actor or object at current position.'},
	58:{'BASE': 'playidle ', 'PARAMS': ['<idle ID>'], 'DETAILS': 'Play an animation (idle) on the specified actor.'},
	59:{'BASE': 'pushactoraway ', 'PARAMS': ['<actor ID> ', '<number>'], 'DETAILS': 'Push an actor away in a random direction.'},
	60:{'BASE': 'recycleactor ', 'PARAMS': ['<destination reference (optional)>'], 'DETAILS': 'Revive/Reset targeted NPC or object.'},
	61:{'BASE': 'removeallitems ', 'PARAMS': ['<actor or container ID>'], 'DETAILS': "Remove all items from a character's inventory."},
	#62:{'BASE': 'removeitem ', 'PARAMS': ['<item ID> ', '<count>'], 'DETAILS': "Remove the specified amount of an item from a character's inventory."},
	#63:{'BASE': 'removeperk ', 'PARAMS': ['<perk ID>'], 'DETAILS': "Remove the specified perk from a character's skills."},
	#64:{'BASE': 'removespell ', 'PARAMS': ['<spell ID>'], 'DETAILS': "Removes a specific spell from a character's spell book. Also works with powers, abilities, blessings, and diseases, but not shouts"},
	#65:{'BASE': 'resetAI', 'PARAMS': None, 'DETAILS': "Reset an NPC's AI."},
	#66:{'BASE': 'resethealth', 'PARAMS': None, 'DETAILS': 'Restore a character to full health.'},
	#67:{'BASE': 'resetinventory', 'PARAMS': None, 'DETAILS': "Reset a container or a character's inventory."},
	#68:{'BASE': 'RestoreActorValue ', 'PARAMS': ['<attribute> ', '<nn>'], 'DETAILS': 'Restore the value of attribute by <nn> amount'},
	#69:{'BASE': 'resurrect ', 'PARAMS': ['<1>'], 'DETAILS': 'Resurrect target actor'},
	70:{'BASE': 'say ', 'PARAMS': ['<dialog topic ID>'], 'DETAILS': 'Makes the targeted actor say a specific dialog topic.'},
	#71:{'BASE': 'setactoralpha ', 'PARAMS': ['<0-100>'], 'DETAILS': "Change the selected actor's alpha/opacity."},
	#72:{'BASE': 'setAV ', 'PARAMS': ['<attribute> ', '<nn>'], 'DETAILS': 'Set value of attribute'},
	73:{'BASE': 'setessential ', 'PARAMS': ['<base ID> ', '<0 or 1>'], 'DETAILS': 'Set a character as mortal (0) or immortal (1).'},
	#74:{'BASE': 'setghost ', 'PARAMS': ['<0 or 1>'], 'DETAILS': 'Set ghost mode for the targeted NPC.'},
	#75:{'BASE': 'setgs ', 'PARAMS': ['<setting> ', '<value>'], 'DETAILS': 'Set game setting.'},
	#76:{'BASE': 'setlevel ', 'PARAMS': ['<multiplier> ', '<modifier> ', '<min> ', '<max>'], 'DETAILS': 'Set NPC level'},
	77:{'BASE': 'SetLocationCleared ', 'PARAMS': ['<locationID> 1'], 'DETAILS': 'Set whether an area has been cleared.'},
	78:{'BASE': 'setnpcweight ', 'PARAMS': ['<0-100>\n(snpcw)'], 'DETAILS': 'Set the weight of the selected NPC and updates the model to reflect the new weight.'},
	79:{'BASE': 'setownership ', 'PARAMS': ['<ID>'], 'DETAILS': 'Sets ownership of the targeted item.'},
	80:{'BASE': 'setrace ', 'PARAMS': ['<race>'], 'DETAILS': "Change a character's race."},
	#81:{'BASE': 'setrelationshiprank ', 'PARAMS': ['<target> ', '<#>'], 'DETAILS': 'Change the relationship between two actors'},
	#82:{'BASE': 'setscale ', 'PARAMS': ['<#>'], 'DETAILS': 'Scale size of target.'},
	#83:{'BASE': 'setstage ', 'PARAMS': ['<quest ID> ', '<stage #>'], 'DETAILS': 'Set the current stage of the given quest.'},
	#84:{'BASE': 'setunconscious ', 'PARAMS': ['<integer>'], 'DETAILS': 'A value of 1 will be unconscious'},
	#85:{'BASE': 'inv/showinventory', 'PARAMS': None, 'DETAILS': "Display the base IDs of every item in a character's inventory."},
	#86:{'BASE': 'shp ', 'PARAMS': ['<parameter #1-parameter #9>'], 'DETAILS': 'Set HDR parameters'},
	#87:{'BASE': 'sifh ', 'PARAMS': ['<#>'], 'DETAILS': 'Set whether an actor should ignore friendly hits.'},
	#88:{'BASE': 'sqs ', 'PARAMS': ['<quest ID>'], 'DETAILS': 'Display stages of a quest'},
	#89:{'BASE': 'stopcombat', 'PARAMS': None, 'DETAILS': 'Stop combat with a targetted NPC'},
	#90:{'BASE': 'str ', 'PARAMS': ['<0-1.000000>'], 'DETAILS': 'Set the refraction value of the selected target.'},
	91:{'BASE': 'teachword ', 'PARAMS': ['<word>'], 'DETAILS': 'Teach a dragon shout.'},
	92:{'BASE': 'unequipitem ', 'PARAMS': ['<Item baseID>'], 'DETAILS': 'Unequip item from selected NPC'},
	# 93:{'BASE': 'unlock', 'PARAMS': None, 'DETAILS': 'Unlock the targeted object.'},
	# 94:{'BASE': 'unlockword ', 'PARAMS': ['<word>'], 'DETAILS': 'Unlock a dragon shout.'},
	# 95:{'BASE': 'bat', 'PARAMS': None, 'DETAILS': 'Execute a batch file'},
	# 96:{'BASE': 'caqs', 'PARAMS': None, 'DETAILS': 'Complete all quest stages'},
	# 97:{'BASE': 'coc', 'PARAMS': None, 'DETAILS': 'Transport to <cellname>'},
	# 98:{'BASE': 'cow', 'PARAMS': None, 'DETAILS': 'Transports to cell <cell x, cell y> in <worldspace>'},
	# 99:{'BASE': 'csb', 'PARAMS': None, 'DETAILS': 'Clear screen blood'},
	# 100:{'BASE': 'fov', 'PARAMS': None, 'DETAILS': 'Set fov <angle>'},
	# 101:{'BASE': 'fw', 'PARAMS': None, 'DETAILS': 'Force Weather'},
	# 102:{'BASE': 'GetGlobalValue ', 'PARAMS': ['<Variable>'], 'DETAILS': 'Returns the value of a single global game setting.'},
	# 103:{'BASE': 'GetInCellParam ', 'PARAMS': ['<Cell ID> ', '<Object ID>'], 'DETAILS': 'Checks if an object is in a specified cell.'},
	# 104:{'BASE': 'GetPCMiscStat ', 'PARAMS': ['<Stat>'], 'DETAILS': 'Returns the value of the (typically meaningless) stats shown in the ESC menu.'},
	# 105:{'BASE': 'help', 'PARAMS': None, 'DETAILS': 'Returns the IDs of all items, spells, game settings, etc. which have the entered text in their name.'},
	# 106:{'BASE': 'killallactors', 'PARAMS': None, 'DETAILS': 'Kill all actors.'},
	# 107:{'BASE': 'load', 'PARAMS': None, 'DETAILS': 'Loads <name> gamesave.'},
	# 108:{'BASE': 'ModPCMiscStat ', 'PARAMS': ['<Stat> ', '<nn>'], 'DETAILS': 'Adjusts the value of the (typically meaningless) stats shown in the ESC menu by <nn> amount.'},
	# 109:{'BASE': 'pcb', 'PARAMS': None, 'DETAILS': 'Purge cell buffer'},
	# 110:{'BASE': 'prid ', 'PARAMS': ['<RefID>'], 'DETAILS': 'Pick reference by ID'},
	# 111:{'BASE': 'qqq', 'PARAMS': None, 'DETAILS': 'Fast quit.'},
	# 112:{'BASE': 'resetinterior ', 'PARAMS': ['<cellID>'], 'DETAILS': 'Reset an entire cell.'},
	# 113:{'BASE': 'refini', 'PARAMS': None, 'DETAILS': 'Refreshes all settings.'},
	# 114:{'BASE': 'resetquest ', 'PARAMS': ['<questID>'], 'DETAILS': 'Reset a quest.'},
	# 115:{'BASE': 'saq', 'PARAMS': None, 'DETAILS': 'Start all quests'},
	# 116:{'BASE': 'save', 'PARAMS': None, 'DETAILS': 'Write <name> gamesave.'},
	# 117:{'BASE': 'saveini', 'PARAMS': None, 'DETAILS': 'Save settings to file.'},
	# 118:{'BASE': 'set ', 'PARAMS': ['<Global Variable> to ', '<Value>'], 'DETAILS': 'Sets a global variable'},
	# 119:{'BASE': ' set gamehour to ##', 'PARAMS': None, 'DETAILS': 'Sets the time of the day'},
	# 120:{'BASE': ' set playeranimalcount to ', 'PARAMS': ['<qty>'], 'DETAILS': 'Sets number of animal followers'},
	# 121:{'BASE': ' set playerfollowercount to ', 'PARAMS': ['<qty>'], 'DETAILS': 'Sets number of followers'},
	# 122:{'BASE': ' set timescale to ', 'PARAMS': ['<qty>'], 'DETAILS': 'Sets the speed of how fast time advances in-game'},
	# 123:{'BASE': 'setplayerrace', 'PARAMS': None, 'DETAILS': 'Set player race.'},
	# 124:{'BASE': 'SexChange', 'PARAMS': None, 'DETAILS': "Switches the player or an NPC's gender"},
	# 125:{'BASE': 'SGTM', 'PARAMS': None, 'DETAILS': 'Changes the Gametime Multiplier to a specified value for slow motion, and fast forward type effects'},
	# 126:{'BASE': 'ShowGlobalVars', 'PARAMS': None, 'DETAILS': 'Shows all current game variables'},
	# 127:{'BASE': 'ShowMessage', 'PARAMS': None, 'DETAILS': 'Shows a message'},
	# 128:{'BASE': 'showracemenu', 'PARAMS': None, 'DETAILS': 'Opens the character creation menu.'},
	# 129:{'BASE': 'showracemenu ', 'PARAMS': ['<race>'], 'DETAILS': "Changes the player's race."},
	# 130:{'BASE': 'spf ', 'PARAMS': ['<file name>'], 'DETAILS': 'Save PC Face'},
	# 131:{'BASE': 'sqo', 'PARAMS': None, 'DETAILS': 'Itemizes quest objectives and their states'},
	# 132:{'BASE': 'sqt', 'PARAMS': None, 'DETAILS': 'List quest ids and targets'},
	# 133:{'BASE': 'sqv ', 'PARAMS': ['<questID>'], 'DETAILS': 'Show quest variables'},
	# 134:{'BASE': 'stp ', 'PARAMS': ['<unknown1> ', '<unknown2> ', '<unknown3> ', '<chroma>'], 'DETAILS': 'Set tint parameters'},
}