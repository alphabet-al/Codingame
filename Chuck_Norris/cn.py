import re

message = input()

res = ''.join(format(i, 'b').zfill(7) for i in bytearray(message, encoding ='utf-8'))
lst = re.split(r'(?<=0)(?=1)|(?<=1)(?=0)', res)
final_lst = []

for i in lst:
    if '1' in i:
        final_lst.append('0')
        final_lst.append(len(i)*'0')
    elif '0' in i:
        final_lst.append('00')
        final_lst.append(len(i)*'0')

print(' '.join(final_lst))