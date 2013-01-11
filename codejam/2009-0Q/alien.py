import re

word_len, word_dict, sample = [int(n) for n in input().split()]
alien_dict = [input() for word in range(word_dict)]

for test in range(sample):
    alien_regex = input().replace('(','[').replace(')',']')
    alien_match = sum(1 for word in alien_dict if re.match(alien_regex, word))
    print('Case #{}: {}'.format(test+1, alien_match))

