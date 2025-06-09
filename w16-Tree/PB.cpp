#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define pb push_back
#define pf push_front
#define ft first
#define sec second
#define pll pair<ll, ll>
#define pii pair<int, int>

int findDistance(vector<vector<int>> &graph, int start, int end, int n)
{
    vector<bool> visited(n + 1, false);
    vector<int> distance(n + 1, 0);
    queue<int> q;

    q.push(start);
    visited[start] = true;

    while (!q.empty())
    {
        int current = q.front();
        q.pop();

        if (current == end)
        {
            return distance[current];
        }

        for (int neighbor : graph[current])
        {
            if (!visited[neighbor])
            {
                visited[neighbor] = true;
                distance[neighbor] = distance[current] + 1;
                q.push(neighbor);
            }
        }
    }
    return -1;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    while (cin >> n)
    {
        int x, y;
        cin >> x >> y;
        cin.ignore();

        vector<vector<int>> graph(n + 1);

        for (int i = 0; i < n; i++)
        {
            string line;
            getline(cin, line);
            stringstream ss(line);
            int v0;
            ss >> v0;
            int v;
            while (ss >> v)
            {
                graph[v0].pb(v);
                graph[v].pb(v0);
            }
        }

        cout << findDistance(graph, x, y, n) << "\n";
        cout.flush();
    }

    return 0;
}
