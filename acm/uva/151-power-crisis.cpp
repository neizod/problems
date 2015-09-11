#include <iostream>
using namespace std;


bool all_blackout(int size, bool regions[]) {
    for (int i=0; i<size; i++) {
        if (!regions[i]) {
            return false;
        }
    }
    return true;
}


int blackout_cycle(int n) {
    int m = 1;
    while (true) {
        bool regions[n] = { false };
        int current = 0;
        regions[current] = true;
        while (!regions[12]) {
            int next = m;
            while (next) {
                current += 1;
                current %= n;
                if (!regions[current]) {
                    next -= 1;
                }
            }
            regions[current] = true;
        }
        if (all_blackout(n, regions)) {
            break;
        }
        m += 1;
    }
    return m;
}


int main(void) {
    int n;
    while (true) {
        cin >> n;
        if (n == 0) {
            break;
        }
        cout << blackout_cycle(n) << endl;
    }
    return 0;
}
