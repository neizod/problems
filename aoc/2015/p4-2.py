#!/usr/bin/env python3

from itertools import count
from hashlib import md5


def find_nonce(key):
    for nonce in count():
        code = md5('{}{}'.format(key, nonce).encode()).hexdigest()
        if {*code[:6]} == {'0'}:
            return nonce


def main():
    print(find_nonce(input().strip()))


if __name__ == '__main__':
    main()
