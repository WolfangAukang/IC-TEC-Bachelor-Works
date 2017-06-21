#include <iostream>
using namespace std;

int main()
{
    int paso = 0;
    int fallo = 0;
    int estudiantes = 1;
    int resultado;

    while (estudiantes <= 10)
    {
        cout << "Favor insertar resultado (1=Paso, 2=Fallo):\n";
        cin >> resultado;
        if (resultado == 1)
            paso += 1;
        else
        {
            fallo += 1;
        }
        estudiantes = (1 + estudiantes);
    }

    cout << "Pasaron " << paso << "\nFallaron " << fallo << endl;
    if (paso >= 8)
        cout << "Instructor obtiene bonus!";

    return 0;
}

