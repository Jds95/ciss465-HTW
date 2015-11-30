#!/usr/bin/env python3
#---------------------------------------------------------------------
# CISS465 Project 3 - Jesse and Nate
#---------------------------------------------------------------------

CAVE_NUMBERS = 20

import cgi
import random
import Cave
import Player
import os
import http.cookies

form = cgi.FieldStorage()

cookie_string = os.environ.get('HTTP_COOKIE')

if cookie_string == '':
    output = "I don't see a cookie."
else:
    cookie = http.cookies.SimpleCookie()
    cookie.load(cookie_string)

def caveCopier(cave_list, morsel):
	cave = Cave.Cave()
	x = morsel.split(".")
	cave.set_value(int(x[0]))

    # Converts cave string into list of elements
	x[1] = x[1].lstrip('[')
	x[1] = x[1].rstrip(']')
	x[1] = x[1].replace(' ', '')
	x[1] = x[1].split(',')
	cave.add_connection(int(x[1][0]))
	cave.add_connection(int(x[1][1]))
	cave.add_connection(int(x[1][2]))
	
	if x[2][0] == 'T':
		cave.set_pit(True)
	else:
		cave.set_pit(False)
	
	if x[3][0] == 'T':
		cave.set_bat(True)
	else:
		cave.set_bat(False)

	if x[4][0] == 'T':
		cave.set_wumpus(True)
	else:
		cave.set_wumpus(False)
	
	cave_list.append(cave)


def playerCopier(Player, morsel):
	x = morsel.split(".")
	Player.set_arrows(int(x[0]))
	
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
        if item in pit_generate:
            item.set_pit(True)

# Function to generate random bats
def bat_generation(cave_list, cave_list_copy):
    cave_list_copy = cave_list[:]
    for item in cave_list_copy:
        if item.get_pit == True:
            cave_list_copy.remove(item)
    
    bat_generate = random.sample(cave_list_copy, 2)
    
    for item in cave_list:
        if item in bat_generate:
            item.set_bat(True)

# Function to generate wumpus location
def wumpus_generation(cave_list, cave_list_copy):
    cave_list_copy = cave_list[:]
    for item in cave_list_copy:
        if item.get_pit == True or item.get_bat == True:
            cave_list_copy.remove(item)
    
    wumpus_generate = random.sample(cave_list_copy, 1)

    for item in cave_list:
        if item in wumpus_generate:
            item.set_wumpus(True)
            
# Function to set player room to a safe room     
def player_start(cave_list, spawn_list):  
    for item in cave_list:
        if item.get_pit() == False and item.get_bat() == False and item.get_wumpus() == False:
            spawn_list.append(item)
    
    spawn_room = random.choice(spawn_list)
    Player.set_room(spawn_room.get_value())

# Function to return the routes the player can travel from current room
def get_player_route(Player, cave_list):   
    for item in cave_list:
        if item.get_value() == Player.get_room():
            return item.get_connection()


# Function to check if arrow shot by player has proper pathing
def valid_arrow_shot(Player, cave_list, shoot_list, done):
    arrow_path = []
    arrow_room = 0
    arrow_room += Player.get_room()
    # Loop to run through length of shoot list
    for i in range(len(shoot_list)):
        for item in cave_list:
            # Boolean to grab room connections for arrow
            if arrow_room == item.get_value():
                arrow_path = item.get_connection()
        # Boolean to see if arrow shot was correct
        if shoot_list[i] not in arrow_path:
            print("Shot failed")
            return False
        else:
            arrow_room = shoot_list[i]
            print("Shot succeeded")

    # Check if Wumpus was shot by arrow
    for item in cave_list:
        if item.get_wumpus():
            if shoot_list[-(len(shoot_list))] == item.get_value():
                print("You shot the Wumpus, You win the game!")
                done = True

    return True

