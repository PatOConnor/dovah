from bs4 import BeautifulSoup
from urllib.request import urlopen
import os
from writetofile import write_to_file

################################
# program uses beautiful soup to access website, get tables, format them into
# usable data and save to file. Redundant now but included inpackage for posterity
################################
is_test = False
def run(category=None, testing=False):
    if testing: 
        category = 'all'
        global is_test 
        is_test = True
    if category == 'items':
        scrape_all(category, 88)#second parameter is how many pages of data to scrape
    elif category == 'enchantments':
        scrape_all(category, 10)
    elif category in ('perks', 'quests', 'spells', 'avs', 'weather'):
        scrape_all(category)
    elif category == 'all':
        get_all_tables()
    else:
        category = main_menu()#invalid input

def main_menu():
    print('######################################\n',
        '#\t\tSkyrim Data Scraper\n',
        '#\t\tFor use with Command Batcher\n',
        '#\tBy Pat O\'Connor\n',
        '#\tData Courtesy of skyrimcommands.com and UESP\n')
    print('categories are items, perks, spells, avs, quests, enchantments, weather')
    return input('enter item type to gather: ').lower().strip()

def get_all_tables():
    print('items')
    scrape_all('items', 88)
    print('enchantments')
    scrape_all('enchantments', 10)
    for c in ['perks', 'quests', 'spells', 'avs', 'weather']:
        print(c)
        scrape_all(c)

#returns massive dictionary of all the data of a given category
def scrape_all(category, bound=None):
    main_url = 'http://www.skyrimcommands.com/'+category+'/'
    value_table_list = list()
    value_table_list.append(scrape_page(main_url))
    print('added page 1')

    #take the first row and make values for keys
    dict_keys = value_table_list[0].pop(0)
    dict_keys = list(dict_keys)
    dict_keys[0] = 'NAME'
    dict_keys = [x.strip().upper().replace(' ','_') for x in dict_keys] 

    if(bound):
        #bounds: items list has 88 pages, npcs has 28
        #        enchantments has 10, the rest have 1
        for i in range(2,bound):#88 is the max
            current_url = main_url+str(i)+'/'
            current_page = scrape_page(current_url)
            if current_page != None:
                value_table_list.append(current_page)
                print('added page '+str(i))
        print('pages added to table')
   
    #these few lines combine the separate pages into one long page
    master_list = []
    for page in value_table_list:
        master_list.extend(page)
    
    final_list_of_dicts = []
    for row in master_list:
        new_entry = dict()
        for k,cell in zip(dict_keys, row):
            new_entry[k] = cell
        final_list_of_dicts.append(new_entry)

    write_to_file(category, master_list, is_test)
    print('file written')


def scrape_page(url_string):
    content_table = []
    content_row = []
    try:
        page = urlopen(url_string)
    except:
        print("error opening URL")
        return
    soup = BeautifulSoup(page, 'html.parser')
    content = soup.find('div', {"class": "mobile-table"})

    for row in content.findAll('tr'):
        for item in row.children:
            if item != '\n':
                content_row.append(item.string)
        #escape apostraphes (sic?)
        for item in content_row:
            if item:
                if "'" in item:
                    item.replace("'","\\\'")
        content_table.append(tuple(content_row))
        content_row.clear()
    return content_table

if __name__=="__main__":
    run()
