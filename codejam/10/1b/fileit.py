def cd(path, cwd, count=0):
    for dir in path:
        if dir not in cwd:
            count += 1
        cwd = cwd.setdefault(dir, {})
    return count

def test(case):
    exist, mkdir = [int(val) for val in input().split()]
    root = {}
    for path in range(exist):
        cd(input().split('/')[1:], root)
    return sum(cd(input().split('/')[1:], root) for path in range(mkdir))

def main():
    for case in range(int(input())):
        output = test(case)
        print('Case #{}: {}'.format(case+1, output))

if __name__ == '__main__':
    main()

