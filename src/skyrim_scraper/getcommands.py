from bs4 import BeautifulSoup
from bs4.element import NavigableString
from urllib.request import urlopen
import os
from rich import print

def run(is_test=False):
    url = 'https://en.uesp.net/wiki/Skyrim:Console'
    commands = scrape_page(url)
    print(commands)
    #write_to_file(commands, is_test)

def scrape_page(url_string):
    commands = []
    try:
        page = urlopen(url_string)
    except:
        print("error opening URL")
        return
    soup = BeautifulSoup(page, 'html.parser')
    content = soup.find('div', {'id':'mw-content-text'})
    table = content.find('table',  {'class':'wikitable centered'})
    rows = table.find_all('tr')
    #skip first row
    for row in rows[1::]:
        #not a header row
        if len(row) == 7:
            command = row.contents[1].text
            if not command: continue #parse_command rejects bad input
            details = row.contents[3].text
            command_dict = parse_command(command, details)
            commands.append(command_dict)
    return commands


def parse_command(command, details):
    new_command = dict()
    new_command['DETAILS'] = details
    new_command['PARAMS'] = None
    
    #looks at command string and splits it up
    
    
    new_command['BASE'] = None
    return new_command
            



#this writes the data to skyrimcommands.py
def write_to_file(data, is_test=False):
    dirname = os.path.dirname(__file__)
    if is_test:
        filename = os.path.join(dirname, "tests\skyrimcommands.py")
    else:
        dirname = dirname[:-14]#go to the previous folder
        filename = os.path.join(dirname, "skyrimdata\skyrimcommands.py")
    file = open(filename, 'w', encoding="utf-8")
    i = 0
    file.write('skyrim_factions = {\n')
    for item in data:  #this writes it in python dictionary syntax
        file.write('\t'+str(i)+':'+str(item)+',\n')
        i += 1
    file.write('\t}')
    file.close()

if __name__ == '__main__':
    run()
