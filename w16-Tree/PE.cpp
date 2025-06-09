#include <iostream>
#include <vector>
#include <set>
#include <sstream>
#include <string>
#include <algorithm>

using namespace std;

#define pb push_back
#define vi vector<int>

int main()
{
    int n;

    while (cin >> n)
    {
        vi allNodes;
        vi nonLeafNodes;

        for (int i = 0; i < n; i++)
        {
            string line;
            getline(cin >> ws, line);

            istringstream iss(line);
            int parent;
            iss >> parent;

            allNodes.pb(parent);

            int child;
            bool hasChildren = false;
            while (iss >> child)
            {
                allNodes.pb(child);
                hasChildren = true;
            }
            if (hasChildren)
            {
                nonLeafNodes.pb(parent);
            }
        }

        sort(allNodes.begin(), allNodes.end());
        allNodes.erase(unique(allNodes.begin(), allNodes.end()), allNodes.end());

        sort(nonLeafNodes.begin(), nonLeafNodes.end());
        nonLeafNodes.erase(unique(nonLeafNodes.begin(), nonLeafNodes.end()), nonLeafNodes.end());

        vi leafNodes;
        for (int node : allNodes)
        {
            if (!binary_search(nonLeafNodes.begin(), nonLeafNodes.end(), node))
            {
                leafNodes.pb(node);
            }
        }

        for (int i = 0; i < leafNodes.size(); i++)
        {
            if (i > 0)
            {
                cout << " ";
            }
            cout << leafNodes[i];
        }
        cout << endl;
    }

    return 0;
}
