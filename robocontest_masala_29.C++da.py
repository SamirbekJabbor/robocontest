#include <iostream>
using namespace std;
int juft(int n){
    if(n % 2 == 1) return 0;
    n /=2;
    int c = 0;
    for(int i = 1; i * i <= n; i ++){
        if (n % i == 0){
             c ++;
             if(i != n / i) c++;
          }
    }
    return c;
}
int main(){
    int t, n;
    cin >> t;
    for(int i = 0; i < t; i ++){
        cin >> n;
        cout << juft(n) << endl;
    }
    return 0;
}
#29
