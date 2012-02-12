import re

word_len, word_dict, sample = [int(val) for val in input().split()]
alien_dict = [input() for word in range(word_dict)]

for test in range(sample):
    alien_regex = re.sub('\(|\)', (lambda c: chr((ord(c.group())<<1)+11)), input())
    alien_match = len([1 for word in alien_dict if re.match(alien_regex, word) != None])
    print('Case #{}: {}'.format(test+1, alien_match))
