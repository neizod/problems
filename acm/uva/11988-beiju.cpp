#include <iostream>
#include <deque>
using namespace std;


void beiju(string text) {
    deque<string> aligned_texts;
    int init = 0, stop = 0;
    bool started = false;
    while (stop<=text.size()) {
        if (text[stop] == '[' || text[stop] == ']' || stop == text.size()) {
            string part = text.substr(started+init, stop-init-started);
            if (text[init] == '[') {
                aligned_texts.push_front(part);
            } else {
                aligned_texts.push_back(part);
            }
            started = true;
            init = stop;
        }
        stop += 1;
    }
    for (string part : aligned_texts) {
        cout << part;
    }
    cout << endl;
}


int main(void) {
    while (true) {
        string text;
        cin >> text;
        if (cin.eof()) {
            break;
        }
        beiju(text);
    }
    return 0;
}
