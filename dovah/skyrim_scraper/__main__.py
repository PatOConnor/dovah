import getskydata, getalchemy, getalcheffects, getfactiondata, getnpcdata, getlocationdata, getcommands
def run(param=None):
    print(param)
    if not param:
        print('which type of data to collect?\n', '1. All\n', '2. Specific\n', 
        '3. Test Scraper')
        module_argument = input().lower().strip()
    else:
        module_argument = param[0]
        print( module_argument)
        param = None
    if module_argument in ['1', 'all']:
        getskydata.run()
        getskydata.run('all')
        getalchemy.run()
        getalcheffects.run()
        getfactiondata.run()
        getcommands.run()
        getlocationdata.run()
        getnpcdata.run()
    elif module_argument in ['3', 'test']:
        getskydata.run(testing=True)
        getalchemy.run(is_test=True)
        getalcheffects.run(is_test=True)
        getfactiondata.run(is_test=True)
        getcommands.run(is_test=True)
        getlocationdata.run(is_test=True)
        getnpcdata.run(is_test=True)
    elif module_argument == '2':
        print('Which Type of Data?', '1. ', '2. ')
        input



if __name__=='__main__':
    run()
