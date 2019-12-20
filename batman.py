import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]

maxX = w
minX = 0
maxY = 0
minY = h

# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    if (bomb_dir == "U" ):   #?(Up)
        minY = y0
        y0 = (minY + maxY)/2
        
    if (bomb_dir == "UR" ):   #?(Up-Right)
        minX = x0
        x0 = (minX + maxX)/2
        minY = y0
        y0 = (minY + maxY)/2

    if (bomb_dir == "R" ):   #?(Right)
        minX = x0
        x0 = (minX + maxX)/2

    if (bomb_dir == "DR" ):   #?(Down-Right)
        minX = x0
        x0 = (minX + maxX)/2
        maxY = y0
        y0 = (minY + maxY)/2

    if (bomb_dir == "D" ):   #?(Down)
        maxY = y0
        y0 = (minY + maxY)/2

    if (bomb_dir == "DL" ):   #?(Down-Left)
        maxX = x0
        x0 = (minX + maxX)/2
        maxY = y0
        y0 = (minY + maxY)/2

    if (bomb_dir == "L" ):   #?(Left)
        maxX = x0
        x0 = (minX + maxX)/2

    if (bomb_dir == "UL" ):   #?(Up-Left)
        maxX = x0
        x0 = (minX + maxX)/2
        minY = y0
        y0 = (minY + maxY)/2

    print ("%d %d" % (x0, y0))
    #cambios
