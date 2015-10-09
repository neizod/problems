#include <iostream>
#include <algorithm>
#include <string>
#include <stack>
#include <queue>
using namespace std;


class Tree {
    public:
        char value;
        Tree* left;
        Tree* right;
        Tree(char value, Tree* left=0, Tree* right=0):
            value(value), left(left), right(right) {};
};


Tree* make_tree(string reverse_polish_nonation) {
    stack<Tree*> stack_memo;
    for (char& ch : reverse_polish_nonation) {
        if ('a' <= ch && ch <= 'z') {
            stack_memo.push(new Tree(ch));
        } else {
            Tree* right = stack_memo.top();
            stack_memo.pop();
            Tree* left = stack_memo.top();
            stack_memo.pop();
            stack_memo.push(new Tree(ch, left, right));
        }
    }
    return stack_memo.top();
}


string traverse(Tree* root) {
    string notation;
    queue<Tree*> queue_memo;
    queue_memo.push(root);
    while (!queue_memo.empty()) {
        Tree* tree = queue_memo.front();
        queue_memo.pop();
        notation += tree->value;
        if (tree->left != 0)
            queue_memo.push(tree->left);
        if (tree->right != 0)
            queue_memo.push(tree->right);
    }
    reverse(notation.begin(), notation.end());
    return notation;
}


int main(void) {
    int test;
    cin >> test;
    for (int i=0; i<test; i++) {
        string notation;
        cin >> notation;
        cout << traverse(make_tree(notation)) << endl;
    }
    return 0;
}

