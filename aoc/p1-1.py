#!/usr/bin/env python3


digits = input()
print(sum(int(a) for a, b in zip(digits, digits[1:]+digits[:1]) if a == b))
