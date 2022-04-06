#this serves as a top-level file to handle the importing of all submodules for testing
from tests.unittest import UnitTest
from tests.cmdtest import CmdTest
from dovah_cli import commandmaker
from sys import argv

if __name__ == '__main__':
    print(argv)
    if argv[1] == 'unittest':
        UnitTest.run(commandmaker)
    elif argv[1] == 'cmdtest':
        CmdTest.run(commandmaker)