# Function to check surrounding player room for warning messages
def warning_message_check(Player, cave_list):
    connecting_room = []
    for item in cave_list:
        if item.get_value() == Player.get_room():
            connecting_room = item.get_connection()

    for i in range(len(connecting_room)):
        for item in cave_list:
            if item.get_value() == connecting_room[i]:
                if item.get_pit():
                    item.pit_warning()
                if item.get_bat():
                    item.bat_warning()
                if item.get_wumpus():
                    item.wumpus_warning()

# Function to check if player went into room with pit/wumpus
def game_over_check(Player, cave_list):
    for item in cave_list:
        if item.get_value() == Player.get_room():
            if item.get_pit():
                print("You triggered a pit, game over")
                return True
            if item.get_wumpus():
                print("You got eaten by the Wumpus, game over")
                return True

    return False

# Function to check to see if teleport by bats was triggered
def teleport_check(Player, cave_list):
    for item in cave_list:
        if Player.get_room() == item.get_value():
            if item.get_bat:
                item_copy = item
                copy_cave = cave_list[:]
                copy_cave.remove(item)
                random_cave = random.sample(copy_cave)
                Player.set_room(random_cave.get_value())
                copy_cave.append(item_copy)


# List containing all the Caves
cave_list = []

for i in range(CAVE_NUMBERS):
	caveCopier(cave_list, cookie[str(i)].value)

Player = Player.Player()
cave_check = []
cave_list_copy = []
spawn_list = []

# Create Player Variable/Object
print("Content-Type: text/html")
print()
print("<html><body>")
print("If at anytime you wish to quit, type quit or q<br />")

# Variable to store what rooms the player can connect to
goToRoom = form.getvalue('room')
Player.set_room(int(goToRoom))
room_connection = get_player_route(Player, cave_list)
#warning_message_check(Player, cave_list)
print("You are in Room:", Player.get_room(), end="<br />")
print("You can travel to:", room_connection)

# Function calls to generate the game and player
"""cave_generation(cave_list, cave_list_copy)
pit_generation(cave_list)
bat_generation(cave_list, cave_list_copy)
wumpus_generation(cave_list, cave_list_copy)
player_start(cave_list, spawn_list)"""


# Creates list of rooms that are linked
room_connection = get_player_route(Player, cave_list)
print('\n', "If at anytime you wish to quit, type quit or q<br />")
print("""
   <br />
   <form method="get" action="/cgi-bin/htw_game.py">
        Move to room number: <input type="text" name="room">
        <input type="submit" value="Submit">
    </form> 
""")


# Storing caves as a cookie
"""for i in range(CAVE_NUMBERS):
	print(i)
	print(": ")
	cookie[str(i)] = cave_list[i].caveCopyCreator()
	print(cookie[str(i)])
	print("<br />")"""

print('</body></html>')
# Storing player as a cookie
cookie['player'] = Player.playerCopyCreator()
"""print("You can shoot an arrow or move: ")
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
    teleport_check(Player, cave_list)
    if game_over_check(Player, cave_list):
        break
        
    # If choice was to shoot, gather input, valid check, game winning check
    if decision.lower() == "shoot" or decision == "s":
        shoot_list = []
        user_input = input("Enter room chain to shoot arrow: ")
        for num in user_input.split():
            shoot_list.append(int(num))
        if len(shoot_list) == 1 and shoot_list[0] == Player.get_room():
            print("You shot an arrow in current room, you pick up the arrow")
            continue
        if len(shoot_list) < 5 and len(shoot_list) > 0:
            valid_arrow_shot(Player, cave_list, shoot_list, done)
        Player.lose_arrow()
        if Player.arrow_check() == 0:
            print("Out of arrows, game over")
            done = True
"""
"""        
# Test print to see Cave Objects Values/(other variabes in the future)
print('Content-Type: text/html')
print()
print('<html><body>')
for item in cave_list:
    print(item)
    print('<br />')
print('</body></html>')
"""
