"""Tests to make sure the command maker prints commands that
   actually function in-game in skyrim"""
# This line does NOT work and is not intended for the final product
# it's for use while coding to enable intellisense when combined with a type hint.
from ..dovah_cli.commandmaker import CommandMaker

class CmdTest:
    def __init__(self, cmd_maker_object:CommandMaker):
        self.cmd_maker = cmd_maker_object


    def run(self):
        self.complete_commands()
        self.incomplete_commands()
        self.bad_input_commands()
    
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

    def bad_input_commands(self):
        pass

    def _complete_toggle_commands(self):
        """No User Interaction"""
        #writes command with no argument
        self.cmd_maker.add_cmd(['0'])
        self.cmd_maker.add_cmd(['animcam'])
        self.cmd_maker.add_cmd(['0', 'foo'])#should ignore extra input
        self.cmd_maker.add_cmd(['tcl', '1A6A4'])
        self.cmd_maker.add_cmd(['tcl', None])
        
    
    def _complete_targeted_commands(self):
        self.cmd_maker.add_cmd()
        self.cmd_maker.add_cmd()
        self.cmd_maker.add_cmd()
        self.cmd_maker.add_cmd()
        self.cmd_maker.add_cmd()
        self.cmd_maker.add_cmd()
        

    def _complete_untargeted_commands():
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


    def _incomplete_toggle_commands(self):
            """User Interaction"""
            self.cmd_maker.add_cmd('tai')
            self.cmd_maker.add_cmd('tcl')
            self.cmd_maker.add_cmd('tcai')

