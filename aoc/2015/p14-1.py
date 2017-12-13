#!/usr/bin/env python3

import re


class Deer(object):
    def __init__(self, name, speed, go_time, rest_time):
        self.name = name
        self.speed = speed
        self.go_time = go_time
        self.rest_time = rest_time

    def distance(self, time):
        full, partial = divmod(time, self.go_time+self.rest_time)
        return (full*self.go_time + min(partial, self.go_time)) * self.speed


def main():
    try:
        deers = []
        while True:
            name, *raw_numbers = re.findall(r'(\w+) .+ (\d+) .+ (\d+) .+ (\d+)', input())[0]
            speed, go_time, rest_time = [int(n) for n in raw_numbers]
            deers += [Deer(name, speed, go_time, rest_time)]
    except EOFError:
        time = 2503
        print(max(deer.distance(time) for deer in deers))


if __name__ == '__main__':
    main()
