def move(val, cr, cc):

    if val == '^':
        cr = cr - 1
    elif val == '>':
        cc = cc + 1
    elif val == '<':
        cc = cc - 1
    elif val == 'v':
        cr = cr + 1

    return cr, cc

def traverse(map, r, c, visited):
    count = 0
    cr, cc = r, c

    if (cr,cc) not in visited:
        visited.add((cr,cc))
    else:
        return float('inf')

    try:
        val = map[cr][cc]
    except IndexError:
        return float('inf')

    if val == 'T':
        count += 1
        return count
    
    if val in ['^', '>', '<', 'v']:
        count += 1

    cr, cc = move(val, cr, cc)
    count += traverse(map, cr, cc, visited)
    
    return count

def find_min_path(mdict):

    min_path_val = min(list(mdict.values()))

    if min_path_val == float('inf'):
        return 'TRAP'
    
    for k,v in mdict.items():
            if v == min_path_val:
                ans = k

    return ans


if __name__ == "__main__":
    data = r'C:\Users\alanv\PythonCode\Projects\Codingame\Dungeons_and_Maps\input.txt'

    with open(data, 'r') as f:
        w, h = [int(i) for i in f.readline().split()]
        r, c = [int(i) for i in f.readline().split()] # start row and start column
        n = int(f.readline())
        map = []
        visited = set()
        map_counts = {}
        
        for i in range(n):
        
            for j in range(h):
                map.append(f.readline().strip('\n'))
            
            map_counts[i] = traverse(map, r, c, visited)
            map.clear()
            visited.clear()
        
        print(find_min_path(map_counts))