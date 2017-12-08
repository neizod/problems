#include <iostream>
#include <algorithm>
using namespace std;


string substract(string &s, string value, string signature, string full) {
    string digits = "";
    while (s.find(signature) != string::npos) {
        for (auto c : full) {
            if (c == 0) { break; }
            s.erase(s.find(c),1);
        }
        digits += value;
    }
    return digits;
}


string find_tel(string s) {
    string tel = "";
    tel += substract(s, "0", "Z", "ZERO");
    tel += substract(s, "2", "W", "TWO");
    tel += substract(s, "4", "U", "FOUR");
    tel += substract(s, "6", "X", "SIX");
    tel += substract(s, "8", "G", "EIGHT");
    tel += substract(s, "1", "O", "ONE");
    tel += substract(s, "3", "T", "THREE");
    tel += substract(s, "5", "F", "FIVE");
    tel += substract(s, "7", "S", "SEVEN");
    tel += substract(s, "9", "N", "NINE");
    sort(tel.begin(), tel.end());
    return tel;
}


int main(void) {
    int n;
    cin >> n;
    for (int i=0; i<n; i++) {
        string s;
        cin >> s;
        cout << "Case #" << i+1 << ": " << find_tel(s) << endl;
    }
    return 0;
}
