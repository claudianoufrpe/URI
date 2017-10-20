// @author Matheus Alves dos Santos
// TITLE: Coloque Tijolos na Parede
// ID: 1426

#include <iostream>

using namespace std;

int main(){

    int n_testes, tijolos[9][9];
    
    cin >> n_testes;
    for (int k = 0; k < n_testes; k++) {
        
        for(int i = 0; i < 9; i += 2) {
            for(int j = 0; j <= i; j += 2) {
                cin >> tijolos[i][j];
            }
        }
        
        for(int i = 0; i < 7; i += 2) {
            for(int j = 0; j <= i; j += 2) {
                tijolos[i+2][j+1] = (tijolos[i][j] - tijolos[i+2][j] - tijolos[i+2][j+2]) / 2;
            }
        }
        
        for(int i = 1; i < 8; i += 2) {
            for(int j = 0; j <= i; j++) {
                tijolos[i][j] = (tijolos[i+1][j] + tijolos[i+1][j+1]);
            }
        }
        
        for(int i = 0; i < 9; i++) {
            for(int j = 0; j <= i; j++) {
                cout << tijolos[i][j];
                if (j < i) {
                    cout << " ";
                }
            }
            cout << endl;
        }
    }
    
    return 0;
}
