from bs4 import BeautifulSoup
from urllib.request import urlopen
import os

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
    elif category == 'npcs':
        scrape_all(category, 28)
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
    print('categories are items, perks, npcs, spells, avs, quests, enchantments, weather')
    return input('enter item type to gather: ').lower().strip()

def get_all_tables():
    print('items')
    scrape_all('items', 88)
    print('npcs')
    scrape_all('npcs', 28)
    print('enchantments')
    scrape_all('enchantments', 10)
    for c in ['perks', 'quests', 'spells', 'avs', 'weather']:
        print(c)
        scrape_all(c)

#returns massive dictionary of all the data of a given category
def scrape_all(category, bound=None):
    main_url = 'http://www.skyrimcommands.com/'+category+'/'
    value_table = list()
    value_table.append(scrape_page(main_url))
    print('added page 1')
    #bounds: items list has 88 pages, npcs has 28
    #        enchantments has 10, the rest have 1
    if(bound):
        for i in range(2,bound):#88 is the max
            current_url = main_url+str(i)+'/'
            current_page = scrape_page(current_url)
            if current_page != None:
                value_table.append(current_page)
                print('added page '+str(i))
        print('pages added to table')
    #these few lines combine the pages into one list and convert to dictionary
    master_list = []
    for pages in value_table:
        master_list.extend(pages)
    print(master_list)
    write_to_file(category, master_list)
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


#this writes the data to the file of the associated category
def write_to_file(category, data):
    dirname = os.path.dirname(__file__)
    print
    if is_test:
        filename = os.path.join(dirname, "tests\skyrim"+category+".py")
    else:
        dirname = dirname[:-14]#go to the previous folder
        filename = os.path.join(dirname, "skyrimdata\skyrim"+category+".py")
    file = open(filename, 'w', encoding="utf-8")
    i = 0
    file.write('skyrim_'+category+' = {\n')
    for item in data:  #this writes it in python dictionary syntax
        file.write('\t'+str(i)+':'+str(item)+',\n')
        i += 1
    file.write('\t}')
    file.close()


if __name__=="__main__":
    run()
