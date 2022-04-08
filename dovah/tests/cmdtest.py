"""Tests to make sure the command maker prints commands that
   actually function in-game in skyrim"""
# This line does NOT work and is not intended for the final product
# it's for use while coding to enable intellisense when combined with a type hint.
from cgitb import lookup
from ..dovah_cli.commandmaker import CommandMaker
from ..dovah_cli.lookup import Lookup

class CmdTest:
    def __init__(self, cmd_maker_object:CommandMaker, lookup_object:Lookup):
        self.cmd_maker = cmd_maker_object
        self.lookup = lookup_object.lookup

    def run(self):
        self.complete_commands()
        self.incomplete_commands()
        self.broken_commands()
    
    def complete_commands(self):
        #does not take a parameter
        self._complete_toggle_commands()
        #takes a target
        self._complete_targeted_commands()
        #takes arguments but no target
        self._complete_untargeted_commands()

    def incomplete_commands(self):
        #blank command - shuold place user right at beginning of "add command" screen
        self.cmd_maker.add_cmd()
        self._incomplete_toggle_commands()

    def broken_commands(self):
        self._broken_toggle_commands()


    #############################################################
    #   COMPLETE COMMANDS BLOCK: THESE SHOULD WORK W/O INPUT    #
    #############################################################

    def _complete_toggle_commands(self):
        #writes toggle command with no argument
        self.cmd_maker.add_cmd(['0'])#read by code
        self.cmd_maker.add_cmd(['animcam'])#read by name
        self.cmd_maker.add_cmd(['0', 'foo'])#should ignore extra input
        #targeted toggle commands
        self.cmd_maker.add_cmd(['tcl', '1A6A4'])#Nazeem
        self.cmd_maker.add_cmd(['tcl', '']) #no target
        #toggle commands with arguments
        self.cmd_maker.add_cmd(['tmm', '1', '0', '1'])
        #toggle command with automatically-assigned argument
        self.cmd_maker.add_cmd([['tfc']])
        self.cmd_maker.add_cmd(['tfc', '1'])
        
    
    def _complete_targeted_commands(self):
        #additem
        self.cmd_maker.add_cmd(['24', 'player', 'f', '1'])
        self.cmd_maker.add_cmd(['additem', 'player', 'f', '1'])
        self.cmd_maker.add_cmd(['additem', 'player', 'f', 1])#number inputted as an int
        self.cmd_maker.add_cmd(['additem', 'player', 'f', 1.0])#number inputted as a float
        
        self.cmd_maker.add_cmd(['additem', 'player', self.lookup('gold')], '1')#using lookup
        self.cmd_maker.add_cmd(['additem', self.lookup('nazeem'), self.lookup('gold'), 1])
        
        

    def _complete_untargeted_commands(self):
        self.cmd_maker.add_cmd()
        self.cmd_maker.add_cmd()
        self.cmd_maker.add_cmd()
        self.cmd_maker.add_cmd()
        self.cmd_maker.add_cmd()
        self.cmd_maker.add_cmd()
        self.cmd_maker.add_cmd()
        self.cmd_maker.add_cmd()
        self.cmd_maker.add_cmd()
        self.cmd_maker.add_cmd()

    #############################################################
    #   INCOMPLETE COMMANDS BLOCK: THESE SHOULD ASK FOR INPUT   #
    #############################################################

    def _incomplete_toggle_commands(self):
            """User Interaction"""
            self.cmd_maker.add_cmd('tai')
            self.cmd_maker.add_cmd('tcl')
            self.cmd_maker.add_cmd('tcai')


    #############################################################
    #   BAD INPUT COMMANDS BLOCK: THESE SHOULD THROW EXCEPTIONS #
    #############################################################

    def _broken_toggle_commands(self):
        self.cmd_maker.add_cmd(['tcl', None]) #None should be empty string
