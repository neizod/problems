#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;


int main(void) {
    while (true) {
        long double n, p;
        cin >> n;
        cin >> p;
        if (cin.eof()) {
            break;
        }
        cout << setprecision(0) << fixed << exp(log(p)/n) << endl;
    }
    return 0;
}
