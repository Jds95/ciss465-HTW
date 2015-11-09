#---------------------------------------------------------------------
# CISS465 Project 3 - Jesse and Nate
#---------------------------------------------------------------------

CAVE_NUMBERS = 20

import random

# Class for Caves
class Cave:
    # Constructor sets the value(location of cave to 0 or NULL)
    def __init__(self):
        self.__value = 0
    # Function to set Cave location to value
    def set_value(self, number):
        self.__value = number
    # Return value as in "You are in Cave: " Cave.get_value()
    def get_value(self):
        return self.__value
    # Set the connections between the rooms via chart
    def set_connection(self, list):
        self.__connection =[]
        for item in list:
            self.__connection.append(item)
    def get_connection(self):
        return self.__connection



# List containing all the Locations for caves
point_list = []

for i in range (CAVE_NUMBERS):
    point_list.append(i + 1)

# List containing all the Caves
cave_list = []

for i in range (CAVE_NUMBERS):
    cave = Cave()
    cave_list.append(cave)

# Loop to go through cave_list and assign it a random value from
# the point_list, then removes that value from the point_list
for i in range (CAVE_NUMBERS):
    cave_list[i].set_value(random.choice(point_list))
    point_list.remove(cave_list[i].get_value())

# Test print to see Cave Objects Values/(other variabes in the future)
for i in range(CAVE_NUMBERS):
    print("Cave", i + 1, "Value:", cave_list[i].get_value())
    
