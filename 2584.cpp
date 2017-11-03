// @author Matheus Alves dos Santos
// TITLE: Pentágono
// ID: 2584

#include <iostream>
#include <cmath>

using namespace std;

int main() {    
    int nTest;
    double height, side, area;
    
    cin >> nTest;
    for(int i = 0; i < nTest; i++) {
        cin >> side;
        height = side / (2 * tan((36 * M_PI) / 180.0));
        area = 10 * ((side * height) / 4);
        
        cout.precision(3);
        cout.setf(ios::fixed);
        
        cout << fixed << area << endl;
    }
    
    return 0;
}
