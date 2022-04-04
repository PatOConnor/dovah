from bs4 import BeautifulSoup
#from bs4.element import NavigableString
from urllib.request import urlopen
import sqlite3
from sqlite3 import Error

def run():
    #go through tables on webpage to get data
    #and store in a dict
    effect_list = []
    url = 'https://en.uesp.net/wiki/Skyrim:Alchemy_Effects'
    try:
        page = urlopen(url)
    except:
        print("error opening URL")
        return
    soup = BeautifulSoup(page, 'html.parser')
    tables = soup.findAll('table')
    effect_table = tables[-1]
    effect_rows = effect_table.findAll('tr')
    for effect in effect_rows[1::]:
        i = 0 #i know this looks grotesque but this context doesnt support indexing with brackets
        for cell in effect:
            if i==1: #name of the effect, ID code
                [name, code] = cell.text.split('\n')
                code = code.lstrip('(').rstrip(')')
            elif i==3: #ingredients that provide the effect
                links = cell.findAll('a')
                ingr = []
                for link in links:
                    if link.string and link.string not in ['DG', 'HF', 'DB', 'CC']:
                        ingr.append(link.string)
            elif i==5: #Description of the effect
                desc = cell.string
            elif i==7:
                base_cost = cell.string
                if base_cost == '(?)':
                    base_cost = 0#no data on wiki
            elif i==9:
                base_magnitude = cell.string
                if base_magnitude == '(?)':
                    base_magnitude = 0
                base_dur = cell.string
                if base_dur == '(?)':
                    base_dur = 0
            elif i==13:
                value = cell.string
            i+=1


        #this bit gets replaced with SQL

        
        effect_entry = {'NAME':name, 'CODE':code, 'INGR':ingr, 'BASE_COST':float(base_cost), 'base_magnitude':float(base_magnitude), 'BASE_DUR':float(base_dur), 'VALUE':float(value)}
        effect_list.append(effect_entry)
    
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def create_table ####this is the part where i realized i need to organize the data itself first


if __name__=='__main__':
    run()
