#include <iostream>
#include <bitset>
#include <string>
using namespace std;


int sum(string bin_str) {
    int counter = 0;
    for (char c : bin_str) {
        counter += c - '0';
    }
    return counter;
}


string as_bin_str(int number) {
    return bitset<16>(number).to_string();
}


int as_dec(string str) {
    return stoi(str, nullptr, 10);
}


int as_hex(string str) {
    return stoi(str, nullptr, 16);
}


void testcase() {
    string str;
    cin >> str;
    cout << sum(as_bin_str(as_dec(str))) << " ";
    cout << sum(as_bin_str(as_hex(str))) << endl;
}


int main(void) {
    int test;
    cin >> test;
    for (int i=0; i<test; i++) {
        testcase();
    }
    return 0;
}
