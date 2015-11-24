# Class for Adventure/Player
class Player:
    # Constructor sets the arrows, boolean for arrows, and room location
    def __init__(self):
        self.__arrows = 5
        self.__has_arrows = True
        self.__room_location = [0]
        
    # Function to set the player's room passed in by variable
    def set_room(self, room):
        self.__room_location[0]= room

    def clear_room(self):
        self.__room_location = [0]

    # Function to return the room_location
    def get_room(self):
        return self.__room_location[0]

    def set_arrows(self, arrow):
        self.__arrows = arrow

	# Function to decrement player arrow, and check boolean for has_arrows
    def lose_arrow(self):
        if (self.__arrows > 0):
            self.__arrows -= 1
        if (self.__arrows == 0):
            self.__has_arrows = False

    # Function to add player arrows
    def gain_arrow(self):
        if (self.__arrows < 5):
            self.__arrows += 1

    # Fucntion to check if player has arrows
    def arrow_check(self):
        return self.__has_arrows

    # Player proliferation producer
    def playerCopyCreator(self):
        rep = str(self.__arrows)
        rep += '.'
        rep += str(self.__has_arrows)
        rep += '.'
        rep += str(self.__room_location[0])
        return rep

    # Default print statement
    def __str__(self):
        rep = "Player Status: "
        rep += "Arrows: "
        rep += str(self.__arrows)
        rep += " Room Location: "
        rep += str(self.__room_location)
        return rep
