#!/usr/bin/env python3


def string(code):
    return eval(code)


def main():
    try:
        codes = []
        while True:
            codes += [input()]
    except EOFError:
        print(sum(len(code) - len(string(code)) for code in codes))


if __name__ == '__main__':
    main()
