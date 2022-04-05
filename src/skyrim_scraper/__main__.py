import getskydata, getalchemy, getalcheffects, getfactiondata
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
        getskydata.run()
        getalchemy.run()
        getalcheffects.run()
        getfactiondata.run()
    elif module_argument in ['5', 'test']:
        getskydata.run(testing=True)
        getalchemy.run(is_test=True)
        getalcheffects.run(is_test=True)
        getfactiondata.run(is_test=True)


if __name__=='__main__':
    run()
