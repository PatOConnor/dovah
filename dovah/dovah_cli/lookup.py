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
    catalog = catalog_reference(category)
    while (True):
        start_str = input("Enter the first letters of the desired "+category+": ")
        for i in catalog:
            if catalog[i][0].lower().startswith(start_str):
                print(i, catalog[i])
        word = input('which one is being added? ')
        k = catalog_lookup
        if k != -1:
            return catalog[k]

#returns the key of the item that has the argument string in the first element
def catalog_lookup(lookupstr, category):
    catalog = catalog_reference(category)
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
    for k in skyrim_commands:
        if skyrim_commands[k]['NAME'].lower().strip() == lookupstr.lower().strip():
            return k
    return -1
