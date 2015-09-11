#include <iostream>
using namespace std;


int factorial(int n) {
    if (n == 0) {
        return 1;
    }
    return n * factorial(n-1);
}


int combination(int n, int k) {
    return factorial(n) / factorial(k) / factorial(n-k);
}


int pow(int base, int exponent) {
    int product = 1;
    while (exponent) {
        product *= base;
        exponent -= 1;
    }
    return product;
}


int fubini(int n) {
    int summation = 0;
    for (int k=0; k<=n; k++) {
        for (int j=0; j<=k; j++) {
            summation += pow(-1, k-j) * combination(k, j) * pow(j, n);
        }
    }
    return summation;
}

int main(void) {
    int test;
    cin >> test;
    for (int i=0; i<test; i++) {
        int n;
        cin >> n;
        cout << fubini(n) << endl;
    }
    return 0;
}
