from .skyrimdata.skyrimcommands import skyrim_commands
from .lookup import user_lookup, catalog_lookup
from rich import print
from rich.table import Table
from os import system, walk



class CommandMaker:
    MS_SKYPATH = 'C:\Program Files (x86)\Steam\steamapps\common\Skyrim Special Edition'  
    
    def __init__(self, skypath=None):
        self.cmd_list = []
        
        if skypath == None:
            self.skypath = CommandMaker.MS_SKYPATH
        elif skypath == 'find':
            self.skypath = CommandMaker.locate_skyrim()
        else:
            self.skypath = skypath

    def run(self, args=None):
        if not args:
            self.run_text_ui()
        elif args[0] =='load':
            if len(args) == 1:
                filename = input('Enter file to load: ')
            else: #the second one is the filename
                filename = args[1]
            self.load_cmds(filename)
            self.run_text_ui()
        else:
            #the word "new" may or may not be present
            if args[0] == 'new' and len(args) > 1:
                self.run_text_ui(args[1::])
            else:
                self.run_text_ui(args)

    def run_text_ui(self, args=None):
        def main_menu():
            return input('Main Menu: Save, Load, Add, Exit:  ').lower().split()
        while(True):
            system("cls")
            self.__show_cmds()
            if not args:
                choice = ['foo']
            else:
                choice = args
            while choice[0] not in ['add','save','load', 'exit']:
                choice = main_menu()

            if choice[0] == 'add':
                if len(choice) > 1:
                    add_cmd(arg=choice[1::]) #further parsing happens by method
                else:
                    add_cmd()

            if choice[0] == 'save':
                if len(choice) > 1:
                    save_cmds(choice[1])#filename
                else:
                    filename = input('What to name this file? ')
                    save_cmds(filename)

            if choice[0] == 'load':
                if len(choice) > 1:
                    self.load_cmds(choice[1])#filename
                else:
                    self.load_cmds()

            if choice[0] == 'exit':
                break
            #after first loop, delete arguments and input from user
            choice.clear()
            if args: args.clear()


    '''Add Command to cmd_list'''
    def add_cmd(self, arg=None):
        #first argument should be either key to command or name of command
        #if it is, then the command wizard proceeds and stops when input runs out
        #if it is not, them the command wizard regards input as garbage and
        #continues as if there were no arguments
        if arg:
            basearg = arg.pop(0)
            #check if the argument is the key corresponding to a command
            k = catalog_lookup(basearg, 'commands')
            if k < 0:
                k = CommandMaker._ask_for_cmd_key()
            cmdbase = skyrim_commands[k]['NAME']
        else:
            k = CommandMaker._ask_for_cmd_key()
            cmdbase = skyrim_commands[k]['NAME']
        #next argument is the desired target if applicable
        if arg:
            target = arg.pop(0)  #e.g. add additem player
        elif 24 <= k <= 94 or k in [4,7,8]:
            target = CommandMaker._ask_for_target()
        #next is all remaining parameters get passed through ask_for_param
        other_params = skyrim_commands[k]['PARAMS']
        param_answers = []
        if arg:
            param_answers = arg  #e.g. add additem player f 20 => [f, 20]
        paramcount = len(param_answers)
        if len(other_params) > len(param_answers):
            param_answers.extend(CommandMaker._ask_for_param(other_params[paramcount::]))
        self.cmd_list.append(CommandMaker.__form_cmd(cmdbase, target, param_answers))


    '''Saves command as a list to folder designated as skyrim directory'''
    def save_cmds(self, filename, testing=False):
        #writing file for test
        if testing:
            filename = '/batches/'+filename+'.txt'
        else:
            filename = self.skypath+'/'+filename+'.txt'
        with open(filename, "w") as f:
            for cmd in self.cmd_list:
                f.write(cmd+'\n')
            f.close()
        

    '''Loads commands from local folder in /batches'''
    def load_cmds(self, filename, testing=False):
        if testing:
            filename ='/batches/'+filename+'.txt'
        else:
            filename = self.skypath+'/'+filename+'.txt'
        with open(filename) as f:
            codes = f.readlines()
            for c in codes:
                self.cmd_list.append(c)
            f.close()

    #Helper methods for the console command writer
    def _ask_for_cmd_key():
        s = input('input name or id# of desired command: ')
        s_key = catalog_lookup(s, 'commands')
        if s_key > 0:
            return s_key
        else:
            for i in skyrim_commands:
                print(str(i)+str(skyrim_commands[i]))
                if not i % 30 and i > 0:
                    x = input('Show More Commands?')
                    if x.lower().strip() in ['n', 'no']:
                        break
            while(s_key < 0):
                s = input('select key: ')
                s_key = catalog_lookup(s, 'commands')
            return s_key

    def _ask_for_target():
        if input('is the player the target? ').lower() == 'y':
            return 'player'
        else:
            return user_lookup('npc')

    def _ask_for_param(paramIDs):
        params = []
        for p in paramIDs:
            if p == '<item ID>':
                params.append(user_lookup('item')[1])
            elif p ==  '<perk ID>':
                params.append(user_lookup('perk')[1])
            elif p ==  '<spell ID>':
                params.append(user_lookup('spell')[1])
            elif p ==  '<faction ID>':
                params.append(user_lookup('faction')[1])
            elif p ==  '<target>':
                params.append(user_lookup('npc')[1])
            elif p ==  '<skill>':
                params.append(user_lookup('skill')[0])
            elif p ==  '<quest ID>':
                params.append(user_lookup('quest')[1])
            elif p ==  '<attribute>':
                params.append(user_lookup('av')[0])
            elif p ==  '<0>':
                params.append('0')
            elif p ==  '<1>':
                params.append('1')
            else:
                word = input(p+'? ')
                params.append(word)
        return params

    def __form_cmd(cmdbase, target=None, params=None):
        text = ''
        if target != None:
            text += target+'.'
        text += cmdbase+' '#space doesnt harm if theres no parameters after
        if params != None:
            text += ' '.join(params)
        return text

    def __show_cmds(self):
        if len(self.cmd_list) < 1:
            print('No Commands Stored')
        else:
            print('Existing Commands: ')
            for cmd in self.cmd_list:
                print(cmd)
        
    '''searches through folders to find skyrim and sets it to self.skypath'''
    def locate_skyrim(start_folder='C:/'):
        for root, dirs, files in walk(start_folder):
            if 'SkyrimSE.exe' in files:
                self.skypath = root
                #print('located skyrim! heres the proof: ', files)
                return