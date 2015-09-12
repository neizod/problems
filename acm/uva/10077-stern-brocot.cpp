#include <iostream>
#include <string>
using namespace std;


int gcd(int a, int b) {
    if (b == 0) {
        return a;
    } else {
        return gcd(b, a%b);
    }
}


class Frac {
    protected:
        int numer, denom;

        void cancle_common() {
            int common = gcd(numer, denom);
            numer /= common;
            denom /= common;
        }

    public:
        Frac(int numer, int denom):
            numer(numer), denom(denom) { cancle_common(); }

        void operator&= (Frac other) {
            numer += other.numer;
            denom += other.denom;
            cancle_common();
        }

        bool operator!= (Frac other) {
            return numer * other.denom != other.numer * denom;
        }

        bool operator< (Frac other) {
            return numer * other.denom < other.numer * denom;
        }

        bool operator> (Frac other) {
            return numer * other.denom > other.numer * denom;
        }

        void out() {
            cout << numer << "/" << denom << endl;
        }
};


string drilldown(Frac find) {
    Frac left(0, 1), current(1, 1), right(1, 0);
    string repr = "";
    while (current != find) {
        if (current < find) {
            left = current;
            current &= right;
            repr += "R";
        } else if (current > find) {
            right = current;
            current &= left;
            repr += "L";
        }
    }
    return repr;
}


int main(void) {
    while (true) {
        int numer, denom;
        cin >> numer;
        cin >> denom;
        if (numer == 1 && denom == 1) {
            break;
        }
        cout << drilldown(Frac(numer, denom)) << endl;
    }
    return 0;
}
