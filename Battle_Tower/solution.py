
# n = 10
# input = ['1 1 2',
#          '2 2 1 3',
#          '3 2 2 4',
#          '4 2 3 5',
#          '5 2 4 6',
#          '6 2 5 7',
#          '7 2 6 8',
#          '8 2 7 9',
#          '9 2 8 10',
#          '10 1 9']

n = 48
input = ['1 1 44',
         '2 7 3 15 21 23 31 33 42',
         '3 1 2',
         '4 1 7',
         '5 1 32',
         '6 4 12 19 29 43',
         '7 5 4 11 13 33 37',
         '8 1 13',
         '9 1 38',
         '10 1 13',
         '11 3 7 14 27',
         '12 1 6',
         '13 6 7 8 10 16 35 36',
         '14 1 11',
         '15 1 2',
         '16 1 13',
         '17 1 26',
         '18 1 38',
         '19 6 6 26 32 33 38 44',
         '20 1 26',
         '21 1 2',
         '22 1 32',
         '23 1 2',
         '24 1 44',
         '25 1 38',
         '26 5 17 19 20 30 48',
         '27 1 11',
         '28 1 32',
         '29 1 6',
         '30 1 26',
         '31 1 2',
         '32 6 5 19 22 28 40 47',
         '33 3 2 7 19',
         '34 1 38',
         '35 1 13',
         '36 1 13',
         '37 1 7',
         '38 6 9 18 19 25 34 45',
         '39 1 42',
         '40 1 32',
         '41 1 44',
         '42 3 2 39 46',
         '43 1 6',
         '44 4 1 19 24 41',
         '45 1 38',
         '46 1 42',
         '47 1 32',
         '48 1 26']

graph = {}         
exit_set = set()

for i in input:
    line = i.split()
    graph[line[0]] = line[2:]


for k,v in graph.items():

    if len(v) == 0:
        exit_set.add(k)
        
    # print(k,v)

    if k not in exit_set:
        for j in v:
            # print(j)
            if j not in exit_set:
                exit_set.add(j)
                break

print(exit_set)
ext_dict = {}
value_list = []



for k,v in graph.items():
    # print(v)
    z = exit_set.intersection(set(v))
    # print(k,z)
    ext_dict[k] = z

for i in ext_dict.values():
    for j in i:
        value_list.append(j)

print(value_list)
print(ext_dict)

for k,v in ext_dict.items():
    # print(k,v)
    if len(v) > 1:
        for i in v:
            # print(i)
            if value_list.count(i) == 1:
                # print(value_list.count(i))
                # print(exit_list)
                exit_set.remove(i)
print(exit_set)
print(len(exit_set))