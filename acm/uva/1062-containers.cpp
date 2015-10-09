#include <iostream>
#include <vector>
using namespace std;


int count_stacks(string containers) {
    vector<char> stacks;
    for (char& container : containers) {
        bool pushed = false;
        for (int i=0; i<stacks.size(); i++) {
            if (container <= stacks[i]) {
                stacks[i] = container;
                pushed = true;
                break;
            }
        }
        if (!pushed) {
            stacks.push_back(container);
        }
    }
    return stacks.size();
}


int main(void) {
    int case_no = 1;
    while (true) {
        string containers;
        cin >> containers;
        if (containers == "end") {
            break;
        }
        cout << "Case " << case_no << ": " << count_stacks(containers) << endl;
        case_no++;
    }
    return 0;
}
