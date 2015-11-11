#---------------------------------------------------------------------
# CISS465 Project 3 - Jesse and Nate
#---------------------------------------------------------------------

CAVE_NUMBERS = 20

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
            
   
# List containing all the Caves
cave_list = []
cave_check = []
cave_list_copy = []

cave_generation(cave_list, cave_list_copy)

print("Cave List Print")
# Test print to see Cave Objects Values/(other variabes in the future)
for item in cave_list:
    print(item)
