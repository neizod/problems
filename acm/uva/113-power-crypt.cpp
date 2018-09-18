#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;


int main(void) {
    long double n, p;
    while (cin >> n >> p) {
        cout << setprecision(0) << fixed << exp(log(p)/n) << endl;
    }
    return 0;
}
