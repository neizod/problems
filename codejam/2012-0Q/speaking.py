def conv_char(c):
    if 'a' <= c <= 'z':
        return 'yhesocvxduiglbkrztnwjpfmaq'[ord(c)-97]
    return c

def test(case):
    return ''.join(conv_char(c) for c in input())

def main():
    for case in range(int(input())):
        output = test(case)
        print('Case #{}: {}'.format(case+1, output))

if __name__ == '__main__':
    main()

