#include <iostream>
#include <stack>
using namespace std;


class Tree {
    public:
        int value;
        Tree* left;
        Tree* right;
        Tree(char value, Tree* left=0, Tree* right=0):
            value(value), left(left), right(right) {};
};


Tree* refill_tree() {
    int value;
    cin >> value;
    if (value == -1) {
        return 0;
    }
    return new Tree(value, refill_tree(), refill_tree());
}


void aux_traverse(Tree* root, stack<int>* leftmost, stack<int>* rightmost) {
    int now = root->value + leftmost->top();
    leftmost->pop();
    leftmost->push(now);
    if (root->left != 0) {
        rightmost->push(leftmost->top());
        leftmost->pop();
        if (leftmost->empty()) {
            leftmost->push(0);
        }
        aux_traverse(root->left, leftmost, rightmost);
        leftmost->push(rightmost->top());
        rightmost->pop();
    }
    if (root->right != 0) {
        if (rightmost->empty()) {
            rightmost->push(0);
        }
        leftmost->push(rightmost->top());
        rightmost->pop();
        aux_traverse(root->right, leftmost, rightmost);
        rightmost->push(leftmost->top());
        leftmost->pop();
    }
}


void falling_leaves(Tree* root) {
    stack<int>* leftmost = new stack<int>;
    stack<int>* rightmost = new stack<int>;
    leftmost->push(0);
    aux_traverse(root, leftmost, rightmost);
    while (!leftmost->empty()) {
        rightmost->push(leftmost->top());
        leftmost->pop();
    }
    while (!rightmost->empty()) {
        cout << rightmost->top();
        if (rightmost->size() > 1) {
            cout << " ";
        }
        rightmost->pop();
    }
    cout << endl;
}


int main(void) {
    int test = 1;
    while (true) {
        Tree* root = refill_tree();
        if (root == 0) {
            break;
        }
        cout << "Case " << test << ":" << endl;
        falling_leaves(root);
        cout << endl;
        test += 1;
    }
}
