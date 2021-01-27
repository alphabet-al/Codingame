def dfs(visited, graph, node, exit_list, pre_dfs, start_node):
    if node not in pre_dfs:
        pre_dfs.append(node)
    if node not in visited:
        visited.append(node)
        for neighbor in graph[node]:
            dfs(visited, graph, neighbor, exit_list, pre_dfs, start_node)
        pre_dfs.pop()
        if len(pre_dfs) != 0:
            parent = pre_dfs[-1]
        if node not in exit_list and node != start_node:
            if node in graph[parent]:
                if parent not in exit_list:
                    exit_list.append(parent)
            else:
                exit_list.append(node)
        elif node not in exit_list and len(graph[node]) == 0:
            exit_list.append(node)

def calc(graph):
    visited = []
    exit_list = []
    pre_dfs = []
 
    node = list(graph.keys())[0] 
    start_node = node
    dfs(visited, graph, node, exit_list, pre_dfs, start_node)

    return len(exit_list)

if __name__ == "__main__":
    data = r'C:\Users\alanv\PythonCode\Projects\Codingame\Battle_Tower\input10.txt'

    with open(data, 'r') as f:
        graph = {i.split()[0]:i.split()[2:] for i in f.read().split('\n')}
    
    num_exit = calc(graph)
    print(num_exit)