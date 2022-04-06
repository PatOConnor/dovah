import os
#this writes the data to the file of the associated category
def write_to_file(category, data, is_test):
    dirname = os.path.dirname(__file__)
    dirname = dirname[:-14]#go to the previous folder
    if is_test:
        filename = os.path.join(dirname, "tests\scrape_tests\skyrim"+category+".py")
    else:
        filename = os.path.join(dirname, "dovah_cli\skyrimdata\skyrim"+category+".py")
    file = open(filename, 'w', encoding="utf-8")
    i = 0
    file.write('skyrim_'+category+' = {\n')
    for item in data:  #this writes it in python dictionary syntax
        file.write('\t'+str(i)+':'+str(item)+',\n')
        i += 1
    file.write('\t}')
    file.close()