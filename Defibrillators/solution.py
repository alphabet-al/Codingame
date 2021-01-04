import sys
import math

class Defib:
    def __init__(self, name, address, phone, longit, latt):
        self.name = name
        self.address = address
        self.phone = phone
        self.longit = longit
        self.latt = latt

    def dist_from(self, lon, lat):
        x = (lon - self.longit) * math.cos((self.latt + lat)/2)
        y = (lat - self.latt)

        d = (math.sqrt((x**2) + (y**2))) * 6371

        return d

    def name(self):
        return self.name

lon = float(input().replace(',', '.'))
lat = float(input().replace(',', '.'))
n = int(input())
alpha = {}
dist_lst = []

for i in range(n):
    dsplit = input().split(';')
    alpha[dsplit[0]] = Defib(dsplit[1], dsplit[2], dsplit[3], float(dsplit[4].replace(',', '.')), float(dsplit[5].replace(',', '.')))

for i in alpha.keys():
    d = alpha[i].dist_from(lon,lat)
    dist_lst.append((i,d))

tup_min = min(dist_lst, key = lambda t: t[1])
print(alpha[tup_min[0]].name)
