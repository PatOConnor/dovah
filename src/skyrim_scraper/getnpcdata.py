from email.mime import base
from bs4 import BeautifulSoup
from bs4.element import NavigableString
from urllib.request import urlopen
import os
from rich import print

def run(is_test=True):
    url = 'https://elderscrolls.fandom.com/wiki/Console_Commands_(Skyrim)/Characters'
    npcs = scrape_page(url)
    # print(npcs)
    write_to_file(npcs, is_test)

def scrape_page(url_string):
    npcs = []
    try:
        page = urlopen(url_string)
    except:
        print("error opening URL")
        return
    soup = BeautifulSoup(page, 'html.parser')
    rows = soup.find_all('tr')
    for row in rows[3:-7]:#remove infobars at top and bottom
        npc_name = row.contents[1].text
        npc_name = npc_name.replace('\n', '')
        ref_id = row.contents[3].text
        ref_id = ref_id.replace('\n', '')
        try:
            base_id = row.contents[5].text
            base_id = base_id.replace('\n', '')
        except: #Ri'saad is the only one that breaks it because there is no punctuation on his lack of a base ID
            base_id = '-'
        npcs.append({'NAME':npc_name, 'REF_ID':ref_id, 'BASE_ID':base_id})
    return npcs


def write_to_file(data, is_test=False):
    dirname = os.path.dirname(__file__)
    if is_test:
        filename = os.path.join(dirname, "tests\skyrimnpcs.py")
    else:
        dirname = dirname[:-14]#go to the previous folder
        filename = os.path.join(dirname, "skyrimdata\skyrimnpcs.py")
    file = open(filename, 'w', encoding="utf-8")
    i = 0
    file.write('skyrim_npcs = {\n')
    for item in data:  #this writes it in python dictionary syntax
        file.write('\t'+str(i)+':'+str(item)+',\n')
        i += 1
    file.write('\t}')
    file.close()

if __name__=='__main__':
    run()