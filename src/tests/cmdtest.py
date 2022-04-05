from ..dovah_cli import commandmaker as cm


"""First Set of Blocks: testing run() with different parameters"""
#opens up CLI
cm.run()
cm.run('new')

#prompts user to enter filename
cm.run('load')
#user enters filename
cm.run('load batch1')
#following commands ignored
cm.run('load batch1 foo bar')


#testing toggle commands
cm.run('new add 0')
cm.run('new add animcam')
cm.run('new add 1')
cm.run('new add psb')
cm.run('new add 2')
cm.run('new add tcai')
cm.run('new add 3')
cm.run('new add tcl')
cm.run('new add 4')
cm.run('new add tg')
cm.run('new add 5')
cm.run('new add tgm')
cm.run('new add 6')
cm.run('new add tim')
cm.run('new add 7')
cm.run('new add tm')
cm.run('new add 8')
cm.run('new add ts')
cm.run('new add 9')
cm.run('new add tt')


#should place user in CLI 
#prompting for the remaining input
cm.run('new add 10')
cm.run('new add 10 player')
cm.run('new add 10 player f')
cm.run('new add 10 player f 200')

cm.run('new add additem')
cm.run('new add additem player')
cm.run('new add additem player f')
cm.run('new add additem player f 200')

cm.run('load batch1 add 10')
cm.run('load batch1 add 10 player')
cm.run('load batch1 add 10 player f')
cm.run('load batch1 add 10 player f 200')

cm.run('load batch1 add additem')
cm.run('load batch1 add additem player')
cm.run('load batch1 add additem player f')
cm.run('load batch1 add additem player f 200')










"""Second Set of Blocks: testing individual 
       methods outside of the run() method"""
cm.run_text_ui()


cm.add_cmd()







cm.save_cmds(filename='cmdtest_1', testing=True)
cm.load_cmds(filename='batch1', testing=True)



#       Here is the block for the
#       helper methods for inter-
#       -acting with the user

print('', cm._ask_for_cmd_key())
print('', cm._ask_for_target())
print('', cm._ask_for_param())

#form command
print('.__form_cmd()')
print('', cm.__form_cmd(cmdbase='additem', target='player', params=['F', '200']))




print('show cmds:')
cm.__show_cmds()
print('locate skyrim:')
cm.skypath = None
print('skypath value just set to None:', cm.skypath)
cm.locate_skyrim()
print('updated skyrim location:', cm.skypath)
print('standard skyrim location:', cm.MS_SKYPATH)