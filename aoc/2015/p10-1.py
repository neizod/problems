#!/usr/bin/env python3


def look_and_say(digits):
    output = ''
    count = 0
    prev = None
    for digit in digits:
        if prev is None:
            prev = digit
            count = 1
        elif prev == digit:
            count += 1
        else:
            output += str(count) + prev
            prev = digit
            count = 1
    output += str(count) + prev
    return output


def main():
    digits = input().strip()
    for _ in range(40):
        digits = look_and_say(digits)
    print(len(digits))


if __name__ == '__main__':
    main()
