#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define pb push_back
#define pf push_front
#define ft first
#define sec second
#define pll pair<ll, ll>
#define pii pair<int, int>
#define vi vector<int>
#define vll vector<ll>
#define vvi vector<vector<int>>
#define vvll vector<vector<ll>>

bool hasCycle(vvi &adj, int start, vi &visited)
{
    int n = adj.size();
    vi parent(n, -1);
    queue<int> q;
    visited[start] = true;
    q.push(start);

    while (!q.empty())
    {
        int curr = q.front();
        q.pop();

        for (int i = 0; i < n; i++)
        {
            if (adj[curr][i])
            {
                if (!visited[i])
                {
                    visited[i] = true;
                    parent[i] = curr;
                    q.push(i);
                }
                else if (i != parent[curr])
                {
                    return true;
                }
            }
        }
    }
    return false;
}

int countConnectedComponents(vvi &adj)
{
    int n = adj.size();
    vi visited(n, false);
    int components = 0;

    for (int i = 0; i < n; i++)
    {
        if (!visited[i])
        {
            components++;
            queue<int> q;
            visited[i] = true;
            q.push(i);

            while (!q.empty())
            {
                int curr = q.front();
                q.pop();

                for (int j = 0; j < n; j++)
                {
                    if (adj[curr][j] && !visited[j])
                    {
                        visited[j] = true;
                        q.push(j);
                    }
                }
            }
        }
    }
    return components;
}

bool isTree(vvi &adj)
{
    int n = adj.size();
    vi visited(n, false);

    if (hasCycle(adj, 0, visited))
    {
        return false;
    }

    for (bool v : visited)
    {
        if (!v)
            return false;
    }

    return true;
}

int main()
{
    int n;
    while (cin >> n)
    {
        vvi adj(n, vi(n));

        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                cin >> adj[i][j];
            }
        }

        int components = countConnectedComponents(adj);

        bool allTrees = true;
        vi visited(n, false);

        for (int i = 0; i < n; i++)
        {
            if (!visited[i])
            {
                if (hasCycle(adj, i, visited))
                {
                    allTrees = false;
                    break;
                }
            }
        }

        if (components == 1 && allTrees)
        {
            cout << "It is a tree." << endl;
        }
        else if (components > 1 && allTrees)
        {
            cout << "It is forest." << endl;
        }
        else
        {
            cout << "It is not a tree." << endl;
        }
    }
    return 0;
}
