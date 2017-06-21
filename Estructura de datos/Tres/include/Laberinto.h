#ifndef LABERINTO_H_INCLUDED
#define LABERINTO_H_INCLUDED
#include "Nodo.h"
#include "Jugador.h"
#include <stdlib.h>     /* srand, rand */
#include <time.h>       /* time */
using namespace std;

class Laberinto{
    private:
        int nivel;
        Nodo** grafo;
        Nodo** laberinto;
        Jugador* jugador;
    public:
        Laberinto(int cantFila, int cantColum){
            nivel = 1;
            jugador = new Jugador();
            grafo = creaGrafo(cantFila*cantColum,true);
        }

        Nodo** creaGrafo(int cantElement, bool camino){
            Nodo** grafo = new Nodo*[cantElement];
            for(int i = 0; i < cantElement; i++){
              grafo[i] = new Nodo[cantElement];
            }
            for(int k =0; k < cantElement; k++){
                for(int j =0;j < cantElement; j++){
                        grafo[k][j].setX(k);
                        grafo[k][j].setY(j);
                        if(k==j){
                            grafo[k][j].setCamino(true);
                        }else{
                            grafo[k][j].setCamino(camino);
                        }
                    cout<<grafo[k][j].hayCamino()<<endl;
                }
            }
            cout<<endl;
            grafo[0][0].setInicial();
            cout<<grafo[0][0].esInicial()<<endl;
            grafo[cantElement-1][cantElement-1].setFinal();
            cout<<grafo[cantElement-1][cantElement-1].esFinal()<<endl;
            cout<<endl;
            cout<<cantElement<<endl;
            return grafo;
        }
        bool estaArcoVacia(int cant, Nodo* arco){
            int j =0;
            for(int i =0; i < cant; i++){
                if(arco[i]==NULL){
                    j++;
                }
            }
            return i==j;
        }
        void prim(int cantFila, int cantColum){
            Nodo** grafo = creaGrafo(cantFila*cantColum,false);
            Nodo inicial = grafo[0][0];
            Nodo* arcos  = getNodosPosibles(grafo,0,0,cantFila,cantColum);
            srand (time(NULL));
            if(!estaArcoVacia(4,arcos)){
                int escogido = primAux(arcos);//0,1,2,3

            }
        }
        int primAux(Nodo* arcos){
            srand(time(NULL));
            int indice = rand()%4;
            if(arcos[indice]==NULL){
                return primAux(arcos);
            }else{
                return indice;
            }
        }

        bool estaEnLista(Nodo* arcos,int posFila, int posColum, int sizeActual){
            for(int i =0; i < sizeActual;i++){
                if((arcos[i].getX()==posFila)&&(arcos[i].getY()==posColum)){
                    return true;
                }
            }return false;
        }

        Nodo* getNodosPosibles(Nodo** grafo, int posFila, int posColum, int cantFila, int cantColum){
            cantColum--;
            cantFila--;
            Nodo* arcos = new Nodo[4];
            int cantInsert = 0;
            for(int i=0; i< cantFila+1; i++){
                for(int j=0; j< cantColum+1; j++){
                    if((posFila-1>=0)&&(posColum==j)&&(!estaEnLista(arcos,posFila-1,posColum,cantInsert))){
                        arcos[cantInsert]=  grafo[posFila-1][posColum];
                        cantInsert++;
                        cout<<"1. Fila: "<<posFila-1<<"Colum: "<<posColum<<endl;
                        cout<<"1. Fila: "<<arcos[cantInsert-1].getX()<<"Colum: "<<arcos[cantInsert-1].getY()<<endl;
                    }
                    else if((posFila+1<=cantFila)&&(posColum==j)&&(!estaEnLista(arcos,posFila+1,posColum,cantInsert))){
                        arcos[cantInsert]= grafo[posFila+1][posColum];
                        cantInsert++;
                        cout<<"2. Fila: "<<posFila+1<<"Colum: "<<posColum<<endl;
                        cout<<"2. Fila: "<<arcos[cantInsert-1].getX()<<"Colum: "<<arcos[cantInsert-1].getY()<<endl;
                    }
                    else if((posFila==i)&&(posColum+1<=cantColum)&&(!estaEnLista(arcos,posFila,posColum+1,cantInsert))){
                        arcos[cantInsert]= grafo[posFila][posColum+1];
                        cantInsert++;
                        cout<<"3. Fila: "<<posFila<<"Colum: "<<posColum+1<<endl;
                        cout<<"3. Fila: "<<arcos[cantInsert-1].getX()<<"Colum: "<<arcos[cantInsert-1].getY()<<endl;
                    }
                    else if((posFila==i)&&(posColum-1>=0)&&(!estaEnLista(arcos,posFila,posColum-1,cantInsert))){
                        arcos[cantInsert]= grafo[posFila][posColum-1];
                        cantInsert++;
                        cout<<"4. Fila: "<<posFila<<"Colum: "<<posColum-1<<endl;
                        cout<<"4. Fila: "<<arcos[cantInsert-1].getX()<<"Colum: "<<arcos[cantInsert-1].getY()<<endl;
                    }
                    else{}
                }
            }
            if(cantInsert==0){return NULL;}
            else{
                    //3
                for(int i=cantInsert; i < 4; i++){
                    arcos[i]= NULL;
                }
                cout<<"Insertados en arcos "<<cantInsert<<endl;
            return finalArcos;
            }

        }

};

#endif // LABERINTO_H_INCLUDED
