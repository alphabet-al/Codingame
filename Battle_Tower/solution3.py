n = 4

data = r'C:\Users\alanv\PythonCode\Projects\Codingame\Battle_Tower\input.txt'

with open(data, 'r') as f:
    # graph = {i.split()[0]:i.split()[2:] for i in f.read().split('\n')}

    links = [None]*n # List of all links
    for i in range(n):
        links[i] = [int(j)-1 for j in f.readline().split()][2:] # Numbering is shifted to be O-based

# There are no cycles so we can transform the graph into a tree
q = [0] # a deque would probably be more efficient
while q:
    cur = q.pop(0)
    for nex in links[cur]:
        links[nex].remove(cur)
    q.extend(links[cur])

# naive recursive implementation
# for large trees, memoization or a dp approach would be necessary
def cover(start):
    if len(links[start]) == 0:
        return 0

    size_selected = 1 # if this node is selected
    for nex in links[start]:
        size_selected += cover(nex) # we add the best result for each subtree

    size_not_selected = 0 # if this node is not selected
    for nex in links[start]:
        size_not_selected += 1 # we selected every sub node
        for nexnex in links[nex]:
            size_not_selected += cover(nexnex) # and add the best result for each subsubtree

    return min(size_selected, size_not_selected)

if n == 1:
    print(1)
else:
    print(cover(0))