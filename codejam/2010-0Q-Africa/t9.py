dict_t9 = { 'a': '2', 'b': '22', 'c': '222',
            'd': '3', 'e': '33', 'f': '333',
            'g': '4', 'h': '44', 'i': '444',
            'j': '5', 'k': '55', 'l': '555',
            'm': '6', 'n': '66', 'o': '666',
            'p': '7', 'q': '77', 'r': '777', 's': '7777',
            't': '8', 'u': '88', 'v': '888',
            'w': '9', 'x': '99', 'y': '999', 'z': '9999',
            ' ': '0' }

for test in range(int(input())):
    word = input()

    press = ''
    for c in word:
        if len(press) and press[-1] == dict_t9[c][0]:
            press += ' '
        press += dict_t9[c]

    print('Case #{}: {}'.format(test+1, press))
