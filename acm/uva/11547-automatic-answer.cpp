#include <iostream>
using namespace std;


int calc_skill(int number) {
    return abs((((number * 567) / 9 + 7492) * 235 / 47 - 498) / 10 % 10);
}


int main(void) {
    int test;
    cin >> test;
    for (int i=0; i<test; i++) {
        int number;
        cin >> number;
        cout << calc_skill(number) << endl;
    }
    return 0;
}
