#include <iostream>
using namespace std;


int fib[10000] = { 1, 1, 2 };
int size = 3;
long group_sum = 0;


pair<int,int> fib_signature(int position) {
    return make_pair(fib[position-1], fib[position-2]);
}


void init_fib() {
    while (fib_signature(size) != fib_signature(2)) {
        fib[size] = (fib[size-1] + fib[size-2]) % 100;
        size += 1;
    }
    size -= 2;
    for (int i=0; i<size; i++) {
        group_sum += fib[i];
    }
}


long sum_fib(long lower, long upper) {
    long total = 0;
    lower -= 1;
    total += group_sum * ((upper - lower) / size);
    int sign = 1;
    if (lower % size > upper % size) {
        lower ^= upper ^= lower ^= upper;
        sign = -1;
        total += group_sum;
    }
    for (int i=lower%size; i<upper%size; i++) {
        total += sign * fib[i];
    }
    return total;
}


int main(void) {
    init_fib();
    int test;
    cin >> test;
    for (int i=0; i<test; i++) {
        long lower, upper;
        cin >> lower >> upper;
        cout << sum_fib(lower, upper) << endl;
    }
    return 0;
}
