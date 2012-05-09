import re

# one-liner version
next('\n'.join('Case #{}: {}'.format(t+1, ''.join(str(len([1 for word in alien_dict if re.match(re.sub('\(|\)', (lambda c: chr((ord(c.group())<<1)+11)), alien_input), word) is not None])) for alien_input in [input()])) for t in range(sample)) for alien_dict, sample in [(lambda args: [[input() for word in range(args[1])], args[2]])([int(val) for val in input().split()])])

###############################################################################


word_len, word_dict, sample = [int(val) for val in input().split()]
alien_dict = [input() for word in range(word_dict)]

for test in range(sample):
    alien_regex = re.sub('\(|\)', (lambda c: chr((ord(c.group())<<1)+11)), input())
    alien_match = len([1 for word in alien_dict if re.match(alien_regex, word) is not None])
    print('Case #{}: {}'.format(test+1, alien_match))
