#include <iostream>
using namespace std;

struct TreeNode
{
    int data;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : data(x), left(nullptr), right(nullptr) {}
};
/* height (root) {
    if (root != nullptr) {
        HL = height(root - > Lchild)
        HR = height(root -> Rchild)
        return max(HL, HR) + 1
    }
}*/
int Height(TreeNode *root)
{
    if (root == nullptr)
        return 0;
    return max(Height(root->left), Height(root->right)) + 1;
}

TreeNode *insert(TreeNode *root, int data)
{
    if (root == nullptr)
    {
        return new TreeNode(data);
    }

    if (data < root->data)
    {
        root->left = insert(root->left, data);
    }
    else
    {
        root->right = insert(root->right, data);
    }

    return root;
}

int main()
{
    int n;
    while (cin >> n)
    {
        TreeNode *root = nullptr;

        for (int i = 0; i < n; i++)
        {
            int data;
            cin >> data;
            root = insert(root, data);
        }

        cout << Height(root) << endl;
    }
    return 0;
}
