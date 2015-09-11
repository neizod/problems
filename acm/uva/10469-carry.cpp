#include <iostream>
using namespace std;


int main(void) {
    while (!cin.eof()) {
        int n, m;
        cin >> n;
        if (cin.eof()) {
            break;
        }
        cin >> m;
        cout << (n ^ m) << endl;
    }
    return 0;
}
