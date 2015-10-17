#include <iostream>
#include <iomanip>
#include <queue>
#include <vector>
#include <limits>
#include <functional>
using namespace std;


const float inf = numeric_limits<float>::infinity();
typedef pair<pair<float,float>,float> fff;


fff make_filter(float a, float b, float c) {
    return make_pair(make_pair(a, b), c);
}


fff swap_filter_range(fff filter) {
    return make_filter(filter.first.second, filter.first.first, filter.second);
}


float calc_light(priority_queue<fff,vector<fff>,greater<fff>> actives) {
    float light = 1.0;
    while (!actives.empty()) {
        light *= actives.top().second;
        actives.pop();
    }
    return light;
}


vector<fff> light_range(priority_queue<fff,vector<fff>,greater<fff>> filters) {
    vector<fff> results;
    float from = -inf, till = inf;
    priority_queue<fff,vector<fff>,greater<fff>> actives;
    actives.push(make_filter(till, from, 1.0));
    while (!actives.empty()) {
        float light = calc_light(actives);
        if (!filters.empty() && filters.top() < actives.top()) {
            till = filters.top().first.first;
            actives.push(swap_filter_range(filters.top()));
            filters.pop();
        } else {
            till = actives.top().first.first;
            actives.pop();
        }
        results.push_back(make_filter(from, till, light));
        from = till;
    }
    return results;
}


int main(void) {
    int test;
    cin >> test;
    while (test) {
        priority_queue<fff,vector<fff>,greater<fff>> filters;
        int lines;
        cin >> lines;
        for (int j=0; j<lines; j++) {
            float x1, x2, r;
            cin >> x1 >> r >> x2 >> r >> r;
            filters.push(make_filter(min(x1, x2), max(x2, x1), r));
        }
        vector<fff> light_results = light_range(filters);
        cout << light_results.size() << endl;
        cout << fixed << setprecision(3);
        for (fff result : light_results) {
            cout << result.first.first << " "
                 << (result.first.second == inf ? showpos : noshowpos)
                 << result.first.second << " "
                 << noshowpos << result.second << endl;
        }
        test -= 1;
        if (test) {
            cout << endl;
        }
    }
    return 0;
}
