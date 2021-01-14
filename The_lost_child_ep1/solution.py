from collections import deque

def search(x,y):
    frontier.append((x, y))
    solution[x,y] = x,y

    while len(frontier) > 0:          # exit while loop when frontier queue equals zero
        x, y = frontier.popleft()     # pop next entry in the frontier queue an assign to x and y location

        if(x - 1, y) in path and (x - 1, y) not in visited:  # check the cell on the left
            cell = (x - 1, y)
            solution[cell] = x, y    # backtracking routine [cell] is the previous cell. x, y is the current cell
            frontier.append(cell)   # add cell to frontier list
            visited.add((x-1, y))  # add cell to visited list

        if (x, y - 1) in path and (x, y - 1) not in visited:  # check the cell down
            cell = (x, y - 1)
            solution[cell] = x, y
            frontier.append(cell)
            visited.add((x, y - 1))

        if(x + 1, y) in path and (x + 1, y) not in visited:   # check the cell on the  right
            cell = (x + 1, y)
            solution[cell] = x, y
            frontier.append(cell)
            visited.add((x +1, y))

        if(x, y + 1) in path and (x, y + 1) not in visited:  # check the cell up
            cell = (x, y + 1)
            solution[cell] = x, y
            frontier.append(cell)
            visited.add((x, y + 1))


def backRoute(x, y, count):
    while (x, y) != (start_x, start_y):    # stop loop when current cells == start cell
        x, y = solution[x, y]               # "key value" now becomes the new key
        count += 10
    return count


# map = [input() for i in range(10)]
map =  ['..........',
        'M#........',
        '#C##......',
        '..........',
        '..........',
        '..........',
        '..........',
        '..........',
        '..........',
        '..........']

walls = []
path = []
visited = set()
frontier = deque()
solution = {}
count = 0

for y,i in enumerate(map):
    for x,j in enumerate(i):
        
        if j == '.' or j == 'M':
            path.append((x,y))
        
        if j == 'M':
            end_x, end_y = x, y
    
        if j == '#':
            walls.append((x,y))
        
        if j == 'C':
            start_x, start_y = x, y


search(start_x, start_y)
count = backRoute(end_x, end_y, count)
print('{}km'.format(count))
