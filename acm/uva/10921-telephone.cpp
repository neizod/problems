#include <iostream>
using namespace std;


char get_digit(char ch) {
    int f1 = (ch - 'A') / 3;
    int f2 = (ch - 'A' - 1) / 3;
    if (0 <= f1 && f1 <= 5) {
        return '2' + f1;
    } else if (5 <= f2 && f2 <= 7) {
        return '2' + f2;
    } else if (ch == 'Z') {
        return '9';
    } else {
        return ch;
    }
}


string find_telephone(string memo_phrase) {
    string tel_number;
    for (char ch : memo_phrase) {
        tel_number += get_digit(ch);
    }
    return tel_number;
}


int main(void) {
    while (true) {
        string memo_phrase;
        cin >> memo_phrase;
        if (cin.eof()) {
            break;
        }
        cout << find_telephone(memo_phrase) << endl;
    }
    return 0;
}
