import lookup, commandmaker, alchemist
from .. import skyrimscraper
from sys import argv
from rich import print

module_argument = '0'
if len(argv) > 1: #there are arguments present
    module_argument = argv[1].lower()
else:
    choice_input = True
    while(choice_input):
        choice_input = False #only runs once unless invalid input tells it to run again
        print('#'*10)
        print('Welcome to DovahPy. Which module would you like to access?')
        print('\n 1. Console Command Creator\n', '2. Best Alchemy\n', '3. Item Code Lookup\n')
        module_argument = input('Enter Selection: ')
        if module_argument in ['1', 'c', 'cmd', 'cmds', 'command', 'commands']:
            if len(argv) > 2:#additional arguments
                commandmaker.run(argv[2::])
            else:
                commandmaker.run()
        elif module_argument in ['2', 'a', 'alch', 'alchemy', 'alchemist']:
            alchemist.run()
        elif module_argument in ['3', 'l', 'look', 'lookup']:
            if len(argv) > 2:#string to look up
                lookup.run(argv[2])
            else:
                lookup.run()
