#include <iostream>
#include <cmath>
#include <set>
using namespace std;


set<int> primes;
void init_primes(int size) {
    bool sieve[size] = { false };
    sieve[0] = sieve[1] = true;
    int p = 2;
    while (true) {
        for (int i=2*p; i<size; i+=p) {
            sieve[i] = true;
        }
        do {
            p += 1;
        } while (p < size && sieve[p]);
        if (p == size) {
            break;
        }
    }
    for (int i=0; i<size; i++) {
        if (!sieve[i]) {
            primes.insert(i);
        }
    }
}


int count_goldbach(int number) {
    int counter = 0;
    for (int prime : primes) {
        if (2*prime > number) {
            break;
        }
        if (primes.find(number-prime) != primes.end()) {
            counter += 1;
        }
    }
    return counter;
}


int main(void) {
    init_primes(pow(2, 15));
    while (true) {
        int number;
        cin >> number;
        if (number == 0) {
            break;
        }
        cout << count_goldbach(number) << endl;
    }
    return 0;
}
