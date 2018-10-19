#!/usr/bin/env python3


def alt_quote():
    while True:
        yield '``'
        yield "''"


def main():
    lines = []
    try:
        while True:
            lines += [input(), '\n']
    except EOFError:
        pass
    it_quote = alt_quote()
    it_string = iter(''.join(lines).split('"'))
    print(next(it_string), end='')
    for string in it_string:
        print(next(it_quote), end='')
        print(string, end='')


if __name__ == '__main__':
    main()
