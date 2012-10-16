def cd(path, mkdir_count=False):
    global root, count
    cwd = root

    for dir in path:
        if dir not in cwd:
            if mkdir_count:
                count += 1
            cwd[dir] = {}
        cwd = cwd[dir]

##############################################################################

for test in range(int(input())):
    exist, mkdir = [int(val) for val in input().split()]

    root = {}    
    for path in range(exist):
        cd(input().split('/')[1:])

    count = 0
    for path in range(mkdir):
        cd(input().split('/')[1:], True)

    print('Case #{}: {}'.format(test+1, count))
