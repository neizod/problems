#!/usr/bin/env python3


def represent(code):
    return '{!r}'.format(code).replace('"', r'\"')


def string(code):
    return eval(code)


def main():
    try:
        codes = []
        while True:
            codes += [input()]
    except EOFError:
        print(sum(len(represent(code)) - len(code) for code in codes))


if __name__ == '__main__':
    main()
