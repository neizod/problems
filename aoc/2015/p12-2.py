#!/usr/bin/env python3

import json


def gather_sum(data):
    if isinstance(data, int):
        return data
    if isinstance(data, list):
        return sum(gather_sum(field) for field in data)
    if isinstance(data, dict):
        if 'red' not in data.values():
            return sum(gather_sum(field) for field in data.values())
    return 0


def main():
    filename = input().strip()
    data = json.load(open(filename))
    print(gather_sum(data))


if __name__ == '__main__':
    main()
