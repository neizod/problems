#include <iostream>

using namespace std;


int size;
string triangle[100];


bool has_coord(int x, int y) {
    return y >= 0 && y < size && x >= 0 && x < triangle[y].length();
}


bool check_cut(int x, int y) {
    return triangle[y][x] == '#';
}


int find_largest_down(int x, int y, int depth=0) {
    if (!has_coord(x, y+depth)) {
        return depth;
    }
    if (check_cut(x, y+depth)) {
        return depth;
    }
    for (int dy=0; dy<depth; dy++) {
        int px = 2*(depth-dy) - 1;
        for (int dx=0; dx<2; dx++) {
            if (check_cut(x+px+dx, y+dy)) {
                return depth;
            }
        }
    }
    return find_largest_down(x, y, depth+1);
}


int find_largest_up(int x, int y, int depth=0) {
    if (!has_coord(x, y+depth) || !has_coord(x-2*depth, y+depth)) {
        return depth;
    }
    for (int dx=0; dx<2*depth+1; dx++) {
        if (check_cut(x-dx, y+depth)) {
            return depth;
        }
    }
    return find_largest_up(x, y, depth+1);
}


int largest_sub_triangle() {
    int answer = 0;
    for (int y=0; y<size; y++) {
        for (int x=0; x<triangle[y].length(); x++) {
            if (x%2 == 0) {
                answer = max(answer, find_largest_down(x, y));
            } else {
                answer = max(answer, find_largest_up(x, y));
            }
        }
    }
    return answer*answer;
}


int main(void) {
    int test = 0;
    while (true) {
        test += 1;
        cin >> size;
        if (size == 0) {
            break;
        }
        for (int i=0; i<size; i++) {
            cin >> triangle[i];
        }
        int answer = largest_sub_triangle();
        cout << "Triangle #" << test << endl;
        cout << "The largest triangle area is " << answer << "." << endl;
        cout << endl;
    }
    return 0;
}
