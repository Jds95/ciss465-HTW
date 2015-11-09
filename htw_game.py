#---------------------------------------------------------------------
# CISS465 Project 3 - Jesse and Nate
#---------------------------------------------------------------------

CAVE_NUMBERS = 20

import random
import Cave

# List containing all the Locations for caves
point_list = []

for i in range (CAVE_NUMBERS):
    point_list.append(i + 1)

# List containing all the Caves
cave_list = []

# Loop to add caves to cave_list
for i in range (CAVE_NUMBERS):
    cave = Cave.Cave()
    cave_list.append(cave)

# Loop to go through cave_list and assign it a random value from
# the point_list, then removes that value from the point_list
for i in range (CAVE_NUMBERS):
    cave_list[i].set_value(random.choice(point_list))
    point_list.remove(cave_list[i].get_value())

# Test print to see Cave Objects Values/(other variabes in the future)
for item in cave_list:
    print(item)
    
