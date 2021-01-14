import sys
import math
from collections import deque

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.popleft() 

        for neighbour in graph[s]:

            if neighbour in ei:
                graph[s].remove(neighbour)
                return s, neighbour

            elif neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]

graph_dict = {}
visited = []
queue = deque()

for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]

    if n1 not in graph_dict.keys():
        graph_dict[n1] = [n2]
    else:
        graph_dict[n1].append(n2)
    
    if n2 not in graph_dict.keys():
        graph_dict[n2] = [n1]
    else:
        graph_dict[n2].append(n1) 

ei = [int(input()) for i in range(e)]

# game loop
while True:
    si = int(input())  # The index of the node on which the Skynet agent is positioned this turn


    # Example: 0 1 are the indices of the nodes you wish to sever the link between
    # print("0 1")

    i,j = bfs(visited, graph_dict, si)
    print(i,j)
    visited.clear()
    queue.clear()