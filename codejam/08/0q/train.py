def days_min(time_str):
    hh, mm = [int(t) for t in time_str.split(':')]
    return 60 * hh + mm

def dep_arr(time_table, turn_around):
    dep, arr = [days_min(t) for t in time_table.split()]
    return [dep, arr+turn_around]

def make_chain(trip, table):
    for i, togo in enumerate(table):
        if trip[-1] <= togo[0]:
            trip.extend(table.pop(i))
            return True
    return False

def make_trip(tables, trips, flag=0):
    if tables[0] > tables[1]:
        flag ^= 1

    if tables[flag]:
        trip = tables[flag].pop(0)
        switch = 1
        while make_chain(trip, tables[flag^switch]):
            switch ^= 1
        trips[flag].append(trip)
    else:
        while tables[flag^1]:
            trips[flag^1].append(tables[flag^1].pop())

def make_schedual(a, b):
    tables = [a, b]
    trips = [[] for _ in range(2)]
    while any(tables):
        make_trip(tables, trips)
    return trips

def testcase(test_no):
    turn_around = int(input())
    a, b = [int(n) for n in input().split()]
    a = sorted(dep_arr(input(), turn_around) for _ in range(a))
    b = sorted(dep_arr(input(), turn_around) for _ in range(b))

    a, b = make_schedual(a, b)
    return len(a), len(b)

def main():
    for case in range(int(input())):
        output = test(case)
        print('Case #{}: {} {}'.format(case+1, *output))

if __name__ == '__main__':
    main()

