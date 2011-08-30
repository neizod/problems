import re
import math

raw = input()
scene = int(raw)

for i in range(scene):
    raw = input()
    raw = re.split('\W+', raw)
    size = int(raw[0]) * int(raw[1])

    ## this is mathematics approch, try it yourself and observe! ##
    if size%2 == 1:
        size = size - 1 + math.sqrt(2)

    ## print the answer ##
    print('Scenario #{}'.format(i+1))
    print('{:.2f}'.format(size))
    print()
