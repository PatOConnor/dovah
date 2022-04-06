import getskydata, getalchemy, getalcheffects, getfactiondata, getnpcdata, getlocationdata, getcommands
def run(param=None):
    print(param)
    if not param:
        print('which type of data to collect?\n', '1. Most Data\n', '2. Alchemy Ingredients\n', 
        '3. Alchemy Effects\n', '4. All\n', '5. Test')
        module_argument = input().lower().strip()
    else:
        module_argument = param[0]
        print( module_argument)
        param = None

    if module_argument in ['1', 'm']:
        getskydata.run()
    elif module_argument in ['2', 'a']:
        getalchemy.run()
    elif module_argument in ['3', 'e']:
        getalcheffects.run()
    elif module_argument in ['4', 'all']:
        getskydata.run('all')
        getalchemy.run()
        getalcheffects.run()
        getfactiondata.run()
        getcommands.run()
        getlocationdata.run()
        getnpcdata.run()
    elif module_argument in ['5', 'test']:
        getskydata.run(testing=True)
        getalchemy.run(is_test=True)
        getalcheffects.run(is_test=True)
        getfactiondata.run(is_test=True)
        getcommands.run(is_test=True)
        getlocationdata.run(is_test=True)
        getnpcdata.run(is_test=True)



if __name__=='__main__':
    run()
