#!/usr/bin/env python3


def ascending_increment(ls, lim=26):
    if not ls:
        raise ValueError('Can not increase value of the sequence furthermore.')
    if ls[-1] < lim:
        ls[-1] += 1
    else:
        ls[:-1] = ascending_increment(ls[:-1], lim-1)
        ls[-1] = ls[-2] + 1
    return ls


def as_word(code):
    return ''.join(chr(96+i) for i in code if i != 0)


def make_word_space():
    space = {}
    position = 0
    code = [0, 0, 0, 0, 0]
    try:
        while True:
            position += 1
            code = ascending_increment(code)
            space[as_word(code)] = position
    except ValueError:
        pass
    return space


def main():
    space = make_word_space()
    try:
        while True:
            print(space.get(input().strip(), 0))
    except EOFError:
        pass


if __name__ == '__main__':
    main()
