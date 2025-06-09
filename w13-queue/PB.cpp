#include <bits/stdc++.h>
using namespace std;
deque<pair<int, int>> v;
priority_queue<int> pq;
int main()
{
    int t, n, pos, m;
    cin >> t;
    while (t--)
    {
        v.clear();
        int ans = 0;
        bool flag = true;
        cin >> n >> pos;
        for (int i = 0; i < n; i++)
        {
            cin >> m;
            v.push_back(make_pair(m, i));
            pq.push(m);
        }
        while (flag)
            for (auto p : v)
            {
                if (p.first == pq.top())
                {
                    if (p.second == pos)
                    {
                        flag = false;
                        ans++;
                        break;
                    }
                    else
                    {
                        ans++;
                        pq.pop();
                        v.pop_front();
                    }
                }
                else
                {
                    v.push_back(v.front());
                    v.pop_front();
                }
            }
        cout << ans << endl;
        while (!pq.empty())
            pq.pop();
    }
}
