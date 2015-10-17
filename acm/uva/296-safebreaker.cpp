#include <iostream>
#include <iomanip>
#include <utility>
#include <list>
#include <cmath>
using namespace std;


class Guess {
    public:
        int code;
        pair<int,int> signature;
        Guess(int code, int corrected, int misplaced):
            code(code) { signature = make_pair(corrected, misplaced); };
};


int exp(int exponent) {
    return pow(10, exponent);
}


int del_digit(int number, int position) {
    return number / exp(position+1) * exp(position) + number % exp(position);
}


int get_digit(int number, int position) {
    return (number / exp(position)) % 10;
}


pair<int,int> signature(int actual, int guess) {
    int corrected = 0;
    int misplaced = 0;
    for (int i=3; i>=0; i--) {
        if (get_digit(actual, i) == get_digit(guess, i)) {
            corrected += 1;
            actual = del_digit(actual, i);
            guess = del_digit(guess, i);
        }
    }
    for (int i=3-corrected; i>=0; i--) {
        for (int j=3-corrected-misplaced; j>=0; j--) {
            if (get_digit(actual, i) == get_digit(guess, j)) {
                misplaced += 1;
                actual = del_digit(actual, i);
                guess = del_digit(guess, j);
                break;
            }
        }
    }
    return make_pair(corrected, misplaced);
}


void decode(list<Guess> guesses) {
    list<int> results;
    for (int i=0; i<10000; i++) {
        results.push_back(i);
    }
    for (Guess guess : guesses) {
        list<int>::iterator iter = results.begin();
        while (iter != results.end()) {
            if (signature(*iter, guess.code) != guess.signature) {
                iter = results.erase(iter);
            } else {
                iter++;
            }
        }
    }
    if (results.size() == 1) {
        cout << setw(4) << setfill('0') << results.front() << endl;
    } else if (results.size() == 0) {
        cout << "impossible" << endl;
    } else {
        cout << "indeterminate" << endl;
    }
}


int main(void) {
    int test;
    cin >> test;
    for (int i=0; i<test; i++) {
        list<Guess> guesses;
        int tried;
        cin >> tried;
        for (int j=0; j<tried; j++) {
            int code, corrected, misplaced;
            char delimiter;
            cin >> code >> corrected >> delimiter >> misplaced;
            guesses.push_back(Guess(code, corrected, misplaced));
        }
        decode(guesses);
    }
    return 0;
}
