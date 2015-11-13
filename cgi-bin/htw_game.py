#!/usr/bin/env python3
#---------------------------------------------------------------------
# CISS465 Project 3 - Jesse and Nate
#---------------------------------------------------------------------

CAVE_NUMBERS = 20

import cgi
import random
import Cave
import Player

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

    # Set up inital dual way connections
    for i, item in enumerate(cave_list):
        item.add_connection(cave_list[(i + 1) % CAVE_NUMBERS].get_value())
        cave_list[(i + 1) % CAVE_NUMBERS].add_connection(item.get_value())
        
    # Set up final connections for caves
    for i, item in enumerate(cave_list):
        if item not in cave_list_copy:
            continue
        item.add_connection(cave_list[(i + 2) % CAVE_NUMBERS].get_value())
        cave_list[(i + 2) % CAVE_NUMBERS].add_connection(item.get_value())
        cave_list_copy.remove(cave_list[(i + 2) % CAVE_NUMBERS])
        cave_list_copy.remove(item)
    
# Function to generate random pits
def pit_generation(cave_list):
    pit_generate = random.sample(cave_list, 2)
    
    for item in cave_list:
        if (item in pit_generate):
            item.set_pit(True)

# Function to generate random bats
def bat_generation(cave_list, cave_list_copy):
    cave_list_copy = cave_list[:]
    for item in cave_list_copy:
        if (item.get_pit == True):
            cave_list_copy.remove(item)
    
    bat_generate = random.sample(cave_list_copy, 2)
    
    for item in cave_list:
        if (item in bat_generate):
            item.set_bat(True)

# Function to generate wumpus location
def wumpus_generation(cave_list, cave_list_copy):
    cave_list_copy = cave_list[:]
    for item in cave_list_copy:
        if (item.get_pit == True or item.get_bat == True):
            cave_list_copy.remove(item)
    
    wumpus_generate = random.sample(cave_list_copy, 1)

    for item in cave_list:
        if (item in wumpus_generate):
            item.set_wumpus(True)
# Function to set player room to a safe room     
def player_start(cave_list, spawn_list):  
    for item in cave_list:
        if (item.get_pit() == False and item.get_bat() == False
            and item.get_wumpus() == False):
            spawn_list.append(item)
    
    spawn_room = random.choice(spawn_list)
    Player.set_room(spawn_room.get_value())

# Function to return the routes the player can travel from current room
def get_player_route(Player, cave_list):
    
    for item in cave_list:
        if (item.get_value() == Player.get_room()):
            return item.get_connection()

    
# List containing all the Caves
cave_list = []
cave_check = []
cave_list_copy = []
spawn_list = []

# Create Player Variable/Object
Player = Player.Player()


# Function calls to generate the game and player
cave_generation(cave_list, cave_list_copy)
pit_generation(cave_list)
bat_generation(cave_list, cave_list_copy)
wumpus_generation(cave_list, cave_list_copy)
player_start(cave_list, spawn_list)

for item in cave_list:
    print(item)

"""
# Game done variable
done = False

print('\n', "If at anytime you wish to quit, type quit or q\n")

# Game Loop
while (done == False):
    # Variable to store what rooms the player can connect to
    room_connection = get_player_route(Player, cave_list)
    print("You are in Room:", Player.get_room(), end=" ")
    print("You can travel to:", room_connection)
   
    print("You can shoot an arrow or move: ")
    # Gather user input if moving or shooting
    decision=input("Which would you like to do?: ")
    print()
    if (decision.lower() == "quit" or decision == "q"):
        done = True
    # If choice was to move, get input
    if (decision.lower() == "move" or decision == "m"):
         user_input = int(input("Which room would you like to travel to? "))
         # check to see if user input was a correct room to travel
         if (user_input not in room_connection):
             continue
         # Set Player's current room to user input
         Player.clear_room()
         Player.set_room(user_input)
    
    if (decision.lower() == "shoot" or decision == "s"):
        print("No shooting function coded yet")


        
# Test print to see Cave Objects Values/(other variabes in the future)
print('Content-Type: text/html')
print()
print('<html><body>')
for item in cave_list:
    print(item)
    print('<br />')
print('</body></html>')

"""
