# one-liner version
exit('\n'.join('Case #{}: {}'.format(t+1, ''.join(d[c] for d in [dict(zip('abcdefghijklmnopqrstuvwxyz ', 'yhesocvxduiglbkrztnwjpfmaq '))] for c in input())) for t in range(int(input()))))
