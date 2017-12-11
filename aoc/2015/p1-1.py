#!/usr/bin/env python3

from collections import Counter


counter = Counter(input())
print(counter['('] - counter[')'])
