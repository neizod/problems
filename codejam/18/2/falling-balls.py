#!/usr/bin/env python3


def get_destination(last_row):
    nudge = 0
    destination = [None for _ in last_row]
    for index, size in enumerate(last_row):
        destination[nudge:nudge+size] = [index] * size
        nudge += size
    return destination


def get_table(last_row):
    if last_row[0] == 0 or last_row[-1] == 0:
        return []
    table = []
    destination = get_destination(last_row)
    count = [1 for _ in last_row]
    while count != last_row:
        next_destination = [None for _ in last_row]
        row = ''
        for index, dest in enumerate(destination):
            if dest is not None and index > dest:
                count[index] -= 1
                count[index-1] += 1
                next_destination[index-1] = dest
                row += '/'
            elif dest is not None and index < dest:
                count[index] -= 1
                count[index+1] += 1
                next_destination[index+1] = dest
                row += '\\'
            else:
                next_destination[index] = dest
                row += '.'
            destination = next_destination
        table += [row]
    table += ['.'*len(last_row)]
    return table


def main():
    for case in range(int(input())):
        input()
        last_row = [int(n) for n in input().split()]
        answer = get_table(last_row)
        feasible = 'IMPOSSIBLE' if not answer else len(answer)
        print('Case #{}: {}'.format(case+1, feasible))
        for line in answer:
            print(line)


if __name__ == '__main__':
    main()
