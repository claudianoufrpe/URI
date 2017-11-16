// @author Matheus Alves dos Santos
// TITLE: Onde está o Mármore?
// ID: 1025

#include <iostream>
#include <algorithm>

using namespace std;

int search(int numbers[], int len, int value) {
    for(int k = 0; k < len; k++) {
            if(numbers[k] == value) {
                     return (k + 1);
            }
    }
    
    return 0;
}

int main() {
    int size, n_tests, cases = 0;
    
    do {
        cin >> size >> n_tests;
        if((size != 0) && (n_tests != 0)) {
            int numbers[size], tests[n_tests];
            cases++;
        
            for(int i = 0; i < size; i++) {
                cin >> numbers[i];
            }
            sort(numbers, numbers + size);
        
            for(int j = 0; j < n_tests; j++) {
                cin >> tests[j];
            }
        
            cout << "CASE# " << cases << ":" << endl;
            for(int k = 0; k < n_tests; k++) {
                int a = search(numbers, size, tests[k]);
                
                if (a == 0) {
                    cout << tests[k] << " not found" << endl;
                } else {
                    cout << tests[k] << " found at " << a << endl;
                }
            }
        }
    } while ((size != 0) && (n_tests != 0));
    
    return 0;
}
