#include <iostream>
using namespace std;


int ceil_div(int numerator, int denominator) {
    return numerator / denominator + (numerator % denominator != 0);
}


int sonar_used(int rows, int cols) {
    return ceil_div(rows-2, 3) * ceil_div(cols-2, 3);
}


int main(void) {
    int test;
    cin >> test;
    for (int i=0; i<test; i++) {
        int rows, cols;
        cin >> rows >> cols;
        cout << sonar_used(rows, cols) << endl;
    }
    return 0;
}
