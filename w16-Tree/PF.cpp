#include <iostream>
#include <vector>
using namespace std;

// DLR
void preorder(vector<int> &tree, int i, int size)
{
    if (i >= size || tree[i] == 0)
        return;
    cout << tree[i] << " ";
    preorder(tree, 2 * i + 1, size);
    preorder(tree, 2 * i + 2, size);
}

// LDR
void inorder(vector<int> &tree, int i, int size)
{
    if (i >= size || tree[i] == 0)
        return;
    inorder(tree, 2 * i + 1, size);
    cout << tree[i] << " ";
    inorder(tree, 2 * i + 2, size);
}

// LRD
void postorder(vector<int> &tree, int i, int size)
{
    if (i >= size || tree[i] == 0)
        return;
    postorder(tree, 2 * i + 1, size);
    postorder(tree, 2 * i + 2, size);
    cout << tree[i] << " ";
}

int main()
{
    int n;
    while (cin >> n)
    {
        int size = (1 << n) - 1;
        vector<int> tree(size);

        for (int i = 0; i < size; i++)
        {
            cin >> tree[i];
        }

        preorder(tree, 0, size);
        cout << endl;
        inorder(tree, 0, size);
        cout << endl;
        postorder(tree, 0, size);
        cout << endl
             << endl;
    }
    return 0;
}
