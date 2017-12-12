#!/usr/bin/env python3


def valid_no_contain(vector):
    return not {*(ord(c)-97 for c in 'iol')} & {*vector}


def valid_repeat(vector):
    count = 0
    skip = False
    for a, b in zip(vector, vector[1:]):
        if skip:
            skip = False
        elif a == b:
            count += 1
            skip = True
    return count >= 2


def valid_increasing(vector):
    for c, b, a in zip(vector, vector[1:], vector[2:]):
        if 1 <= b < 25 and a+1 == b == c-1:
            return True
    return False


def valid(vector):
    return valid_no_contain(vector) and valid_repeat(vector) and valid_increasing(vector)


def get_value(vector):
    return sum(v*26**i for i, v in enumerate(vector))


def get_vector(value):
    vector = []
    while value:
        vector += [value%26]
        value //= 26
    return vector


def fast_skip(value):
    vector = get_vector(value)
    for i, v in reversed(list(enumerate(vector))):
        if v in {ord(i)-97 for i in 'iol'}:
            vector[i] += 1
            vector[:i] = [0]*len(vector[:i])
            break
    return vector


def increment(vector):
    value = get_value(vector)
    value += 1
    return fast_skip(value)


def create(password):
    vector = increment([ord(c)-97 for c in reversed(password)])
    while not valid(vector):
        vector = increment(vector)
    return ''.join(chr(v+97) for v in reversed(vector))


def main():
    password = input().strip()
    password = create(password)
    print(create(password))


if __name__ == '__main__':
    main()
