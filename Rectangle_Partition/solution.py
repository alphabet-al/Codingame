w, h, count_x, count_y = [int(i) for i in input().split()]
x = [0,w]
y = [0,h]

for i in input().split():
    x.append(int(i))
for i in input().split():
    y.append(int(i))

x.sort(reverse=True)
y.sort(reverse=True)

xlst = []
ylst = []

for i in range(len(x)):
    for j in range(i+1, len(x)):
        xlst.append(x[i] - x[j])

for i in range(len(y)):
    for j in range(i+1, len(y)):
        ylst.append(y[i] - y[j])

xset = set(xlst)
yset = set(ylst)

z = xset.intersection(yset)

count = 0

for i in z:
    if i in xlst and i in ylst:
        count += xlst.count(i) * ylst.count(i)

print(count)

