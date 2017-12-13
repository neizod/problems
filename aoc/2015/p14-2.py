#!/usr/bin/env python3

import re


class Deer(object):
    def __init__(self, name, speed, go_time, rest_time):
        self.name = name
        self.speed = speed
        self.go_time = go_time
        self.rest_time = rest_time
        self.point = 0
        self.distant = 0
        self.power = self.go_time
        self.rest = self.rest_time

    def go_forward(self):
        if self.power > 0:
            self.distant += self.speed
            self.power -= 1
        else:
            self.rest -= 1
        if self.rest == 0:
            self.power = self.go_time
            self.rest = self.rest_time
        return self.distant


def main():
    try:
        deers = []
        while True:
            name, *raw_numbers = re.findall(r'(\w+) .* (\d+) .* (\d+) .* (\d+)', input())[0]
            speed, go_time, rest_time = [int(n) for n in raw_numbers]
            deers += [Deer(name, speed, go_time, rest_time)]
    except EOFError:
        time = 2503
        for _ in range(time):
            distant = max(deer.go_forward() for deer in deers)
            for deer in deers:
                if deer.distant == distant:
                    deer.point += 1
        print(max(deer.point for deer in deers))


if __name__ == '__main__':
    main()
