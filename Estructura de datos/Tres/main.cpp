#include <iostream>
#include <string>
#include <istream>
#include <sstream>
#include "include/Laberinto.h"
using namespace std;

int column =0;
int fila =0;


bool esNumero(string element){
    int j= 0;
    int i;
    if(element.length()==0){
        return false;
    }else{
        int e = element.length();
        for(i =0; i< e; i++){
            if(element.at(i)=='0'||element.at(i)=='1'||element.at(i)=='2'||element.at(i)=='3'||
                    element.at(i)=='4'||element.at(i)=='5'||element.at(i)=='6'||element.at(i)=='7'||
                    element.at(i)=='8'||element.at(i)=='9'){
                j++;
            }
        }return j==i;
    }
}


void ingresoDatos(){
    cout<<"BIENVENIDO AL PUEBLO LABERINTOS x3"<<endl;

    char cantF[256];
    char cantC[256];
    string cantFilas = "";
    string cantColumn = "";
    while(!esNumero(cantFilas)){

        cout <<"Introduzca cant. filas"<< endl;
        cin.getline(cantF,256);
        char *charF = &cantF[0];
        cantFilas = charF;
    }istringstream (cantFilas) >> fila;
    while (!esNumero(cantColumn)){
            cout <<"Introduzca cant. columnas"<< endl;
            cin.getline(cantC,256);
            char *charC = &cantC[0];
            cantColumn = charC;
        }istringstream (cantColumn) >> column;

    if(fila>1 && column>1){
        cout<<"DISFRUTE SU ESTANCIA!"<<endl;
        Laberinto* l = new Laberinto(fila,column);
        l->prim(fila,column);
    }else{
        cout<<"NO PUEDE INGRESAR. INTENTELO DE NUEVO"<<endl;
        cout<<"CON OTROS PARAMETROS"<<endl;
        cout<<""<<endl;
        ingresoDatos();
    }

}


int main()
{
    ingresoDatos();
    return 0;
}
