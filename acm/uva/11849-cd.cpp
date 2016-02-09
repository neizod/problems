#include <iostream>
#include <unordered_set>
using namespace std;


int main() {
    do {
        int jack, jill;
        cin >> jack >> jill;
        if (jack == 0 && jill == 0) {
            break;
        }
        unordered_set<int> cds;
        for (int i = 0; i < jack; i++) {
            int tmp;
            cin >> tmp;
            cds.insert(tmp);
        }
        for (int i = 0; i < jill; i++) {
            int tmp;
            cin >> tmp;
            cds.erase(tmp);
        }
        cout << jack - cds.size() << endl;
    } while (true);
    return 0;
}
