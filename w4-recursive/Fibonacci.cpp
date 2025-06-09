#include <iostream>
using namespace std;
#define ll long long

ll fib(ll n)
{
    if (n <= 1)
        return n;
    return fib(n - 1) + fib(n - 2);
}

int main()
{
    ll n;
    while (cin >> n)
    {
        cout << fib(n) << endl;
    }
    return 0;
}