#include <iostream>
#include <iomanip>
#include <unordered_map>
using namespace std;


unordered_map<char,int> init_map(int no_lines) {
    unordered_map<char,int> char_val;
    for (int j=0; j<no_lines; j++) {
        char ch;
        int val;
        cin >> ch >> val;
        char_val.insert(make_pair(ch, val));
    }
    return char_val;
}


int calc_paid(unordered_map<char,int> char_val, int no_lines) {
    int cents = 0;
    while (no_lines >= 0) {
        char ch;
        cin.get(ch);
        if (ch == '\n') {
            no_lines -= 1;
        } else {
            unordered_map<char,int>::iterator got = char_val.find(ch);
            if (got != char_val.end()) {
                cents += got->second;
            }
        }
    }
    return cents;
}


void testcase() {
    int no_lines;
    cin >> no_lines;
    unordered_map<char,int> char_val = init_map(no_lines);
    cin >> no_lines;
    int cents = calc_paid(char_val, no_lines);
    cout << fixed << setprecision(2) << cents/100.0 << "$" << endl;
}


int main(void) {
    int test;
    cin >> test;
    for (int i=0; i<test; i++) {
        testcase();
    }
    return 0;
}
