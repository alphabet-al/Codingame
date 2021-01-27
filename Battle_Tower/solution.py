def cord(graph, exit_list, edges):
    
    while True:
        inv_edge = []
        temp = []

        for i in edges:
            if i[0] not in exit_list and i[1] not in exit_list:
                inv_edge.append(i)

        for i in inv_edge:
            # print(i)
            for j in i:
                temp.append(j)
      
        if len(temp) != 0:
            # print(inv_edge)
            mci = max(temp, key = temp.count)
            exit_list.append(mci)
        else:
            break

    return exit_list

def de_exit(graph):
    exit_list = []

    for k,v in graph.items():

        if len(v) == 0:
            exit_list.append(k)

        elif len(v) == 1:
            if v[0] not in exit_list:
                exit_list.append(v[0])
                

    return exit_list

def find_exit_per(edges, exit_list):
    count = 0
    for i in edges:
            if i[0] in exit_list and i[1] in exit_list:
                print(i)
                count += 1
    print(count)
         

def find_edges(graph):
    edges = []

    for k,v in graph.items():
        for i in v:
            edges.append((k,i))

    return edges

def calc(graph, edges):

    exit_list = de_exit(graph)
    exit_list = cord(graph, exit_list, edges)
    # find_exit_per(edges, exit_list)

    return len(exit_list)

if __name__ == "__main__":
    data = r'C:\Users\alanv\PythonCode\Projects\Codingame\Battle_Tower\input9.txt'

    with open(data, 'r') as f:
        graph = {i.split()[0]:i.split()[2:] for i in f.read().split('\n')}
 
    edges = find_edges(graph)
    num_exit = calc(graph, edges)
    print(num_exit)