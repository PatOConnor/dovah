#this serves as a top-level file to handle the importing of all submodules for testing
from distutils.cmd import Command
from tests.unittest import UnitTest
from tests.cmdtest import CmdTest
from dovah_cli.commandmaker import CommandMaker
from sys import argv

if __name__ == '__main__':
    if argv[1] == 'unittest':
        tester = UnitTest(CommandMaker())
    elif argv[1] == 'cmdtest':
        tester = CmdTest(CommandMaker())
    tester.run()
