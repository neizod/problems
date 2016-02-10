#!/usr/bin/env python3


def isqrt(n):
    if n == 0:
        return 0
    x = 2 ** sum(divmod(n.bit_length(), 2))
    while True:
        y = x + n // x
        y //= 2
        if y >= x:
            return x
        x = y


def triangle_number(n):
    return n * (n + 1) // 2


def find_seq(position):
    size = isqrt(2 * position)
    while triangle_number(size) < position:
        size += 1
    size -= 1
    return position - triangle_number(size)


def main():
    print(find_seq(int(input())))


if __name__ == '__main__':
    main()
