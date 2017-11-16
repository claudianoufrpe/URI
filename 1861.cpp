// @author Matheus Alves dos Santos
// TITLE: O Hall dos Assassinos
// ID: 1861

#include <iostream>
#include <map> 

using namespace std;

int main() {
    map <string, int> who_kills;
    map <string, int> who_dies;
    
    map<string, int> :: iterator it;
    
    string murder, murdered;
    int tst;
    
    while (cin >> murder >> murdered) {
        who_kills[murder]++;
        who_dies[murdered]++;
    }
    
    cout << "HALL OF MURDERERS" << endl;
    for(it = who_kills.begin(); it != who_kills.end(); it++) {
        tst = who_dies[it->first];
        
        if (!tst) {
            cout << it->first << " " << it->second << endl;
        }
    }
    who_kills.clear();
    who_dies.clear();
    
    return 0;
}
