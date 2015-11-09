# Class for Caves
class Cave:
    # Constructor sets the value(location of cave to 0 or NULL)
    def __init__(self):
        self.__value = 0
        self.__connection =[]
    # Function to set Cave location to value
    def set_value(self, number):
        self.__value = number
    # Return value as in "You are in Cave: " Cave.get_value()
    def get_value(self):
        return self.__value
    
    # Set the connections between the rooms via chart
    def set_connection(self, list):
        for item in list:
            self.__connection.append(item)
            
    # Return the list of what it connects to
    def get_connection(self):
        return self.__connection

    # Bool check for list to see if it has 3 items for connections
    def is_connection_full(self):
        if (len(self.__connection) < 3):
            return False
        else:
            return True

    # Default print statement, can add booleans in later
    def __str__(self):
        rep = "Cave: "
        rep += str(self.__value)
        rep += " Connections: "
        rep += str(self.__connection)
        return rep
