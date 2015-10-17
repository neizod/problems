#!/usr/bin/env python3


def single_line(hour, line):
    if hour == 0 and line == 0:
        return 1
    hour -= 1
    new_line = line % 2**hour
    return (2 if line == new_line else 1) * single_line(hour, new_line)


def bf_count(hour, lower, upper):
    return sum(single_line(hour, line) for line in range(lower, upper))


def dq_count(hour, lower, upper):
    if lower == upper:
        return 0
    if lower == 0 and upper == 2**hour:
        return 3**hour
    hour -= 1
    lower_lower = min(lower, 2**hour)
    lower_upper = min(upper, 2**hour)
    upper_lower = max(lower, 2**hour) - 2**hour
    upper_upper = max(upper, 2**hour) - 2**hour
    lower_part = dq_count(hour, lower_lower, lower_upper)
    upper_part = dq_count(hour, upper_lower, upper_upper)
    return 2 * lower_part + upper_part


def test_assert(n):
    for i in range(n):
        for j in range(2**i):
            for k in range(j+1, 2**i+1):
                assert dq_count(i, j, k) == bf_count(i, j, k)


def measure_time(hour, lower, upper):
    from time import time
    t = time()
    bf_count(hour, lower, upper);
    print("bf: {:.3f} mili-seconds".format(1000*(time()-t)))
    t = time()
    dq_count(hour, lower, upper);
    print("dq: {:.3f} mili-seconds".format(1000*(time()-t)))


def main():
    for case in range(int(input())):
        hour, lower, upper = [int(n) for n in input().split()]
        print("Case {}: {}".format(case+1, dq_count(hour, lower-1, upper)))


if __name__ == '__main__':
    main()
