while True:
    try:
        print(sum(int(i) for i in input().rsplit(' ')))
    except EOFError:
        break
