from collections import deque

def normal_war(ns, ks):
    c = 0
    while ns:
        n = ns.pop()
        if ks[-1] < n:
            ks.pop(0)
            c += 1
        else:
            i = 0
            while n > ks[i]:
                i += 1
            ks.pop(i)
    return c

def deceitful_war(ns, ks):
    while any(n < k for n, k in zip(ns, ks)):
        ns.popleft() and ks.pop()
    return len(ns)

for case in range(int(input())):
    _ = input()
    ns = sorted(float(n) for n in input().split())
    ks = sorted(float(n) for n in input().split())
    dw_answer = deceitful_war(deque(ns), deque(ks))
    nw_answer = normal_war(ns[:], ks[:])
    print('Case #{}: {} {}'.format(case+1, dw_answer, nw_answer))
