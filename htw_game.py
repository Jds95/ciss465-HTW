#---------------------------------------------------------------------
# CISS465 Project 3 - Jesse and Nate
#---------------------------------------------------------------------

import random
# Variable locations according to dodecahedron picture in files
POINT1 = 1
POINT2 = 2
POINT3 = 3
POINT4 = 4
POINT5 = 5
POINT6 = 6
POINT7 = 7
POINT8 = 8
POINT9 = 9
POINT10 = 10
POINT11 = 11
POINT12 = 12
POINT13 = 13
POINT14 = 14
POINT15 = 15
POINT16 = 16
POINT17 = 17
POINT18 = 18
POINT19 = 19
POINT20 = 20
class Cave:
    def __init__(self):
        self.__value = 0

    def set_value(self, number):
        self.__value = number

    def get_value(self):
        return self.__value
# Cave Variables initialized to 0
Cave1 = Cave()
Cave2 = Cave()
Cave3 = Cave()
Cave4 = Cave()
Cave5 = Cave()
Cave6 = Cave()
Cave7 = Cave()
Cave8 = Cave()
Cave9 = Cave()
Cave10 = Cave()
Cave11 = Cave()
Cave12 = Cave()
Cave13 = Cave()
Cave14 = Cave()
Cave15 = Cave()
Cave16 = Cave()
Cave17 = Cave()
Cave18 = Cave()
Cave19 = Cave()
Cave20 = Cave()

point_list = [POINT1, POINT2, POINT3, POINT4, POINT5, POINT6, POINT7, POINT8,
              POINT9, POINT10, POINT11, POINT12, POINT13, POINT14, POINT15,
              POINT16, POINT17, POINT18, POINT19, POINT20]

cave_list = [Cave1, Cave2, Cave3, Cave4, Cave5, Cave6, Cave7, Cave8, Cave9,
             Cave10, Cave11, Cave12, Cave13, Cave14, Cave15, Cave16, Cave17,
             Cave18, Cave19, Cave20]

for i in range(0, 20, 1):
    cave_list[i].set_value(random.choice(point_list))
    point_list.remove(cave_list[i].get_value())


for i in range(0, 20, 1):
    print("Cave", i, "Value:", cave_list[i].get_value())
