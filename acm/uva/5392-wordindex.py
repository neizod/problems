d = [' '] + [chr(97+i) for i in range(26)]

def get(text):
    '''get the encode number of valid text'''
    global d
    i = 1
    c = [0, 0, 0, 0, 0]

    while i <= 83681:
        c[4] += 1
        if c[4] > 26:
            c[3] += 1
            c[4] = c[3] + 1
        if c[3] > 25:
            c[2] += 1
            c[3] = c[2] + 1
            c[4] = c[3] + 1
        if c[2] > 24:
            c[1] += 1
            c[2] = c[1] + 1
            c[3] = c[2] + 1
            c[4] = c[3] + 1
        if c[1] > 23:
            c[0] += 1
            c[1] = c[0] + 1
            c[2] = c[1] + 1
            c[3] = c[2] + 1
            c[4] = c[3] + 1

        word = ''
        for j in range(5):
            word += d[c[j]]
        if text == word:
            return i
        i += 1

def pattern(text):
    '''check if the text are in correct pattern'''
    if len(text) > 5:
        return False
    chk = True
    for i in range(len(text) - 1):
        if ord(text[i]) >= ord(text[i+1]):
            chk = False
    return chk

################################################################################

import re

while True:
    try:
        raw = input()
    except EOFError:
        break

    raw = re.sub('\r|\n', '', raw)
    if not pattern(raw):
        ## return 0 on invalid text ##
        print(0)
        continue

    raw = ' '*(5-len(raw)) + raw
    print(get(raw))
