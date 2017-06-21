#include <iostream>
#include <cstdlib>
#include <time.h>
using namespace std;

/*------------------------------------------------------------------------------------------------
Código fuente realizado por Pedro Henrique Rodríguez de Oliveira
Estudiante del Instituto Tecnológico de Costa Rica
Carrera de Ingeniería en Computación
Carnet No. 2013086585
Curso de Estructuras de Datos
Profesor: Mauricio Avilés Cisneros
2014
------------------------------------------------------------------------------------------------*/

/*------------------------------------------------------------------------------------------------
Ejercicio escogido: Multiplicador de matrices
Entrada: Datos de las dos matrices a crear (cantidad de filas y columnas, además de su contenido)
Salida: El resultado de la multiplicación de las dos matrices creadas.
Restricción: La cantidad de columnas de la primera matriz no puede ser diferente a la cantidad de
filas de la segunda matriz, sino se indicará mensaje de error.
------------------------------------------------------------------------------------------------*/

/*Función que construye las matrices y las multiplica*/
int multiplicador(int fila1, int columna1, int fila2, int columna2)
{
    /*Variables con las cuales se construirá la matriz*/
    int matriz1[fila1][columna1], matriz2[fila2][columna2], matriz3[fila1][columna2];
    int x = 0;
    int y = 0;
    srand(time(0));
    /*Variables que confirman la respuesta del usuario en caso de crear manualmente o no la matriz*/
    char opcion;
    bool validez = false;
    bool automatico = false;
    while (validez == false){ //Pregunta de confirmación 1
        cout << "Desea crear la matriz 1 manualmente? (s/n) ";
        cin >> opcion;
        if (opcion != 's' && opcion != 'n')
            cout << "Error! Opcion invalida!" << endl;
        else{
            validez = true;
            if (opcion == 'n')
                automatico = true;
            else{
                automatico = false;
            }
        }
    }
    if (automatico == true){ //Creador automático 1
        while (y < fila1){
            int insertar = rand() % 25 + 1;
            matriz1[y][x] = insertar;
            ++x;
            if (x == columna1){
                ++y;
                x = 0;
            }
        }
    }
    else{ //Creador manual 1
        while (y < fila1){
            int insertar;
            cout << "Favor insertar elemento de fila " << (y+1) << " y columna " << (x+1) <<" : ";
            cin >> insertar;
            cout << endl;
            matriz1[y][x] = insertar;
            ++x;
            if (x == columna1){
                ++y;
                x = 0;
            }
        }
    }
    for (y = 0; y < fila1; ++y){ //Impresión de matriz 1
        for (x = 0; x < columna1; ++x){
                cout << matriz1[y][x] << " ";
        }
        cout << endl;
    }
    cout << endl;
    /*Reseteo de variables*/
    x = 0;
    y = 0;
    opcion = 'j';
    validez = false;
    automatico = false;
    while (validez == false){ //Pregunta de confirmación 2
        cout << "Desea crear la matriz 2 manualmente? (s/n) ";
        cin >> opcion;
        if (opcion != 's' && opcion != 'n')
            cout << "Error! Opcion invalida!" << endl;
        else{
            validez = true;
            if (opcion == 'n')
                automatico = true;
            else{
                automatico = false;
            }
        }
    }
    if (automatico == true){ //Creador automático 2
        while (y < fila2){
            int insertar = rand() % 25 + 1;
            matriz2[y][x] = insertar;
            ++x;
            if (x == columna2){
                ++y;
                x = 0;
            }
        }
    }
    else{ //Creador manual 2
        while (y < fila2){
            int insertar;
            cout << "Favor insertar elemento de fila " << (y+1) << " y columna " << (x+1) <<" : ";
            cin >> insertar;
            cout << endl;
            matriz2[y][x] = insertar;
            ++x;
            if (x == columna2){
                ++y;
                x = 0;
            }
        }
    }
    for (y = 0; y < fila2; ++y){ //Impresión de matriz 2
        for (x = 0; x < columna2; ++x){
                cout << matriz2[y][x] << " ";
        }
        cout << endl;
    }
    cout << endl;
    /*Reseteo de variables*/
    x = 0;
    y = 0;
    int z = 0;
    int insertar = 0;
    /*-------Proceso de multiplicación------*/
    while (x < fila1){
        while (z < columna2){
            while (y < fila2){
                insertar += (matriz1[x][y] * matriz2[y][z]);
                ++y;
            }
            matriz3[x][z] = insertar;
            insertar = 0;
            y = 0;
            ++z;
        }
        ++x;
        z = 0;
    }
    cout << "El resultado de la multiplicacion seria: " << endl;
    cout << endl;
    for (y = 0; y < fila1; ++y){ //Impresión de resultado (matriz 3)
        for (x = 0; x < columna2; ++x){
                cout << matriz3[y][x] << " ";
        }
        cout << endl;
    }
}

/*Función principal, que recibe datos sobre la cantidad de columnas y filas de las matrices a trabajar.
Esta confirma si los datos son válidos o no. Si lo son, se envían al constructor/multiplicador*/
int main()
{
    int totalColumnas1ra, totalFilas1ra, totalColumnas2da, totalFilas2da;
    cout << "Bienvenido al multiplicador de matrices!" << endl;
    cout << "\nFavor insertar la cantidad de filas y columnas de la primera matriz, respectivamente: ";
    cin >> totalFilas1ra >> totalColumnas1ra;
    cout << "\nElegiste una matriz de " << totalFilas1ra << " filas y de " << totalColumnas1ra << " columnas" << endl;
    cout << "\nAhora, favor insertar la cantidad de filas y columnas de la segunda matriz, respectivamente: ";
    cin >> totalFilas2da >> totalColumnas2da;
    cout << "\nElegiste una matriz de " << totalFilas2da << " filas y de " << totalColumnas2da << " columnas" << endl;
    if (totalColumnas1ra != totalFilas2da){
        cout << "\nError, debes recordar que la cantidad de columnas de la primera matriz debe ser igual a la cantidad de filas de la segunda matriz." << endl;
    }
    else{
        multiplicador(totalFilas1ra, totalColumnas1ra, totalFilas2da, totalColumnas2da);
    }
}
