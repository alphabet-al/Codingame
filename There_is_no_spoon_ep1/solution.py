def check_right(grid, x, y):
    x2 = x + 1
    y2 = y

    if x2 > width - 1:
        return -1, -1
    elif grid[y2][x2] == '0':
        return x2, y2
    else:
        x2, y2 = check_right(grid, x2, y2)
    
    return x2, y2

def check_down(grid, x, y):
    x3 = x
    y3 = y + 1

    if y3 > height - 1:
        return -1, -1
    elif grid[y3][x3] == '0':
        return x3, y3
    else:
        x3, y3 = check_down(grid, x3, y3)
    
    return x3, y3

width = int(3)  # the number of cells on the X axis
height = int(3)  # the number of cells on the Y axis
grid = [['0', '.', '0'], ['.', '.', '.'], ['0', '.', '0']]

for i in range(height):
    for j in range(width):
        if grid[i][j] == '0':
            x1, y1 = j, i
            x2, y2 = check_right(grid, j, i)
            x3, y3 = check_down(grid, j, i)

            print(x1, y1, x2, y2, x3, y3)


# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)


# Three coordinates: a node, its right neighbor, its bottom neighbor
# print("0 0 1 0 0 1")
