import re

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
md = {}

for i in range(n):
    ext, mt = input().split()
    md[ext.lower()] = mt

for i in range(q):
    fname = re.findall(r'(?<=\.)\w+$', input())  # One file name per line.
  
    if len(fname) == 0:
        print('UNKNOWN')

    elif fname[0].lower() in md.keys():
        print(md[fname[0].lower()])

    else:
        print('UNKNOWN')
