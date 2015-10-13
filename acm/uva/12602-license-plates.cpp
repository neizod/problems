#include <iostream>
#include <cmath>
using namespace std;


int base_converter(int base, char start, string repr) {
    int value = 0;
    for (int i=0; i<repr.size(); i++) {
        value += (repr[repr.size()-i-1]-start) * (int)pow(base, i);
    }
    return value;
}


int b26(string repr) {
    return base_converter(26, 'A', repr);
}


int b10(string repr) {
    return base_converter(10, '0', repr);
}


bool nice(string plate) {
    return abs(b26(plate.substr(0, 3)) - b10(plate.substr(4, 4))) <= 100;
}


int main(void) {
    int test;
    cin >> test;
    for (int i=0; i<test; i++) {
        string plate;
        cin >> plate;
        cout << (nice(plate) ? "nice" : "not nice") << endl;
    }
    return 0;
}
