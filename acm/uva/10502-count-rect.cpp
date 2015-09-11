#include <iostream>
using namespace std;


bool board[100][100];


void read_board(int n, int m) {
    char temp_read;
    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            cin >> temp_read;
            board[i][j] = temp_read - '0';
        }
    }
}


bool contain_rect(int y, int x, int h, int w) {
    for (int i=y; i<y+h; i++) {
        for (int j=x; j<x+w; j++) {
            if (!board[i][j]) {
                return false;
            }
        }
    }
    return true;
}


int count_rect(int n, int m) {
    int counter = 0;
    for (int h=1; h<=n; h++) {
        for (int w=1; w<=m; w++) {
            for (int y=0; y<=n-h; y++) {
                for (int x=0; x<=m-w; x++) {
                    counter += contain_rect(y, x, h, w);
                }
            }
        }
    }
    return counter;
}


void testcase(int n, int m) {
    read_board(n, m);
    cout << count_rect(n, m) << endl;
}


int main(void) {
    int n, m;
    while (true) {
        cin >> n;
        if (n == 0) {
            break;
        }
        cin >> m;
        testcase(n, m);
    }
    return 0;
}
