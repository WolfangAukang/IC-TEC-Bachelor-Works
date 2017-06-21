#include <iostream>
using namespace std;

/*Entrada: Dos numeros, sea entero o flotantes
Salida: La suma, producto, diferencia y cociente entre el primer y el segundo numero
Restricciones: No se deben insertar caracteres*/
int algebraica()
{
    float num1,num2;
    cout << "Favor insertar dos numeros:\n";
    cin >> num1 >>num2;
    float suma = (num1 + num2);
    float producto = (num1 * num2);
    float diferencia = (num1 - num2);
    float cociente = (num1 / num2);
    cout << "La suma es igual a " << suma << "\nEl producto es igual a " << producto << "\nLa diferencia es igual a " << diferencia << "\nY el cociente es igual a " << cociente << endl;
}
/*Entrada: Un numero entero, equivalente al radio
Salida: El diametro, circunferencia y area del circulo con tal cantidad de radio
Restricciones: No se puede insertar flotantes ni caracteres*/
int circulo()
{
    const float PI = 3.14159;
    int radio;
    cout << "Favor insertar radio del circulo:\n";
    cin >> radio;
    int diametro = (radio * 2);
    float circunf = (2 * PI * radio);
    float area = (PI * radio * radio);
    cout << "El diametro es igual a " << diametro << "\nLa circunferencia es igual a " << circunf << "\nY el area es igual a " << area << endl;
}
/*Entrada:
Salida:
Restricciones:*/
int triangulo()
{
    float a,b,c;
    cout << "Favor insertar los dos catetos del triangulo: ";
    cin >> a >> b;
    cout << "Ahora inserte la hipotenusa: ";
    cin >> c;
    float catetoSuma = ((a * a)+(b * b));
    if (catetoSuma == (c * c))
        cout << "Es un triangulo rectangulo!";
    else
        cout << "No es un triangulo rectangulo";
}
/*Entrada:
Salida:
Restricciones:*/
int palindromo()
{
    int entrada;
    cout << "Favor insertar numero de comprobacion: ";
    cin >> entrada;
    int modificado = entrada;
    int comprobacion = 0;
    while (modificado != 0)
    {
        comprobacion *= 10;
        comprobacion += (modificado % 10);
        modificado /= 10;
    }
    if (comprobacion == entrada)
        cout << "Es un palindromo";
    else
        cout << "No es un palindromo";
}
/*Entrada:
Salida:
Restricciones:*/
int productoPar()
{
    /*Pedir datos generales de la lista*/
    int cantElementos;
    cout << "Favor insertar la cantidad de elementos de la lista de numeros: ";
    cin >> cantElementos;
    int lista[cantElementos];
    int posicion;
    /*Insercion de elementos en la lista*/
    for (posicion = 0; posicion < cantElementos; ++posicion)
    {
        int elemento;
        cout << "Favor insertar elemento: ";
        cin >> elemento;
        lista[posicion]=elemento;
    }
    /*Algoritmo de busqueda de numeros cuyo producto sea par*/
    int averiguador = 1;
    int producto;
    posicion = 0;
    while (posicion < (cantElementos - 1))
    {
        producto = (lista[posicion] * lista[averiguador]);
        if (producto % 2 == 0)
        {
            cout << "Existe un par de elementos cuya multiplicacion es par" << endl;
            break;
        }
        else if ((averiguador + 1) == cantElementos)
        {
            ++posicion;
            averiguador = (posicion + 1);
            if ((posicion == cantElementos - 1))
            {
                cout << "No existe un par de elementos cuya multiplicacion es par" << endl;
                break;
            }
        }
        else
        {
            ++averiguador;
        }
    }
}
/*Entrada:
Salida:
Restricciones:*/
int insercion()
{
    int lista[20];
    /*Insercion de datos en lista*/
    int posicion = 0;
    int elemento;
    while (posicion < 20)
    {
        cout << "Favor insertar un numero entre el 10 y el 100 (" << (posicion+1) << "): ";
        cin >> elemento;
        if (elemento >= 10 && elemento <= 100)
        {
            lista[posicion]=elemento;
            ++posicion;
        }
        else
        {
            cout << "Numero no valido, insertarlo de nuevo" << endl;
        }

    }
    cout << endl;
    /*Busqueda de elementos repetidos de la lista*/
    posicion = 0;
    int averiguador = 1;
    bool repeticion = false;
    while (posicion < 19)
    {
        if (lista[posicion] == lista[averiguador] && (lista[posicion] != 0 || lista[averiguador] != 0))
        {
            lista[averiguador] = 0;
            repeticion = true;
        }
        ++averiguador;
        if (averiguador == 20)
        {
            if (repeticion == true)
            {
                lista[posicion] = 0;
            }
            ++posicion;
            repeticion = false;
            while (lista[posicion] == 0)
            {
             ++posicion;
            }
            averiguador = (posicion + 1);
        }
    }
    /*Impresion de elementos no repetidos*/
    for (posicion = 0; posicion < 20; ++posicion)
    {
        if (lista[posicion] != 0)
        {
            cout << lista[posicion] << " ";
        }
    }
}
/*Entrada:
Salida:
Restricciones:*/
int ordenarRandom()
{
    int lista[52];
    int num;
    for (num = 0; num < 52; ++num)
    {
        lista[num] = num + 1;
    }
    int listaSalida[52];
    while
}

int main()
{
    ordenarRandom();
}
