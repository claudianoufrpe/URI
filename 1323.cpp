// @author Matheus Alves dos Santos
// TITLE: Feynman
// ID: 1323

#include <iostream>
#include <cmath>

using namespace std;

int main() {
    int n;
    while (true){
        cin >> n;
        if (n == 0) {
            break;
        }
        
        int sum = 0;
        while(n > 1) {
            sum += pow(n, 2);
            n--;
        }
        sum ++;
        cout << sum ;
    }

    return 0;
}
