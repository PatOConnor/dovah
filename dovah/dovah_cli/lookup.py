from .skyrimdata.skyrimcommands import skyrim_commands
from .skyrimdata.skyrimavs import skyrim_avs
from .skyrimdata.skyrimenchantments import skyrim_enchantments
from .skyrimdata.skyrimitems import skyrim_items
from .skyrimdata.skyrimnpcs import skyrim_npcs
from .skyrimdata.skyrimperks import skyrim_perks
from .skyrimdata.skyrimquests import skyrim_quests
from .skyrimdata.skyrimspells import skyrim_spells
from .skyrimdata.skyrimweather import skyrim_weather
from .skyrimdata.skyrimskills import skyrim_skills
from .skyrimdata.skyrimalchemy import ingredients, effects
from .skyrimdata.skyrimlocations import skyrim_locations

class Lookup:
    #this class is not designed to have objects made of it
    #this is for dependency injection while testing
    def __init__(self):
        pass

    #returns the text to add to a command based on the 
    #picks the first string that matches
    def lookup(lookupstr, category):
        catalog = Lookup.catalog_reference(category)
        #check if it matches the name of a catalog entry
        for k in catalog:
            if catalog[k]['NAME'].lower().strip() == lookupstr.lower().strip():
                lookup_item = catalog[k]
        category = category.lower().strip()
        if category in ['alcheffect', 'alcheffects', 'av', 'avs', 'attribute', 'attributes', 
                        'ench', 'enchant', 'enchantment', 'enchantments', 'ingr', 'ingredient', 
                        'ingredients', 'item', 'items', 'loc', 'location', 'locations', 'perk', 
                        'perks', 'quests', 'quests', 'spell', 'spells', 'weather']:
            return lookup_item['CODE']
        elif category in ['fac', 'faction', 'factions']:
            return lookup_item['INFO']['Form ID']
        elif category in ['npc', 'npcs']:
            return lookup_item['REF_ID']


        

    #returns the key of the item that has the argument string in the first element
    def catalog_lookup(lookupstr, category):
        catalog = DovahLookup.catalog_reference(category)
        #first, check if it itself is a number and continue on if it is not
        try:
            lookupstr = int(lookupstr)
            if lookupstr in skyrim_commands:
                return lookupstr
            else:
                return -1
        except ValueError:
            pass
        #nif not a number, check if it matches the name of a catalog entry
        for k in catalog:
            if catalog[k]['NAME'].lower().strip() == lookupstr.lower().strip():
                return k
        return -1

    def catalog_reference(category):
        if category == 'commands':
            targetdict = skyrim_commands
        elif category == 'av':
            targetdict = skyrim_avs
        elif category == 'enchantments':
            targetdict = skyrim_enchantments
        elif category == 'item':
            targetdict = skyrim_items
        elif category == 'npc':
            targetdict = skyrim_npcs
        elif category == 'perk':
            targetdict = skyrim_perks
        elif category == 'quest':
            targetdict = skyrim_quests
        elif category == 'spell':
            targetdict = skyrim_spells
        elif category == 'weather':
            targetdict = skyrim_weather
        elif category == 'skill':
            targetdict = skyrim_skills
        elif category == 'ingredients':
            targetdict = ingredients
        elif category == 'effects':
            targetdict = effects
        elif category == 'locations':
            targetdict = skyrim_locations
        else:
            raise ValueError
        return targetdict

    #small user text interface
    def user_lookup(category): 
        #grabs dictionary to pick through
        catalog = DovahLookup.self.cmd_maker.add_cmd(['additem', 'player', 'f', 1])#number inputted as a numbercatalog_reference(category)
        while (True):
            start_str = input("Enter the first letters of the desired "+category+": ")
            for i in catalog:
                if catalog[i][0].lower().startswith(start_str):
                    print(i, catalog[i])
            word = input('which one is being added? ')
            k = DovahLookup.catalog_lookup()
            if k != -1:
                return catalog[k]

   
