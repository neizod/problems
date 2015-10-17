#include <iostream>
#include <unordered_map>
using namespace std;


long pow(long base, int exponent) {
    if (exponent == 0) {
        return 1;
    }
    return (exponent % 2 == 0 ? 1 : base) * pow(base*base, exponent/2);
}


int p2(int exponent) {
    return 1 << exponent;
}


int lim_min(int hour, int number) {
    return min(number, p2(hour));
}


int lim_max(int hour, int number) {
    return max(number-p2(hour), 0);
}


long count(int hour, int lo, int hi) {
    if (lo == hi) {
        return 0;
    } else if (lo == 0 && hi == p2(hour)) {
        return pow(3, hour);
    }
    hour -= 1;
    return 2 * count(hour, lim_min(hour, lo), lim_min(hour, hi)) +
               count(hour, lim_max(hour, lo), lim_max(hour, hi));
}


int main(void) {
    int test;
    cin >> test;
    for (int i=1; i<=test; i++) {
        int hour, lower, upper;
        cin >> hour >> lower >> upper;
        lower -= 1;
        cout << "Case " << i << ": " << count(hour, lower, upper) << endl;
    }
    return 0;
}
