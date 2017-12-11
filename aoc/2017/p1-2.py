#!/usr/bin/env python3


digits = input()
skip = len(digits) // 2
print(sum(int(a) for a, b in zip(digits, digits[skip:]+digits[:skip]) if a == b))
