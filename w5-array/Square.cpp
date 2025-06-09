#include <iostream>
#include <algorithm>
using namespace std;

bool ok = false;
int MAP[50000] = {}, stick[50000] = {}, N;

void DFS(const int length, const int finish, const int add, const int start)
{
    if (finish == 3 || ok)
    {
        ok = true;
        return;
    }
    if (add == length)
    {
        DFS(length, finish + 1, 0, 0);
        return;
    }
    for (int i = start; i < N; i++)
    {
        if (MAP[i] == 0 && add + stick[i] <= length)
        {
            MAP[i] = 1;
            DFS(length, finish, add + stick[i], i + 1);
            MAP[i] = 0;
        }
        else if (stick[i] + add > length)
            return;
    }
}

int main()
{
    cin.sync_with_stdio(0);
    cin.tie(0);
    int T;
    cin >> T;
    for (int i = 0; i < T; i++)
    {
        int sum = 0, max = -999;
        cin >> N;
        ok = false;
        for (int j = 0; j < N; j++)
        {
            MAP[j] = 0;
        }
        for (int j = 0; j < N; j++)
        {
            cin >> stick[j];
            sum += stick[j];
            if (stick[j] > max)
                max = stick[j];
        }
        if (sum % 4 != 0 || max > sum / 4)
        {
            cout << "no\n";
            continue;
        }
        sort(stick, stick + N);
        DFS(sum / 4, 0, 0, 0);
        if (ok)
            cout << "yes\n";
        else
            cout << "no\n";
    }
}

// ZeroJudge D375
// Dr. SeanXD