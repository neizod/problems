#include <iostream>
using namespace std;


bool board[500][500];


void init_board(int w, int h) {
    for (int i=0; i<h; i++) {
        for (int j=0; j<w; j++) {
            board[i][j] = false;
        }
    }
}


void fill_rect(int x1, int y1, int x2, int y2) {
    if (x2 < x1) {
        x1 ^= x2 ^= x1 ^= x2;
    }
    if (y2 < y1) {
        y1 ^= y2 ^= y1 ^= y2;
    }
    for (int i=y1-1; i<y2; i++) {
        for (int j=x1-1; j<x2; j++) {
            board[i][j] = true;
        }
    }
}


int count_free(int w, int h) {
    int counter = 0;
    for (int i=0; i<h; i++) {
        for (int j=0; j<w; j++) {
            counter += !board[i][j];
        }
    }
    return counter;
}


bool testcase() {
    int w, h, n;
    cin >> w >> h >> n;
    if (w == 0 && h == 0 && n == 0) {
        return false;
    }
    init_board(w, h);
    for (int i=0; i<n; i++) {
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        fill_rect(x1, y1, x2, y2);
    }
    int answer = count_free(w, h);
    if (answer == 0) {
        cout << "There is no empty spots." << endl;
    } else if (answer == 1) {
        cout << "There is one empty spot." << endl;
    } else {
        cout << "There are " << answer << " empty spots." << endl;
    }
    return true;
}


int main(void) {
    while (testcase());
    return 0;
}
