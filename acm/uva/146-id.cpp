#include <iostream>
#include <string>
#include <algorithm>
using namespace std;


int swapper_offset(int offset, string str) {
    int found = -1;
    for (int i=offset+1; i<str.length(); i++) {
        if (str[i] > str[offset] && (found == -1 || str[i] < str[found])) {
            found = i;
        }
    }
    return found;
}


string next_id(string str) {
    for (int offset=str.length()-1; offset>=0; offset--) {
        int swap = swapper_offset(offset, str);
        if (swap != -1) {
            str[offset] ^= str[swap] ^= str[offset] ^= str[swap];
            sort(1+offset+str.begin(), str.end());
            return str;
        }
    }
    return "No Successor";
}


int main(void) {
    while (true) {
        string str;
        cin >> str;
        if (str.compare("#") == 0) {
            break;
        }
        cout << next_id(str) << endl;
    }
    return 0;
}
