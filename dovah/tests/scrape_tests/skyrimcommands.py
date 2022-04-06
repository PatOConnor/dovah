skyrim_commands = {
	0:{'NAME': 'animcam', 'PARAMS': None, 'DETAILS': 'Toggle animator camera'},
	1:{'NAME': 'psb', 'PARAMS': None, 'DETAILS': 'Player Spell Book'},
	2:{'NAME': 's1st', 'PARAMS': None, 'DETAILS': 'Shows 1st person model in 3rd person'},
	3:{'NAME': 'sucsm ', 'PARAMS': ['<number>'], 'DETAILS': 'Changes the speed of the free-flying camera (UFO cam)'},
	4:{'NAME': 'tai', 'PARAMS': None, 'DETAILS': 'Toggle AI'},
	5:{'NAME': 'tb', 'PARAMS': None, 'DETAILS': 'Toggle Borders'},
	6:{'NAME': 'tc', 'PARAMS': None, 'DETAILS': 'Toggle controls driven'},
	7:{'NAME': 'tcai', 'PARAMS': None, 'DETAILS': 'Toggle Combat AI'},
	8:{'NAME': 'tcl', 'PARAMS': None, 'DETAILS': 'Toggle collision (clipping, noclip)'},
	9:{'NAME': 'tdetect', 'PARAMS': None, 'DETAILS': 'Toggle AI Detection'},
	10:{'NAME': 'teofis', 'PARAMS': None, 'DETAILS': 'Toggle End-Of-Frame ImageSpace'},
	11:{'NAME': 'tfc ', 'PARAMS': ['<1>'], 'DETAILS': 'Freeflying camera'},
	12:{'NAME': 'tfow', 'PARAMS': None, 'DETAILS': 'Toggle Fog of War'},
	13:{'NAME': 'tg', 'PARAMS': None, 'DETAILS': 'Toggle grass'},
	14:{'NAME': 'tgm', 'PARAMS': None, 'DETAILS': 'Toggle god mode'},
	15:{'NAME': 'tim', 'PARAMS': None, 'DETAILS': 'Toggle immortal mode'},
	16:{'NAME': 'tll', 'PARAMS': None, 'DETAILS': 'Toggle LOD'},
	17:{'NAME': 'tm', 'PARAMS': None, 'DETAILS': 'Toggle menus (HUD)'},
	18:{'NAME': 'tmm ', 'PARAMS': ['<show?>(,', '<discovered?>,', '<includehidden?>)'], 'DETAILS': 'Show/hide all map markers'},
	19:{'NAME': 'ts', 'PARAMS': None, 'DETAILS': 'Toggle sky'},
	20:{'NAME': 'tscr', 'PARAMS': None, 'DETAILS': 'Toggle script processing.'},
	21:{'NAME': 'tt', 'PARAMS': None, 'DETAILS': 'Toggle trees'},
	22:{'NAME': 'twf', 'PARAMS': None, 'DETAILS': 'Toggle wireframe'},
	23:{'NAME': 'tws', 'PARAMS': None, 'DETAILS': 'Toggle water system'},
	24:{'NAME': 'additem ', 'PARAMS': ['<item ID> ', '<count> ', '<flag (optional)>'], 'DETAILS': 'Give a character the specified amount of an item'},
	25:{'NAME': 'addperk ', 'PARAMS': ['<perk ID>'], 'DETAILS': 'Give a character the selected perk'},
	26:{'NAME': 'addspell ', 'PARAMS': ['<spell ID>'], 'DETAILS': "Add a specific spell to a character's available arsenal."},
	27:{'NAME': 'addfac/addtofaction ', 'PARAMS': ['<faction ID> ', '<faction rank>'], 'DETAILS': 'Add a character to a faction.'},
	28:{'NAME': 'advlevel', 'PARAMS': None, 'DETAILS': "Advance a character's level by one."},
	29:{'NAME': 'AdvSkill ', 'PARAMS': ['<skill> ', '<nn>'], 'DETAILS': 'Advance the specified skill.'},
	30:{'NAME': 'completequest ', 'PARAMS': ['<quest ID>'], 'DETAILS': 'Complete the quest instantly.'},
	31:{'NAME': 'DamageActorValue ', 'PARAMS': ['<attribute> ', '<nn>'], 'DETAILS': 'Damage value of attribute by <nn> amount'},
	32:{'NAME': 'disable', 'PARAMS': None, 'DETAILS': "Don't render the selected object (includes actors.)"},
	33:{'NAME': 'dispelallspells', 'PARAMS': None, 'DETAILS': 'Dispel all temporary spell effects on target'},
	34:{'NAME': 'drop', 'PARAMS': None, 'DETAILS': "Force drop items from a character's inventory"},
	35:{'NAME': 'duplicateallitems ', 'PARAMS': ['<container/NPC refID>'], 'DETAILS': 'Duplicate all items in the targeted container and places them in the given container.'},
	36:{'NAME': 'enable', 'PARAMS': None, 'DETAILS': 'Render the selected object (includes actors.)'},
	37:{'NAME': 'equipitem ', 'PARAMS': ['<Item baseID> ', '<0/1> ', '<left/right>'], 'DETAILS': 'Equip selected NPC with Item'},
	38:{'NAME': 'equipspell ', 'PARAMS': ['<Spell ID> ', '<Casting Sources>'], 'DETAILS': 'Equipping the given spell on a particular casting source.'},
	39:{'NAME': 'equipshout ', 'PARAMS': ['<Shout ID>'], 'DETAILS': 'Equipping the given shout.'},
	40:{'NAME': 'forceAV ', 'PARAMS': ['<attribute> ', '<nn>'], 'DETAILS': 'Force to modify the value of attribute'},
	41:{'NAME': 'getAV ', 'PARAMS': ['<attribute>'], 'DETAILS': 'Get value of attribute'},
	42:{'NAME': 'getAVinfo ', 'PARAMS': ['<attribute>'], 'DETAILS': 'Get value information of attribute'},
	43:{'NAME': 'getlevel ', 'PARAMS': ['<target>'], 'DETAILS': 'Get level of target'},
	44:{'NAME': 'GetLocationCleared ', 'PARAMS': ['<locationID>'], 'DETAILS': "Check an area's clear code."},
	45:{'NAME': 'getrelationshiprank ', 'PARAMS': ['<target>'], 'DETAILS': 'Get the relationship rank of two actors.'},
	46:{'NAME': 'getstage ', 'PARAMS': ['<quest ID>'], 'DETAILS': 'Show the current active quest stage.'},
	47:{'NAME': 'hasperk ', 'PARAMS': ['<perk ID>'], 'DETAILS': 'Check if the selected actor has a perk with the selected ID'},
	48:{'NAME': 'incPCS ', 'PARAMS': ['<skill name>'], 'DETAILS': 'Increase the given skill to the next level.'},
	49:{'NAME': 'kill ', 'PARAMS': ['<Actor ID (optional)>'], 'DETAILS': 'Kill the selected actor (NOT the optional Actor ID).'},
	50:{'NAME': 'lock ', 'PARAMS': ['<level>'], 'DETAILS': 'Lock targeted object (i.e. door, container) with a difficulty of <level>.'},
	51:{'NAME': 'MarkForDelete', 'PARAMS': None, 'DETAILS': 'Delete an object.'},
	52:{'NAME': 'modAV ', 'PARAMS': ['<attribute> ', '<nn>'], 'DETAILS': 'Modify value of attribute by <nn> amount'},
	53:{'NAME': 'moveto ', 'PARAMS': ['<actor ID>'], 'DETAILS': 'Move a character to specified actor and vice versa.'},
	54:{'NAME': 'movetoqt ', 'PARAMS': ['<quest ID>'], 'DETAILS': 'Move to quest target'},
	55:{'NAME': 'openactorcontainer 1', 'PARAMS': None, 'DETAILS': "Open a character's inventory."},
	56:{'NAME': 'paycrimegold (', 'PARAMS': ['<jail?> ', '<confiscate?> ', '<faction ID>)'], 'DETAILS': 'Pay the bounty.'},
	57:{'NAME': 'placeatme ', 'PARAMS': ['<actor/object ID>'], 'DETAILS': 'Spawn specified actor or object at current position.'},
	58:{'NAME': 'playidle ', 'PARAMS': ['<idle ID>'], 'DETAILS': 'Play an animation (idle) on the specified actor.'},
	59:{'NAME': 'pushactoraway ', 'PARAMS': ['<actor ID> ', '<number>'], 'DETAILS': 'Push an actor away in a random direction.'},
	60:{'NAME': 'recycleactor ', 'PARAMS': ['<destination reference (optional)>'], 'DETAILS': 'Revive/Reset targeted NPC or object.'},
	61:{'NAME': 'removeallitems ', 'PARAMS': ['<actor or container ID>'], 'DETAILS': "Remove all items from a character's inventory."},
	62:{'NAME': 'removeitem ', 'PARAMS': ['<item ID> ', '<count>'], 'DETAILS': "Remove the specified amount of an item from a character's inventory."},
	63:{'NAME': 'removeperk ', 'PARAMS': ['<perk ID>'], 'DETAILS': "Remove the specified perk from a character's skills."},
	64:{'NAME': 'removespell ', 'PARAMS': ['<spell ID>'], 'DETAILS': "Removes a specific spell from a character's spell book. Also works with powers, abilities, blessings, and diseases, but not shouts"},
	65:{'NAME': 'resetAI', 'PARAMS': None, 'DETAILS': "Reset an NPC's AI."},
	66:{'NAME': 'resethealth', 'PARAMS': None, 'DETAILS': 'Restore a character to full health.'},
	67:{'NAME': 'resetinventory', 'PARAMS': None, 'DETAILS': "Reset a container or a character's inventory."},
	68:{'NAME': 'RestoreActorValue ', 'PARAMS': ['<attribute> ', '<nn>'], 'DETAILS': 'Restore the value of attribute by <nn> amount'},
	69:{'NAME': 'resurrect ', 'PARAMS': ['<1>'], 'DETAILS': 'Resurrect target actor'},
	70:{'NAME': 'say ', 'PARAMS': ['<dialog topic ID>'], 'DETAILS': 'Makes the targeted actor say a specific dialog topic.'},
	71:{'NAME': 'setactoralpha ', 'PARAMS': ['<0–100>'], 'DETAILS': "Change the selected actor's alpha/opacity."},
	72:{'NAME': 'setAV ', 'PARAMS': ['<attribute> ', '<nn>'], 'DETAILS': 'Set value of attribute'},
	73:{'NAME': 'setessential ', 'PARAMS': ['<base ID> ', '<0 or 1>'], 'DETAILS': 'Set a character as mortal (0) or immortal (1).'},
	74:{'NAME': 'setghost ', 'PARAMS': ['<0 or 1>'], 'DETAILS': 'Set ghost mode for the targeted NPC.'},
	75:{'NAME': 'setgs ', 'PARAMS': ['<setting> ', '<value>'], 'DETAILS': 'Set game setting.'},
	76:{'NAME': 'setlevel ', 'PARAMS': ['<multiplier> ', '<modifier> ', '<min> ', '<max>'], 'DETAILS': 'Set NPC level'},
	77:{'NAME': 'SetLocationCleared ', 'PARAMS': ['<locationID> 1'], 'DETAILS': 'Set whether an area has been cleared.'},
	78:{'NAME': 'setnpcweight ', 'PARAMS': ['<0–100>\n(snpcw)'], 'DETAILS': 'Set the weight of the selected NPC and updates the model to reflect the new weight.'},
	79:{'NAME': 'setownership ', 'PARAMS': ['<ID>'], 'DETAILS': 'Sets ownership of the targeted item.'},
	80:{'NAME': 'setrace ', 'PARAMS': ['<race>'], 'DETAILS': "Change a character's race."},
	81:{'NAME': 'setrelationshiprank ', 'PARAMS': ['<target> ', '<#>'], 'DETAILS': 'Change the relationship between two actors'},
	82:{'NAME': 'setscale ', 'PARAMS': ['<#>'], 'DETAILS': 'Scale size of target.'},
	83:{'NAME': 'setstage ', 'PARAMS': ['<quest ID> ', '<stage #>'], 'DETAILS': 'Set the current stage of the given quest.'},
	84:{'NAME': 'setunconscious ', 'PARAMS': ['<integer>'], 'DETAILS': 'A value of 1 will be unconscious'},
	85:{'NAME': 'inv/showinventory', 'PARAMS': None, 'DETAILS': "Display the base IDs of every item in a character's inventory."},
	86:{'NAME': 'shp ', 'PARAMS': ['<parameter #1-parameter #9>'], 'DETAILS': 'Set HDR parameters'},
	87:{'NAME': 'sifh ', 'PARAMS': ['<#>'], 'DETAILS': 'Set whether an actor should ignore friendly hits.'},
	88:{'NAME': 'sqs ', 'PARAMS': ['<quest ID>'], 'DETAILS': 'Display stages of a quest'},
	89:{'NAME': 'stopcombat', 'PARAMS': None, 'DETAILS': 'Stop combat with a targetted NPC'},
	90:{'NAME': 'str ', 'PARAMS': ['<0–1.000000>'], 'DETAILS': 'Set the refraction value of the selected target.'},
	91:{'NAME': 'teachword ', 'PARAMS': ['<word>'], 'DETAILS': 'Teach a dragon shout.'},
	92:{'NAME': 'unequipitem ', 'PARAMS': ['<Item baseID>'], 'DETAILS': 'Unequip item from selected NPC'},
	93:{'NAME': 'unlock', 'PARAMS': None, 'DETAILS': 'Unlock the targeted object.'},
	94:{'NAME': 'unlockword ', 'PARAMS': ['<word>'], 'DETAILS': 'Unlock a dragon shout.'},
	95:{'NAME': 'bat', 'PARAMS': None, 'DETAILS': 'Execute a batch file'},
	96:{'NAME': 'caqs', 'PARAMS': None, 'DETAILS': 'Complete all quest stages'},
	97:{'NAME': 'coc', 'PARAMS': None, 'DETAILS': 'Transport to <cellname>'},
	98:{'NAME': 'cow', 'PARAMS': None, 'DETAILS': 'Transports to cell <cell x, cell y> in <worldspace>'},
	99:{'NAME': 'csb', 'PARAMS': None, 'DETAILS': 'Clear screen blood'},
	100:{'NAME': 'fov', 'PARAMS': None, 'DETAILS': 'Set fov <angle>'},
	101:{'NAME': 'fw', 'PARAMS': None, 'DETAILS': 'Force Weather'},
	102:{'NAME': 'GetGlobalValue ', 'PARAMS': ['<Variable>'], 'DETAILS': 'Returns the value of a single global game setting.'},
	103:{'NAME': 'GetInCellParam ', 'PARAMS': ['<Cell ID> ', '<Object ID>'], 'DETAILS': 'Checks if an object is in a specified cell.'},
	104:{'NAME': 'GetPCMiscStat ', 'PARAMS': ['<Stat>'], 'DETAILS': 'Returns the value of the (typically meaningless) stats shown in the ESC menu.'},
	105:{'NAME': 'help', 'PARAMS': None, 'DETAILS': 'Returns the IDs of all items, spells, game settings, etc. which have the entered text in their name.'},
	106:{'NAME': 'killallactors', 'PARAMS': None, 'DETAILS': 'Kill all actors.'},
	107:{'NAME': 'load', 'PARAMS': None, 'DETAILS': 'Loads <name> gamesave.'},
	108:{'NAME': 'ModPCMiscStat ', 'PARAMS': ['<Stat> ', '<nn>'], 'DETAILS': 'Adjusts the value of the (typically meaningless) stats shown in the ESC menu by <nn> amount.'},
	109:{'NAME': 'pcb', 'PARAMS': None, 'DETAILS': 'Purge cell buffer'},
	110:{'NAME': 'prid ', 'PARAMS': ['<RefID>'], 'DETAILS': 'Pick reference by ID'},
	111:{'NAME': 'qqq', 'PARAMS': None, 'DETAILS': 'Fast quit.'},
	112:{'NAME': 'resetinterior ', 'PARAMS': ['<cellID>'], 'DETAILS': 'Reset an entire cell.'},
	113:{'NAME': 'refini', 'PARAMS': None, 'DETAILS': 'Refreshes all settings.'},
	114:{'NAME': 'resetquest ', 'PARAMS': ['<questID>'], 'DETAILS': 'Reset a quest.'},
	115:{'NAME': 'saq', 'PARAMS': None, 'DETAILS': 'Start all quests'},
	116:{'NAME': 'save', 'PARAMS': None, 'DETAILS': 'Write <name> gamesave.'},
	117:{'NAME': 'saveini', 'PARAMS': None, 'DETAILS': 'Save settings to file.'},
	118:{'NAME': 'set ', 'PARAMS': ['<Global Variable> to ', '<Value>'], 'DETAILS': 'Sets a global variable'},
	119:{'NAME': ' set gamehour to ##', 'PARAMS': None, 'DETAILS': 'Sets the time of the day'},
	120:{'NAME': ' set playeranimalcount to ', 'PARAMS': ['<qty>'], 'DETAILS': 'Sets number of animal followers'},
	121:{'NAME': ' set playerfollowercount to ', 'PARAMS': ['<qty>'], 'DETAILS': 'Sets number of followers'},
	122:{'NAME': ' set timescale to ', 'PARAMS': ['<qty>'], 'DETAILS': 'Sets the speed of how fast time advances in-game'},
	123:{'NAME': 'setplayerrace', 'PARAMS': None, 'DETAILS': 'Set player race.'},
	124:{'NAME': 'SexChange', 'PARAMS': None, 'DETAILS': "Switches the player or an NPC's gender"},
	125:{'NAME': 'SGTM', 'PARAMS': None, 'DETAILS': 'Changes the Gametime Multiplier to a specified value for slow motion, and fast forward type effects'},
	126:{'NAME': 'ShowGlobalVars', 'PARAMS': None, 'DETAILS': 'Shows all current game variables'},
	127:{'NAME': 'ShowMessage', 'PARAMS': None, 'DETAILS': 'Shows a message'},
	128:{'NAME': 'showracemenu', 'PARAMS': None, 'DETAILS': 'Opens the character creation menu.'},
	129:{'NAME': 'showracemenu ', 'PARAMS': ['<race>'], 'DETAILS': "Changes the player's race."},
	130:{'NAME': 'spf ', 'PARAMS': ['<file name>'], 'DETAILS': 'Save PC Face'},
	131:{'NAME': 'sqo', 'PARAMS': None, 'DETAILS': 'Itemizes quest objectives and their states'},
	132:{'NAME': 'sqt', 'PARAMS': None, 'DETAILS': 'List quest ids and targets'},
	133:{'NAME': 'sqv ', 'PARAMS': ['<questID>'], 'DETAILS': 'Show quest variables'},
	134:{'NAME': 'stp ', 'PARAMS': ['<unknown1> ', '<unknown2> ', '<unknown3> ', '<chroma>'], 'DETAILS': 'Set tint parameters'},
	}