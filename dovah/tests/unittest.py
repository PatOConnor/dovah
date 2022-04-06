#this class is passed the object that it is testing from a higher-level module
class UnitTest:
       def run(command_maker):
              """Second Set of Blocks: testing individual methods outside of the run() method"""
              command_maker.run_text_ui()
              command_maker.add_cmd()
              command_maker.save_cmds(filename='cmdtest_1', testing=True)
              command_maker.load_cmds(filename='batch1', testing=True)
              #       Here is the block for the
              #       helper methods for inter-
              #       -acting with the user
              print('', command_maker._ask_for_cmd_key())
              print('', command_maker._ask_for_target())
              print('', command_maker._ask_for_param())
              #form command
              print('.__form_cmd()')
              print('', command_maker.__form_cmd(cmdbase='additem', target='player', params=['F', '200']))
              print('show cmds:')
              command_maker.__show_cmds()
              print('locate skyrim:')
              command_maker.skypath = None
              print('skypath value just set to None:', command_maker.skypath)
              command_maker.locate_skyrim()
              print('updated skyrim location:', command_maker.skypath)
              print('standard skyrim location:', command_maker.MS_SKYPATH)