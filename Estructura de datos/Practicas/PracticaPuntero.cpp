#include <iostream>
#include <cstdlib>
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

/*Crea la matriz en la memoria dinámica*/
int** creadormatrices(int fila, int columna){
    int** matriz = new int*[fila];
    for(int i = 0; i < fila; i++){
      matriz[i] = new int[columna];
    }
    return matriz;

}
/*Pregunta al usuario si desea crear una matriz manualmente o no*/
bool consultarelleno(){
    char opcion;
    bool validez, automatico;
    validez = automatico = false;
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
    return automatico;
}

/*Rellena la matriz*/
void rellenamatrices(int** imp, int fila, int columna, bool autom){
    int insertar;
    if (autom == true){ //Creador automático 1
        for(int y = 0; y < fila; y++){
            for(int x = 0; x < columna; x++){
                insertar = rand()%25;
                imp[y][x] = insertar;
            }
        }
    }
    else{
        for(int y = 0; y < fila; y++){
            for(int x = 0; x < columna; x++){
                cout << "Favor insertar elemento de fila " << y+1 << " y columna " << x+1 <<": ";
                cin >> insertar; //Error
                cout << endl;
                imp[y][x] = insertar;
            }
        }

    }
}

/*Imprime la matriz*/
void impresormatrices(int** imp, int fila, int columna){
    for (int y = 0; y < fila; ++y){
        for (int x = 0; x < columna; ++x){
                cout << imp[y][x] << " ";  //Error
        }
        cout << endl;
    }
}

/*Limpia la matriz*/
void limpiarmatriz(int** imp, int fila, int columna){
    for (int i=0; i < fila; i++){
        delete imp[i];
    }
    delete imp;
}

/*Multiplica la matriz*/
void multiplicarmatrices(int** matriz1, int** matriz2, int** matrizR, int fila, int columna, int limite){
    int insertar, x, y, z;
    insertar = x = y = z = 0;
    while (x < fila){
        while (z < columna){
            while (y < limite){
                insertar += (matriz1[x][y] * matriz2[y][z]);
                ++y;
            }
            matrizR[x][z] = insertar;
            insertar = 0;
            y = 0;
            ++z;
        }
        ++x;
        z = 0;
    }
}

/*Función principal, que recibe datos sobre la cantidad de columnas y filas de las matrices a trabajar.
Esta confirma si los datos son válidos o no. Si lo son, se envían al constructor/multiplicador*/
int main(){
    int Columnas1, Filas1, Columnas2, Filas2;
    int** m1,** m2,** m3;
    cout << "Bienvenido al multiplicador de matrices!" << endl;
    cout << "\nFavor insertar la cantidad de filas y columnas de la primera matriz, respectivamente: ";
    cin >> Filas1 >> Columnas1;
    cout << "\nElegiste una matriz de " << Filas1 << " filas y de " << Columnas1 << " columnas" << endl;
    cout << "\nAhora, favor insertar la cantidad de filas y columnas de la segunda matriz, respectivamente: ";
    cin >> Filas2 >> Columnas2;
    cout << "\nElegiste una matriz de " << Filas2 << " filas y de " << Columnas2 << " columnas" << endl;
    if (Columnas1 != Filas2){
        cout << "\nError, debes recordar que la cantidad de columnas de la primera matriz debe ser igual a la cantidad de filas de la segunda matriz." << endl;
    }
    else{
        bool autom;
        m1 = creadormatrices(Filas1,Columnas1);
        m2 = creadormatrices(Filas2,Columnas2);
        m3 = creadormatrices(Filas1,Columnas2);
        autom = consultarelleno();
        rellenamatrices(m1, Filas1, Columnas1, autom);
        impresormatrices(m1, Filas1, Columnas1);
        cout << endl;
        autom = consultarelleno();
        rellenamatrices(m2, Filas2, Columnas2, autom);
        impresormatrices(m2, Filas2, Columnas2);
        cout << endl;
        multiplicarmatrices(m1,m2,m3,Filas1,Columnas2,Filas2);
        cout << "El resultado de la multiplicacion es igual a:\n" << endl;
        impresormatrices(m3, Filas1, Columnas2);
        cout << "Limpiando las matrices..." << endl;
        limpiarmatriz(m1, Filas1, Columnas1);
        limpiarmatriz(m2, Filas2, Columnas2);
        limpiarmatriz(m3, Filas1, Columnas2);
    }
}
