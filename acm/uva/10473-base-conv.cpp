#include <iostream>
#include <iomanip>
#include <string>
using namespace std;


void dec_to_hex(string str) {
    cout << hex << uppercase << "0x" << stoi(str, nullptr, 10) << endl;
}


void hex_to_dec(string str) {
    cout << dec << stoi(str.substr(2), nullptr, 16) << endl;
}


bool is_hex(string str) {
    return str.substr(0, 2).compare("0x") == 0;
}


int main(void) {
    while (true) {
        string str;
        cin >> str;
        if (str[0] == '-') {
            break;
        }
        (is_hex(str) ? hex_to_dec : dec_to_hex)(str);
    }
    return 0;
}
