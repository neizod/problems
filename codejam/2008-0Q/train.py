def dep_arr(time_table):
    return [days_min(t) for t in time_table.split()]

def days_min(time_str):
    hh, mm = [int(t) for t in time_str.split(':')]
    return 60 * hh + mm

def make_chain(trip, togo_table, turnaround):
    for i, togo in enumerate(togo_table):
        if trip[-1] + turnaround <= togo[0]:
            trip.extend(togo_table.pop(i))
            return True
    return False

def make_trip(table_a, table_b, trip_a, trip_b, turnaround):
    if table_a and table_b:
        if table_a[0] < table_b[0]:
            trip = table_a.pop(0)
            flag = 1
            togo_table = table_b
            while make_chain(trip, togo_table, turnaround):
                flag ^= 1
                togo_table = table_b if flag else table_a
            trip_a.append(trip)
        else:
            trip = table_b.pop(0)
            flag = 0
            togo_table = table_a
            while make_chain(trip, togo_table, turnaround):
                flag ^= 1
                togo_table = table_b if flag else table_a
            trip_b.append(trip)
    elif not table_a:
        trip_b.append(table_b.pop())
    elif not table_b:
        trip_a.append(table_a.pop())

def make_schedual(table_a, table_b):
    trip_a = []
    trip_b = []
    while any([table_a, table_b]):
        make_trip(table_a, table_b, trip_a, trip_b, turnaround)
    return trip_a, trip_b

for test in range(int(input())):
    turnaround = int(input())
    a, b = [int(n) for n in input().split()]

    table_a = sorted(dep_arr(input()) for _ in range(a))
    table_b = sorted(dep_arr(input()) for _ in range(b))

    a, b = make_schedual(table_a, table_b)

    print('Case #{}: {} {}'.format(test+1, len(a), len(b)))

