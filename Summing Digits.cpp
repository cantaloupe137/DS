// summing digits
#include <iostream>
using namespace std;

int solve(int n) {
    while (n >= 10) {
        int sum = 0;
        while (n > 0) {
            sum += n % 10;
            n /= 10;
        }
        n = sum;
    }
    return n;
}

int main() {
    while (true) {
        int n;
        cin >> n;
        if (n == 0) {
            break;
        }
        cout <<  solve(n) << endl;
    }
    return 0;
}