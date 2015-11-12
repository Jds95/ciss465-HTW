#!/usr/bin/env python3
#---------------------------------------------------------------------
# CISS465 Project 3 - Jesse and Nate
#---------------------------------------------------------------------

CAVE_NUMBERS = 20

import cgi
import random
import Cave

def cave_generation(cave_list, cave_list_copy):
    
    # List containing all the Locations for caves
    point_list = []

    for i in range (CAVE_NUMBERS):
        point_list.append(i + 1)

    # Loop to add caves to cave_list
    for i in range (CAVE_NUMBERS):
        cave = Cave.Cave()
        cave_list.append(cave)
        
    # Loop to go through cave_list and assign it a random value from
    # the point_list, then removes that value from the point_list
    for i in range (CAVE_NUMBERS):
        cave_list[i].set_value(random.choice(point_list))
        point_list.remove(cave_list[i].get_value())
        
    cave_list_copy = cave_list[:]
            
    # Set up connections for the caves
    for i in range(3):
        for item in cave_list:
            if (item not in cave_list_copy):
                continue
            item_copy = item
            if (item in cave_list_copy):
                cave_list_copy.remove(item)
                random_cave = random.choice(cave_list_copy)
                item_copy.add_connection(random_cave.get_value())
                random_cave.add_connection(item_copy.get_value())
                if (random_cave in cave_list_copy):
                    cave_list_copy.remove(random_cave)

        cave_list_copy = cave_list[:]

def pit_generation(cave_list):
    pit_generate = random.sample(cave_list, 2)
    
    for item in cave_list:
        if (item in pit_generate):
            item.set_pit(True)

def bat_generation(cave_list, cave_list_copy):
    cave_list_copy = cave_list[:]
    for item in cave_list_copy:
        if (item.get_pit == True):
            cave_list_copy.remove(item)
    
    bat_generate = random.sample(cave_list_copy, 2)
    
    for item in cave_list:
        if (item in bat_generate):
            item.set_bat(True)

def wumpus_generation(cave_list, cave_list_copy):
    cave_list_copy = cave_list[:]
    for item in cave_list_copy:
        if (item.get_pit == True or item.get_bat == True):
            cave_list_copy.remove(item)
    
    wumpus_generate = random.sample(cave_list_copy, 1)

    for item in cave_list:
        if (item in wumpus_generate):
            item.set_wumpus(True)
            
   
# List containing all the Caves
cave_list = []
cave_check = []
cave_list_copy = []


# Function calls to generate the game
cave_generation(cave_list, cave_list_copy)
pit_generation(cave_list)
bat_generation(cave_list, cave_list_copy)
wumpus_generation(cave_list, cave_list_copy)

# Test print to see Cave Objects Values/(other variabes in the future)
print('Content-Type: text/html')
print()
print('<html><body>')
for item in cave_list:
    print(item)
    print('<br />')
print('</body></html>')

