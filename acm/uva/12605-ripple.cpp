#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;


int grid[15][15], conn[15][15];


bool found(pair<int,int> pos, deque<pair<int,int>> elems) {
    return find(elems.begin(), elems.end(), pos) != elems.end();
}


pair<int,int> dest(int mask, pair<int,int> pos) {
    if (mask == 1) {
        pos.first -= 1;
    } else if (mask == 2) {
        pos.second += 1;
    } else if (mask == 4) {
        pos.first += 1;
    } else {
        pos.second -= 1;
    }
    return pos;
}


bool going(int mask, pair<int,int> pos, deque<pair<int,int>> seen) {
    return conn[pos.first][pos.second] & mask && !found(dest(mask, pos), seen);
}


deque<pair<int,int>> polygon_cells(int row, int col) {
    deque<pair<int,int>> wait, seen;
    wait.push_back(make_pair(row, col));
    while (!wait.empty()) {
        pair<int,int> pos = wait.back();
        wait.pop_back();
        if (!found(pos, seen)) {
            seen.push_back(pos);
            for (int mask=1; mask<=8; mask*=2) {
                if (going(mask, pos, seen)) {
                    wait.push_back(dest(mask, pos));
                }
            }
        }
    }
    return seen;
}


bool check_poly(int row, int col) {
    deque<pair<int,int>> cells = polygon_cells(row, col);
    cells.pop_front();
    for (pair<int,int> pos : cells) {
        if (grid[row][col] == grid[pos.first][pos.second]) {
            return false;
        }
    }
    return true;
}


bool check_dist(int row, int col, int rows, int cols) {
    int value = grid[row][col];
    for (int r=max(row-value, 0); r<min(row+value, rows); r++) {
        if (row != r && value == grid[r][col]) {
            return false;
        }
    }
    for (int c=max(col-value, 0); c<min(col+value, cols); c++) {
        if (col != c && value == grid[row][c]) {
            return false;
        }
    }
    return true;
}


bool check(int rows, int cols) {
    for (int row=0; row<rows; row++) {
        for (int col=0; col<cols; col++) {
            if (!check_poly(row, col) || !check_dist(row, col, rows, cols)) {
                return false;
            }
        }
    }
    return true;
}


int main(void) {
    int test;
    cin >> test;
    while (test) {
        int rows, cols;
        cin >> rows >> cols;
        for (int row=0; row<rows; row++) {
            for (int col=0; col<cols; col++) {
                char digit;
                cin >> digit;
                grid[row][col] = digit - '0';
            }
        }
        for (int row=0; row<rows; row++) {
            for (int col=0; col<cols; col++) {
                cin >> conn[row][col];
            }
        }
        cout << (check(rows, cols) ? "valid" : "invalid") << endl;
        test -= 1;
    }
    return 0;
}
