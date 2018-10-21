#!/usr/bin/env python3


def iter_divisor():
    while True:
        yield from iter([100, 10, 100, 100])


def iter_expander():
    while True:
        yield from iter(['shata', 'hajar', 'lakh', 'kuti'])


def split(number):
    parts = []
    for divisor in iter_divisor():
        number, remainder = divmod(number, divisor)
        parts += [remainder]
        if not number:
            break
    return list(reversed(parts))


def bangla(number):
    words = []
    parts = split(number)
    for expander in iter_expander():
        part = parts.pop()
        if part or not parts:
            words += [str(part)]
        if parts and (parts[-1] or expander == 'kuti'):
            words += [expander]
        if not parts:
            break
    return ' '.join(reversed(words))


def main():
    case = 1
    try:
        while True:
            print('{:>4}. {}'.format(case, bangla(int(input()))))
            case += 1
    except EOFError:
        pass


if __name__ == '__main__':
    main()
