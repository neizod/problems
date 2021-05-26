#include <iostream>
using namespace std;

int xs[100];


int count_reversort(int n) {
    int count = 0;
    for (int i=0; i<n-1; i++) {
        int j = i;
        while (i+1 != xs[j]) {
            j += 1;
        }
        int s = (1+j-i);
        count += s;
        for (int k=0; k<s/2; k++) {
            swap(xs[i+k], xs[j-k]);
        }
    }
    return count;
}


int main(void) {
    int tt;
    cin >> tt;
    for (int t=0; t<tt; t++) {
        int n;
        cin >> n;
        for (int i=0; i<n; i++) {
            cin >> xs[i];
        }
        int answer = count_reversort(n);
        printf("Case #%i: %i\n", t+1, answer);
    }
    return 0;
}
