#include <iostream>
using namespace std;


int main(void) {
    int n, m;
    while (cin >> n >> m) {
        cout << (n ^ m) << endl;
    }
    return 0;
}
