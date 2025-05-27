#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main()
{
    int N;
    while (cin >> N)
    {
        if (N == 0)
        {
            cout << 0 << endl;
            continue;
        }
        queue<int> q;
        for (int i = 0; i < N; ++i)
        {
            int x;
            cin >> x;
            q.push(x);
        }
        while (q.size() > 1)
        {
            vector<int> v;
            while (!q.empty())
            {
                v.push_back(q.front());
                q.pop();
            }
            sort(v.begin(), v.end());
            int y = v.back();
            v.pop_back();
            int x = v.back();
            v.pop_back();
            if (y != x)
                v.push_back(y - x);

            for (int stone : v)
                q.push(stone);
        }
        if (q.empty())
            cout << 0 << endl;
        else
            cout << q.front() << endl;
    }
    return 0;
}