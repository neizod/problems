#include <iostream>
#include <queue>
using namespace std;


class Tree {
    public:
        string value;
        Tree* left;
        Tree* right;
        Tree(string value="", Tree* left=0, Tree* right=0):
            value(value), left(left), right(right) {};
};


pair<string,string> parse(string read_pair) {
    bool read_first;
    string first;
    string second;
    for (char ch : read_pair) {
        if (ch == '(') {
            read_first = true;
        } else if (ch == ',') {
            read_first = false;
        } else if (ch != ')') {
            if (read_first) {
                first += ch;
            } else {
                second += ch;
            }
        }
    }
    return make_pair(first, second);
}


Tree* read_tree() {
    Tree* tree = new Tree();
    string read_pair;
    while (cin >> read_pair && read_pair.length() > 2) {
        pair<string,string> parsed_pair = parse(read_pair);
        Tree* now = tree;
        for (char dir : parsed_pair.second) {
            if (dir == 'L') {
                if (now->left == 0) {
                    now->left = new Tree();
                }
                now = now->left;
            } else {
                if (now->right == 0) {
                    now->right = new Tree();
                }
                now = now->right;
            }
        }
        if (now->value == "") {
            now->value = parsed_pair.first;
        } else {
            now->value = "duplicated";
        }
    }
    if (!cin) {
        exit(EXIT_SUCCESS);
    }
    return tree;
}


void traverse(Tree* tree) {
    bool valid = true;
    queue<string> values;
    queue<Tree*> waiting;
    waiting.push(tree);
    while (!waiting.empty()) {
        Tree* now = waiting.front();
        waiting.pop();
        if (now->value == "" || now->value == "duplicated") {
            valid = false;
        } else {
            values.push(now->value);
        }
        if (now->left != 0) {
            waiting.push(now->left);
        }
        if (now->right != 0) {
            waiting.push(now->right);
        }
        delete now;
    }
    if (valid) {
        while (true) {
            cout << values.front();
            values.pop();
            if (!values.empty()) {
                cout << " ";
            } else {
                break;
            }
        }
        cout << endl;
    } else {
        cout << "not complete" << endl;
    }
}


int main(void) {
    while (true) {
        traverse(read_tree());
    }
    return 0;
}
