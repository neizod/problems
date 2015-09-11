#include <iostream>
using namespace std;


int count(int size, bool array[]) {
    int result = 0;
    for (int i=0; i<size; i++) {
        result += array[i];
    }
    return result;
}


int workday_loss(int days, int num_parties, int parties[]) {
    bool calendar[days] = { false };
    for (int i=0; i<num_parties; i++) {
        int hartal_cycle = parties[i];
        for (int d=hartal_cycle-1; d<days; d+=hartal_cycle) {
            calendar[d] = true;
        }
    }
    for (int d=6-1; d<days; d+=7) {
        calendar[d] = calendar[d+1] = false;
    }
    return count(days, calendar);
}


void testcase() {
    int days, num_parties;
    cin >> days;
    cin >> num_parties;
    int parties[num_parties] = { 0 };
    for (int i=0; i<num_parties; i++) {
        cin >> parties[i];
    }
    cout << workday_loss(days, num_parties, parties) << endl;
}


int main(void) {
    int test;
    cin >> test;
    for (int i=0; i<test; i++) {
        testcase();
    }
    return 0;
}
