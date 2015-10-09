#include <iostream>
#include <stack>
#include <queue>
using namespace std;


bool rearrangeable(int n, queue<int> order) {
    stack<int> swap_rail;
    int comming = 1;
    while (!order.empty()) {
        if (order.front() == comming) {
            order.pop();
            comming += 1;
        } else if (order.front() > comming) {
            swap_rail.push(comming);
            comming += 1;
        } else if (order.front() == swap_rail.top()) {
            swap_rail.pop();
            order.pop();
        } else {
            return false;
        }
    }
    return true;
}


int main(void) {
    while (true) {
        int n;
        cin >> n;
        if (n == 0) {
            break;
        }
        while (true) {
            queue<int> order;
            for (int i=0; i<n; i++) {
                int train_no;
                cin >> train_no;
                if (train_no == 0) {
                    break;
                }
                order.push(train_no);
            }
            if (order.empty()) {
                cout << endl;
                break;
            } else {
                cout << (rearrangeable(n, order) ? "Yes" : "No") << endl;
            }
        }
    }
    return 0;
}
