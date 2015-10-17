#include <iostream>
#include <queue>
#include <unordered_set>
using namespace std;


unordered_set<int> major_scales({0, 2, 4, 5, 7, 9, 11});


int note2i(string note) {
    int tone = 2 * (note[0] - 'C') + 12;
    if (note[0] > 'E') {
        tone -= 1;
    }
    if (note[0] < 'C') {
        tone += 1;
    }
    if (note.size() == 2 && note[1] == '#') {
        tone += 1;
    }
    return tone % 12;
}


string i2note(int tone) {
    string note = "C";
    if (tone > 4) {
        tone += 1;
    }
    if (tone > 9) {
        tone -= 15;
    }
    note[0] += tone / 2;
    if (tone % 2 == 1 || (tone+1) % 2 == -1) {
        note += "#";
    }
    return note;
}


unordered_set<int> up_scale(unordered_set<int> tones, int dist) {
    unordered_set<int> moved_tones;
    for (auto tone : tones) {
        moved_tones.insert((tone+12-dist)%12);
    }
    return moved_tones;
}


bool check_major(unordered_set<int> tones) {
    for (auto tone : tones) {
        if (major_scales.find(tone) == major_scales.end()) {
            return false;
        }
    }
    return true;
}


deque<string> find_scales(unordered_set<int> tones) {
    deque<string> valid_scales;
    for (int i=0; i<12; i++) {
        if (check_major(up_scale(tones, i))) {
            valid_scales.push_back(i2note(i));
        }
    }
    return valid_scales;
}


int main(void) {
    string note;
    while (true) {
        unordered_set<int> tones;
        while (true) {
            cin >> note;
            tones.insert(note2i(note));
            if (cin.peek() == '\n') {
                break;
            }
        }
        if (note == "END") {
            break;
        } else {
            deque<string> valid_scales = find_scales(tones);
            while (!valid_scales.empty()) {
                cout << valid_scales.front();
                valid_scales.pop_front();
                if (!valid_scales.empty()) {
                    cout << " ";
                }
            }
            cout << endl;
        }
    }
    return 0;
}
