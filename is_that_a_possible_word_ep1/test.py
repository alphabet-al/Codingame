
_input = ['a', 'b', 'c', 'd']
states = ['A', 'B', 'C']
t={}
for i in range(6):
    tr = ['A', 'a', 'B'], ['B', 'c', 'C'], ['C', 'a', 'C'], ['C', 'b', 'C'], ['C', 'c', 'C'], ['C', 'd', 'C']
    t[tr[i][0]+tr[i][1]] = tr[i][2]
ss = 'A'
es = 'C'

for i in range(1):
    w = 'ab'
    c = ss
    for s in w:
        try:
            c = t[c+s]
        except:
            c="!"
    print("true" if c in es else "false")