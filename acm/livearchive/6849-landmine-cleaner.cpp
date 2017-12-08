#include <iostream>

using namespace std;


int n, m;
int hint[1000][1000];
char mine[1000][1000];


void print_output() {
    for (int y=0; y<n; y++) {
        for (int x=0; x<m; x++) {
            cout << mine[y][x];
        }
        cout << endl;
    }
}


int count_suround_mines(int x, int y) {
    int c = 0;
    for (int dy=-1; dy<=1; dy++) {
        for (int dx=-1; dx<=1; dx++) {
            if (dx == 0 && dy == 0) {
                continue;
            }
            if (x+dx < 0 || y+dy < 0 || x+dx >= m || y+dy >= n) {
                continue;
            }
            if (mine[y+dy][x+dx] == '?') {
                c += 1;
            }
        }
    }
    return c;
}


void update(bool is_mine, int x, int y) {
    if (is_mine) {
        mine[y][x] = 'L';
        hint[y][x] -= 4;
        for (int dy=-1; dy<=1; dy++) {
            for (int dx=-1; dx<=1; dx++) {
                if (dx == 0 && dy == 0) {
                    continue;
                }
                if (x+dx < 0 || y+dy < 0 || x+dx >= m || y+dy >= n) {
                    continue;
                }
                hint[y+dy][x+dx] -= 1;
            }
        }
    } else {
        mine[y][x] = '-';
    }
}


void solve() {
    for (int y=0; y<n; y++) {
        int remain = m;
        while (remain) {
            for (int x=0; x<m; x++) {
                if (mine[y][x] != '?') {
                    continue;
                }
                if (hint[y][x] < 4) {
                    update(false, x, y);
                    remain -= 1;
                } else if (hint[y][x] > count_suround_mines(x, y)) {
                    update(true, x, y);
                    remain -= 1;
                }
            }
        }
    }
}


int main(void) {
    int t;
    cin >> t;
    for (int k=0; k<t; k++) {
        cin >> n >> m;
        for (int y=0; y<n; y++) {
            for (int x=0; x<m; x++) {
                cin >> hint[y][x];
                mine[y][x] = '?';
            }
        }
        solve();
        print_output();
    }
    return 0;
}
