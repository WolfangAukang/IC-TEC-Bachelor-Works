#include <iostream>

using std::cout;
using std::cin;
using std::endl;

int main()
{
    int num1, num2;

    cout << "Favor insertar dos numeros:\n";
    cin >> num1 >> num2;

    if (num1 == num2)
        cout << num1 << " == " << num2 << endl;

    if (num1 != num2)
        cout << num1 << " != " << num2 << endl;

    if (num1 > num2)
        cout << num1 << " > " << num2 << endl;

    if (num1 < num2)
        cout << num1 << " < " << num2 << endl;

    if (num1 >= num2)
        cout << num1 << " >= " << num2 << endl;

    if (num1 <= num2)
        cout << num1 << " <= " << num2 << endl;

    return 0;
}
