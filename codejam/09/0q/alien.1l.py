import re

exit(next('\n'.join('Case #{}: {}'.format(test+1, ''.join(str(len([1 for word in alien_dict if re.match(re.sub('\(|\)', (lambda c: chr((ord(c.group())<<1)+11)), alien_input), word) is not None])) for alien_input in [input()])) for test in range(sample)) for alien_dict, sample in [(lambda args: [[input() for word in range(args[1])], args[2]])([int(val) for val in input().split()])]))
