#!/usr/bin/env python3

def make_signature(unicorns, mixs):
    return ''.join(color*amount for amount, color in unicorns+mixs)


def check_validity(answer, signature):
    if sorted(answer) != sorted(signature):
        return False
    for pair in zip(answer, answer[-1]+answer[:-1]):
        if any(set(pair) <= set(invalid) for invalid in ['ROV', 'YGO', 'BVG']):
            return False
    return True


def cancel_mix_color(unicorns, mixs):
    unicorns[2][0] -= mixs[0][0]
    unicorns[0][0] -= mixs[1][0]
    unicorns[1][0] -= mixs[2][0]


def create_mix_colors(mixs):
    mix_o = 'BO'*mixs[0][0]
    mix_g = 'RG'*mixs[1][0]
    mix_v = 'YV'*mixs[2][0]
    return mix_o, mix_g, mix_v


def simple_combination(unicorns):
    unicorns.sort()
    combination = ''
    if any(unicorn[0] < 0 for unicorn in unicorns):
        return combination
    n_intersect = unicorns[0][0] + unicorns[1][0] - unicorns[2][0]
    for _ in range(unicorns[0][0]-n_intersect):
        combination += unicorns[0][1] + unicorns[2][1]
    for _ in range(n_intersect):
        combination += unicorns[0][1] + unicorns[1][1] + unicorns[2][1]
    for _ in range(unicorns[1][0]-n_intersect):
        combination += unicorns[1][1] + unicorns[2][1]
    return combination


def mix_combination(combination, mixs):
    for mix in create_mix_colors(mixs):
        if mix:
            if mix[0] not in combination:
                combination += mix
            else:
                combination = combination.replace(mix[0], mix+mix[0], 1)
    return combination


def stable_combination(unicorns, mixs):
    signature = make_signature(unicorns, mixs)
    cancel_mix_color(unicorns, mixs)
    intermediet = simple_combination(unicorns)
    answer = mix_combination(intermediet, mixs)
    if check_validity(answer, signature):
        return answer
    else:
        return 'IMPOSSIBLE'


def main():
    for case in range(int(input())):
        _, nr, no, ny, ng, nb, nv = [int(n) for n in input().split()]
        answer = stable_combination( [[nr, 'R'], [ny, 'Y'], [nb, 'B']],
                                     [[no, 'O'], [ng, 'G'], [nv, 'V']] )
        print('Case #{}: {}'.format(case+1, answer))


if __name__ == '__main__':
    main()
