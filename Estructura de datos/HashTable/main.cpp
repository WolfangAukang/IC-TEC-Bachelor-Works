#include <iostream>
#include "include\HashTable.h"
#include <string>
#include <sstream>

using namespace std;

int main()
{
    HashTable<string, string> tablaHash;
    for (int i = 0; i < 500; i++) {
        if (i % 2 == 0) {
            ostringstream s;
            s << i;
            tablaHash.put(s.str(), "Número " + s.str());
        }
    }
    for (int i = 0; i < 500; i++) {
        try {
            ostringstream s;
            s << i;
            cout << i << " - " << tablaHash.get(s.str()) << endl;
        }
        catch (runtime_error e) {
            cout << i << " - No encontrado" << endl;
        }
    }
    return 0;
}
