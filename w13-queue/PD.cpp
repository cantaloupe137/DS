#include <iostream>
#include<deque>
using namespace std;

int main() {
    int n, tmp;
    while(cin >> n){
        deque<int> former, later, ans;
        int left, right, train;
        bool flag = true;

        for(int i=0;i<n;i++){
            cin >> tmp;
            former.push_back(tmp);
        }
        for(int i=0;i<n;i++){
            cin >> tmp;
            later.push_back(tmp);
        }

        ans.push_back(former.front());
        former.pop_front();

        for(int i=0;i<n;i++){
            if(ans[0]==later[i]){
                left = right = i;
                break;
            }
        }

        for(int i=0;i<n-1;i++){
            train = former.front();
            former.pop_front();

            if((left-1)>=0 && later[left-1]==train){
                ans.push_front(train);
                left--;
            }
            else if((right+1)<n && later[right+1]==train){
                ans.push_back(train);
                right++;
            }else{
                flag = false;
                break;
            }


        }

        if(flag) cout << "Success" << endl;
        else cout << "Fail" << endl;
    }


    return 0;
}
