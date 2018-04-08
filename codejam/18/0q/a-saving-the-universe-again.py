#!/usr/bin/env python3


def make_attack_group(instructions):
    ls = [0]
    for inst in instructions:
        if inst == 'S':
            ls[-1] += 1
        else:
            ls += [0]
    return ls


def min_swap(shield, instructions):
    attack_group = make_attack_group(instructions)
    if sum(attack_group) > shield:
        return -1
    damage = sum(x*2**i for i, x in enumerate(attack_group))
    time_swap = 0
    while damage > shield:
        if attack_group[-1] == 0:
            attack_group.pop()
        else:
            time_swap += 1
            attack_group[-1] -= 1
            attack_group[-2] += 1
            damage -= 2**(len(attack_group)-2)
    return time_swap



def main():
    for case in range(int(input())):
        raw_shield, instructions = input().split()
        shield = int(raw_shield)
        answer = min_swap(shield, instructions)
        if answer == -1:
            answer = 'IMPOSSIBLE'
        print('Case #{}: {}'.format(case+1, answer))


if __name__ == '__main__':
    main()
