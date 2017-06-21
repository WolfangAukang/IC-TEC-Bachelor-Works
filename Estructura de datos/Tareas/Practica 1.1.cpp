#include <iostream>
#include <cstdlib>
using namespace std;

/*Multiplicador de matrices
Entrada: Datos de las dos matrices a crear
Salida: El resultado de la multiplicacion de las dos matrices
Restriccion: La cantidad de columnas de la primera matriz no puede ser diferente a la cantidad de filas de la segunda matriz*/

/*Funcion que construye las matrices*/
int producematriz(int fila, int columna)
{
    char opcion;
    bool validez = false;
    bool automatico = false;
    cout << fila << " " << columna << endl;
    while (!validez)
    {
        cout << "Desea crear la matriz manualmente? (s/n) ";
        cin >> opcion;
        if (opcion != 's' && opcion != 'n')
            cout << "Error! Opcion invalida!" << endl;
        else
        {
            validez = true;
            if (opcion == 'n')
                automatico = true;
            else
            {
                automatico = false;
            }
        }
    }
    int x = 0;
    int y = 0;
    int matriz[fila][columna];
    if (automatico != true)
    {
        while (y < fila)
        {
            int insertar = rand() % 25 + 1;
            matriz[y][x] = insertar;
            ++x;
            if (x == columna)
            {
                ++y;
                x = 0;
            }
        }
        while (y < fila)
        {
            cout << matriz[y][x] << " ";
            ++x;
            if (x == columna)
            {
                ++y;
                x = 0;
                cout << endl;
            }
        }
    }
    else
    {
        cout << "manual!";
    }
    return true;
}

/*Funcion que recibe datos de la matriz, para enviarselas al constructor*/
int creadormatriz()
{
    int totalColumnas1ra, totalFilas1ra, totalColumnas2da, totalFilas2da;
    cout << "Bienvenido al multiplicador de matrices!" << endl;
    cout << "\nFavor insertar la cantidad de filas y columnas de la primera matriz, respectivamente: ";
    cin >> totalFilas1ra >> totalColumnas1ra;
    cout << "\nElegiste una matriz de " << totalFilas1ra << " filas y de " << totalColumnas1ra << " columnas" << endl;
    cout << "\nAhora, favor insertar la cantidad de filas y columnas de la segunda matriz, respectivamente: ";
    cin >> totalFilas2da >> totalColumnas2da;
    cout << "\nElegiste una matriz de " << totalFilas2da << " filas y de " << totalColumnas2da << " columnas" << endl;
    if (totalColumnas1ra != totalFilas2da)
    {
        cout << "\nError, debes recordar que la cantidad de columnas de la primera matriz debe ser igual a la cantidad de filas de la segunda matriz." << endl;
        return false;
    }
    else
    {
        int matriz1 = producematriz(totalFilas1ra,totalColumnas1ra);
        return matriz1;
    }
}

int main()
{
    bool proximaFuncion = creadormatriz();
    if (proximaFuncion == true)
        cout << "Todo bien por ahora";
    else
    {
        cout << "\nFin";
    }
}
