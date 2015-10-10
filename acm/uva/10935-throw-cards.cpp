#include <iostream>
#include <queue>
using namespace std;


void throwing_cards(int no_cards) {
    queue<int> deck;
    for (int i=0; i<no_cards; i++) {
        deck.push(i+1);
    }
    cout << "Discarded cards:";
    while (deck.size() > 1) {
        cout << " " << deck.front();
        deck.pop();
        if (deck.size() > 1) {
            cout << ",";
            deck.push(deck.front());
            deck.pop();
        }
    }
    cout << endl << "Remaining card: " << deck.front() << endl;
}


int main(void) {
    while (true) {
        int no_cards;
        cin >> no_cards;
        if (!no_cards) {
            break;
        }
        throwing_cards(no_cards);
    }
    return 0;
}
