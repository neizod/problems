#include <iostream>
#include <list>
using namespace std;


int sort_steps(int carriages, list<int> trains) {
    int steps = 0;
    for (int i=0; i<carriages; i++) {
        int margin = 0;
        for (list<int>::iterator j=trains.begin(); j!=trains.end(); j++) {
            if ((*j) == i) {
                steps += margin;
                trains.erase(j);
                break;
            }
            margin += 1;
        }
    }
    return steps;
}


int main(void) {
    int test;
    cin >> test;
    for (int i=0; i<test; i++) {
        int carriages;
        cin >> carriages;
        list<int> trains;
        for (int j=0; j<carriages; j++) {
            int train_no;
            cin >> train_no;
            trains.push_back(train_no);
        }
        cout << "Optimal train swapping takes ";
        cout << sort_steps(carriages, trains) << " swaps." << endl;
    }
    return 0;
}
