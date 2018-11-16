#include <bits/stdc++.h>
using namespace std;

typedef pair<double,double> pt;
typedef pair<pt,double> circ;


unsigned get_seed() {
    return chrono::system_clock::now().time_since_epoch().count();
}


double det(double m11, double m12, double m13,
           double m21, double m22, double m23,
           double m31, double m32, double m33) {
    return m11*m22*m33 + m12*m23*m31 + m13*m21*m32 - m31*m22*m13 - m32*m23*m11 - m33*m21*m12;
}


pt center(circ circle) {
    return circle.first;
}


double sq_dist(pt p1, pt p2=make_pair(0, 0)) {
    return pow(p1.first-p2.first, 2.0) + pow(p1.second-p2.second, 2.0);
}


// XXX please note that though the problem statement says 2 <= n <= 100,
//     the actual test does contain case of n == 1 too. WTF!!!
circ from_1_points(pt p1) {
    return make_pair(p1, 0);
}


circ from_2_points(pt p1, pt p2) {
    double dx = (p1.first + p2.first) / 2.0;
    double dy = (p1.second + p2.second) / 2.0;
    pt c = make_pair(dx, dy);
    double r = pow(sq_dist(p1, p2), 0.5) / 2.0;
    return make_pair(c, r);
}


circ from_3_points(pt p1, pt p2, pt p3) {
    double ss1 = sq_dist(p1);
    double ss2 = sq_dist(p2);
    double ss3 = sq_dist(p3);
    double a = det(p1.first, p1.second, 1, p2.first, p2.second, 1, p3.first, p3.second, 1);
    double b = det(p1.first, p1.second, ss1, p2.first, p2.second, ss2, p3.first, p3.second, ss3);
    double sx = det(ss1, p1.second, 1, ss2, p2.second, 1, ss3, p3.second, 1);
    double sy = det(p1.first, ss1, 1, p2.first, ss2, 1, p3.first, ss3, 1);
    pt c = make_pair(sx/a/2.0, sy/a/2.0);
    double r = pow(b/a + sq_dist(c), 0.5);
    return make_pair(c, r);
}


bool contains(circ circle, pt p) {
    if (circle.second == 0) {
        return false;
    }
    return sq_dist(p, center(circle)) <= pow(circle.second, 2.0);
}


circ mincircle3p(pt p1, pt p2, pt p3) {
    if (contains(from_2_points(p1, p3), p2)) {
        return from_2_points(p1, p3);
    }
    if (contains(from_2_points(p2, p3), p1)) {
        return from_2_points(p2, p3);
    }
    return from_3_points(p1, p2, p3);
}


circ mincircle2p(vector<pt> ps, pt p1, pt p2) {
    circ circle = from_2_points(p1, p2);
    for (int i=0; i<size(ps); i++) {
        if (!contains(circle, ps[i])) {
            circle = mincircle3p(p1, p2, ps[i]);
        }
    }
    return circle;
}


circ mincircle1p(vector<pt> ps, pt p1) {
    vector<pt> seen;
    shuffle(ps.begin(), ps.end(), default_random_engine(get_seed()));
    circ circle = from_1_points(p1);
    for (int i=0; i<size(ps); i++) {
        if (!contains(circle, ps[i])) {
            circle = mincircle2p(seen, p1, ps[i]);
        }
        seen.push_back(ps[i]);
    }
    return circle;
}


circ mincircle(vector<pt> ps) {
    vector<pt> seen;
    shuffle(ps.begin(), ps.end(), default_random_engine(get_seed()));
    circ circle = make_pair(make_pair(0, 0), 0);
    for (int i=0; i<size(ps); i++) {
        if (!contains(circle, ps[i])) {
            circle = mincircle1p(seen, ps[i]);
        }
        seen.push_back(ps[i]);
    }
    return circle;
}


int main(void) {
    int n;
    for (int t=1;;t++) {
        cin >> n;
        if (n == 0) {
            break;
        }
        vector<pt> ps;
        double x, y;
        for (int i=0; i<n; i++) {
            cin >> x >> y;
            ps.push_back(make_pair(x, y));
        }
        circ ans = mincircle(ps);
        printf("Instancia %d\n", t);
        printf("%.2f %.2f %.2f\n\n", ans.first.first, ans.first.second, ans.second);
    }
    return 0;
}
