#include <iostream>
#include <algorithm>
using namespace std;


string jolly_checker(int size, int elements[]) {
    for (int i=0; i<size-1; i++) {
        elements[i] = abs(elements[i] - elements[i+1]);
    }
    elements[size-1] = 0;
    sort(elements, elements+size);
    for (int i=0; i<size; i++) {
        if (i != elements[i]) {
            return "Not jolly";
        }
    }
    return "Jolly";
}


int main(void) {
    int size;
    while (cin >> size) {
        int elements[size];
        for (int i=0; i<size; i++) {
            cin >> elements[i];
        }
        cout << jolly_checker(size, elements) << endl;
    }
    return 0;
}
