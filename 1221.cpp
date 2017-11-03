// @author Matheus Alves dos Santos
// TITLE: Primo Rápido
// ID: 1221

#include <iostream>
#include <cmath>

using namespace std;

int main() {
    int number, nTests;
    
    cin >> nTests;
    
    for(int i = 0; i < nTests; i++) {
        cin >> number;
        bool isPrime = true;
        
        for(int j = 2; j <= sqrt(number); j++)
        {
            if(number % j == 0)
            {
                isPrime = false;
                break;
            }
        }
      
        if (isPrime) {
            cout << "Prime\n";
        } else {
            cout << "Not Prime\n";
        }
    }

    return 0;
}
