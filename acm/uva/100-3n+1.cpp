#include <iostream>
#include <algorithm>
using namespace std;


int find_cycle(int n) {
    int cycle = 1;
    while (n != 1) {
        if (n % 2 == 0) {
            n /= 2;
        } else {
            n *= 3;
            n += 1;
        }
        cycle += 1;
    }
    return cycle;
}


int find_max_cycle(int start, int stop) {
    int max_cycle = 0;
    if (start > stop) {
        start ^= stop ^= start ^= stop;
    }
    for (int number=start; number<=stop; number++) {
        max_cycle = max(max_cycle, find_cycle(number));
    }
    return max_cycle;
}


int main(void) {
    int i, j;
    while (cin >> i >> j) {
        cout << i << " " << j << " " << find_max_cycle(i, j) << endl;
    }
    return 0;
}
