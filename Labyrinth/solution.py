import sys
import math
from collections import deque

def bfs(x,y):
    q.append((x,y))
    sol[x,y] = x,y

    while len(q) > 0:
        x,y = q.popleft()

        if (x-1, y) in path and (x-1, y) not in vis:
            cell = (x-1, y)
            sol[cell] = x,y
            q.append(cell)
            vis.add(cell)

        if (x, y-1) in path and (x, y-1) not in vis:
            cell = (x, y-1)
            sol[cell] = x,y
            q.append(cell)
            vis.add(cell)
        
        if (x+1, y) in path and (x+1, y) not in vis:
            cell = (x+1, y)
            sol[cell] = x,y
            q.append(cell)
            vis.add(cell)

        if (x, y+1) in path and (x, y+1) not in vis:
            cell = (x, y+1)
            sol[cell] = x,y
            q.append(cell)
            vis.add(cell)

def backtrack(x,y):
    while (x,y) != (kc, kr):
        x, y = sol[x,y]



# r: number of rows.
# c: number of columns.
# a: number of rounds between the time the alarm countdown is activated and the time the alarm goes off.
r, c, a = [int(i) for i in input().split()]
q = deque()
vis = set()
sol = {}
walls = []
path = []
unknown = []

# game loop
while True:
    # kr: row where Kirk is located.
    # kc: column where Kirk is located.
    kr, kc = [int(i) for i in input().split()]

    for i in range(r):
        row = input()  # C of the characters in '#.TC?' (i.e. one line of the ASCII maze).
        for x,j in enumerate(row):
            path.clear()
            walls.clear()
            unknown.clear()

            if j == '.' or j == 'C':
                path.append((x,i))
        
            if j == 'C':
                end_x, end_y = x, i
        
            if j == '#':
                walls.append((x,i))
            
            if j == 'T':
                start_x, start_y = x, i

            if j == '?':
                unknown.append((x,i))
    print('UP')

