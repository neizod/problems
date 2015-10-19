#include <iostream>
#include <algorithm>
using namespace std;


int ages[2000000];


int main(void) {
    while (true) {
        long no_peoples;
        cin >> no_peoples;
        if (no_peoples == 0) {
            break;
        }
        for (int i=0; i<no_peoples; i++) {
            cin >> ages[i];
        }
        sort(ages, ages+no_peoples);
        for (int i=0; i<no_peoples; i++) {
            cout << ages[i];
            if (i+1 != no_peoples) {
                cout << " ";
            }
        }
        cout << endl;
    }
    return 0;
}
