#include <iostream>
using namespace std;

int cambiarpos(int *y, int *x){
    int z;
    z = *y;
    *y = *x;
    *x = z;
}

int main(){
    int a = 18, b = 13;
    cout << "a = " << a << " y b = " << b << endl;
    cambiarpos(&a, &b);
    cout << "a = " << a << " y b = " << b << endl;
}
