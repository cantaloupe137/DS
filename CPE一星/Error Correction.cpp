#include <iostream>
using namespace std;
int main()
{

    int n;
    while (cin >> n)
    {
        int arr[100][100], row_sum = 0, col_sum = 0, p1 = 0, p2 = 0, row_count = 0, col_count = 0;
        if (n == 0)
            break; // terminate condition
        // input the two-dimensional array
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                cin >> arr[i][j];
            }
        }
        // add up the rows and check if it is even or odd
        // if it is odd, position + 1, count + 1
        // and if count > 1 break
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                row_sum += arr[i][j];
            }
            if (row_sum % 2 != 0)
            {
                row_count++;
                p1 = i;
                row_sum = 0;
            }
            if (row_count > 1)
                break;
            row_sum = 0;
        }

        // add up the columns and check if it is even or odd
        // if it is odd, position + 1, count + 1
        // and if count > 1 break
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                col_sum += arr[j][i];
            }
            if (col_sum % 2 != 0)
            {
                p2 = i;
                col_count++;
                col_sum = 0;
            }
            if (col_count > 1)
                break;
            col_sum = 0;
        }
        // if row and column's count are 0 then print OK
        // if row and column's count are 1 then print Change bit(i,j)
        // else print Corrupt
        if (row_count == 0 && col_count == 0)
            cout << "OK\n";
        else if (row_count == 1 && col_count == 1)
            cout << "Change bit(" << p1 + 1 << "," << p2 + 1 << ")\n";
        else
            cout << "Corrupt\n";
    }

    return 0;
}