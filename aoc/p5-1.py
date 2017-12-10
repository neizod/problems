#!/usr/bin/env python3

ls = []
try:
    while True:
        ls += [int(input())]
except EOFError:
    pass


n = 0
c = 0
while 0 <= n < len(ls):
    ls[n] += 1
    n += ls[n] - 1
    c += 1
print(c)
