#include <iostream>
using namespace std;


int hamming_distance(string w1, string w2) {
    int counter = 0;
    for (int i=0; i<w1.size(); i++) {
        counter += w1[i] != w2[i];
    }
    return counter;
}


int guess(string word) {
    if (word.size() == 5) {
        return 3;
    } else if (hamming_distance("two", word) <= 1) {
        return 2;
    }
    return 1;
}


int main(void) {
    int test;
    cin >> test;
    for (int i=0; i<test; i++) {
        string word;
        cin >> word;
        cout << guess(word) << endl;
    }
    return 0;
}
