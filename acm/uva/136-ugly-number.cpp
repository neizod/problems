#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
using namespace std;


long double pow(int base, int exponent) {
    if (exponent == 0) {
        return 1;
    }
    return (exponent % 2 == 0 ? 1 : base) * pow(base*base, exponent/2);
}


bool found_ugly(int index, vector<long double> numbers) {
    if (numbers.size() < index) {
        return false;
    }
}


int least_pow(int e2, int e3, int e5) {
    long double p2 = pow(2, e2);
    long double p3 = pow(3, e3);
    long double p5 = pow(5, e5);
    if (p2 < p3 && p2 < p5) {
        return 2;
    } else if (p3 < p5) {
        return 3;
    }
    return 5;
}


bool satisfy(vector<long double> numbers, int index, int e2, int e3, int e5) {
    if (numbers.size() < index) {
        return false;
    }
    long double ugly = numbers[index-1];
    return ugly <= pow(2, e2) && ugly <= pow(3, e3) && ugly <= pow(5, e5);
}


long double find_ugly(int index) {
    vector<long double> numbers = { 1.0L };
    int e2 = 0, e3 = 0, e5 = 0;
    while (!satisfy(numbers, index, e2, e3, e5)) {
        switch (least_pow(e2, e3, e5)) {
            case 2:
                e2 += 1;
                for (int i=0; i<=e3; i++) {
                    for (int j=0; j<=e5; j++) {
                        numbers.push_back(pow(2, e2) * pow(3, i) * pow(5, j));
                    }
                }
                break;
            case 3:
                e3 += 1;
                for (int i=0; i<=e2; i++) {
                    for (int j=0; j<=e5; j++) {
                        numbers.push_back(pow(2, i) * pow(3, e3) * pow(5, j));
                    }
                }
                break;
            case 5:
                e5 += 1;
                for (int i=0; i<=e2; i++) {
                    for (int j=0; j<=e3; j++) {
                        numbers.push_back(pow(2, i) * pow(3, j) * pow(5, e5));
                    }
                }
                break;
        }
        sort(numbers.begin(), numbers.end());
    }
    return numbers[index-1];
}


int main(void) {
    cout << "The 1500'th ugly number is "
         << fixed << setprecision(0) << find_ugly(1500) << "." << endl;
    return 0;
}
