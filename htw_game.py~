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
# Cave Variables initialized to 0
Cave1 = 0
Cave2 = 0
Cave3 = 0
Cave4 = 0
Cave5 = 0
Cave6 = 0
Cave7 = 0
Cave8 = 0
Cave9 = 0
Cave10 = 0
Cave11 = 0
Cave12 = 0
Cave13 = 0
Cave14 = 0
Cave15 = 0
Cave16 = 0
Cave17 = 0
Cave18 = 0
Cave19 = 0
Cave20 = 0

point_list = [POINT1, POINT2, POINT3, POINT4, POINT5, POINT6, POINT7, POINT8,
              POINT9, POINT10, POINT11, POINT12, POINT13, POINT14, POINT15,
              POINT16, POINT17, POINT18, POINT19, POINT20]

cave_list = [Cave1, Cave2, Cave3, Cave4, Cave5, Cave6, Cave7, Cave8, Cave9,
             Cave10, Cave11, Cave12, Cave13, Cave14, Cave15, Cave16, Cave17,
             Cave18, Cave19, Cave20]

for i in range(0, 20, 1):
    cave_list[i] = random.choice(point_list)
    print("Cave", i, "Value: ", cave_list[i])
    point_list.remove(cave_list[i])

print(cave_list)
print(point_list)
