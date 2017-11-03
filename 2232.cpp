// @author Matheus Alves dos Santos
// TITLE: Triângulo de Pascal
// ID: 2232

#include <iostream>
#include <cmath>

using namespace std;

int main() {
    int nTest, number;
    
    cin >> nTest;
    for(int i = 0; i < nTest; i++) {
        int sum = 0;
        
        cin >> number;
        while(number > 0) {
            sum += pow(2, number - 1);
            number--;
        }
            cout << sum << "\n" ;
    }
    
    return 0;
}
