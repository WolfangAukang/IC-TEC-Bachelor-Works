#ifndef LABERINTO_H_INCLUDED
#define LABERINTO_H_INCLUDED
#include "Nodo.h"
#include <stdlib.h>
#include <ctime>
#include <algorithm>
#include <vector>       // std::vector
using namespace std;

class Laberinto{
    private:
        int nivel;
        int cantFila;
        int cantColum;
        Nodo** grafo;
        //Jugador* jugador;

    public:
         Laberinto(int  numFilas, int numColumnas){
            //jugador = new Jugador();
            nivel = 1;
            cantColum = numColumnas;
            cantFila = numFilas;
            grafo = crearGrafo(numFilas,numColumnas);
        }
        //Crea una matriz de Nodos sin relaciones y setea sus posiciones
        Nodo** crearGrafo(int pcantFila, int pcantColum){
            Nodo** grafoLocal = new Nodo*[pcantFila];
            for(int i = 0; i < pcantFila; i++){
              grafoLocal[i] = new Nodo[pcantColum];
            }
            for(int k=0; k < pcantFila; k++){
                for(int j=0; j< pcantColum; j++){
                    grafoLocal[k][j].setPosFila(k);
                    grafoLocal[k][j].setPosColum(j);
                }
            }
            cout<<"La creo"<<endl;
            return grafoLocal;
        }

 void hacerRelac(int filI, int colI, int tipoRelacion){
     if(tipoRelacion==0){
        //DERECHA
        grafo[filI][colI].setCamDer(true);
        grafo[filI][colI+1].setCamIzq(true);
     }
     else if(tipoRelacion==1){
        //IZQUIERDA
        grafo[filI][colI].setCamIzq(true);
        grafo[filI][colI-1].setCamDer(true);
     }
     else if(tipoRelacion==2){
        //ARRIBA
        grafo[filI][colI].setCamArriba(true);
        grafo[filI-1][colI].setCamAbajo(true);
     }
     else if(tipoRelacion==3){
        //ABAJO
        grafo[filI][colI].setCamAbajo(true);
        grafo[filI+1][colI].setCamArriba(true);
     }
     else{
         cout<<"No hay cambio de relaciones"<<endl;
     }
 }

    bool notInMatrix(int i, int j){
        if( (i<0) ||(i>=cantFila)){
            return true;
        }
        else if( (j<0) || (j>=cantColum) ){
                return true;
        }
        else{
            return false;
            }
    }

    int cualRelacion(int fInic, int cInic, int fFin, int cFin){
        if(notInMatrix(fInic,cInic)||notInMatrix(fFin,cFin)){
            return 4;
        }else{
        if(fInic==fFin){
            if(cInic+1==cFin){
                return 0;//Derecha
            }else if(cInic-1==cFin){
                return 1;//Izquierda
            }else{
                return 4;
            }
        }else if(cInic==cFin){
            if(fInic-1==fFin){
                return 2;//Arriba
            }else if(fInic+1==fFin){
                return 3;//Abajo
            }else{
                return 4;
            }
        }else{
            return 4;
        }
    }
}

bool todosRelacionados(){
    for(int i =0; i < cantFila; i++){
        for(int j =0; j < cantColum; j++){
            if(!grafo[i][j].getConectado()){
                return false;
            }
        }
    }return true;
}

    int getCantVecinos(int pFila, int pColum){
        int cantVecinos = 0;
        for(int i =0; i < 4; i++){
            if(i==0){
                if(cualRelacion(pFila,pColum,pFila,pColum-1)<4){
                    if(!grafo[pFila][pColum-1].getConectado()){
                        cantVecinos++;
                    }
                }
            }
            else if(i==1){
                if(cualRelacion(pFila,pColum,pFila,pColum+1)<4){
                    if(!grafo[pFila][pColum+1].getConectado()){
                        cantVecinos++;
                    }
                }
            }
            else if(i==2){
                if(cualRelacion(pFila,pColum,pFila+1,pColum)<4){
                    if(!grafo[pFila+1][pColum].getConectado()){
                        cantVecinos++;
                    }
                }
            }
            else{
                if(cualRelacion(pFila,pColum,pFila-1,pColum)<4){
                    if(!grafo[pFila-1][pColum].getConectado()){
                        cantVecinos++;
                    }
                }
            }
        }
        return cantVecinos;
    }

Nodo* obtenerVecinos(int pFila, int pColum){
        int cantVecinos = getCantVecinos(pFila,pColum);

        if(cantVecinos==0){return NULL;}
        else{
            Nodo* listaVecinos = new Nodo[cantVecinos];
            int indice=0;

        for(int i =0; i < 4; i++){
            if(i==0){
                if(cualRelacion(pFila,pColum,pFila,pColum-1)==1){
                        if(!grafo[pFila][pColum-1].getConectado()){
                            listaVecinos[indice]=grafo[pFila][pColum-1];
                            indice++;
                        }
                }
            }
            else if(i==1){
                if(cualRelacion(pFila,pColum,pFila,pColum+1)==0){
                    if(!grafo[pFila][pColum+1].getConectado()){
                        listaVecinos[indice]=grafo[pFila][pColum+1];
                        indice++;
                    }
                }
            }
            else if(i==2){
                if(cualRelacion(pFila,pColum,pFila+1,pColum)==3){
                    if(!grafo[pFila+1][pColum].getConectado()){
                        listaVecinos[indice]=grafo[pFila+1][pColum];
                        indice++;
                    }
                }
            }
            else{
                if(cualRelacion(pFila,pColum,pFila-1,pColum)==2){
                    if(!grafo[pFila-1][pColum].getConectado()){
                        listaVecinos[indice]=grafo[pFila-1][pColum];
                        indice++;
                    }
                }
            }
        }
        return listaVecinos;
    }
}

    int getRandom(int cantVecinos){
        return rand()%cantVecinos;
    }

    bool stuck(int filActual,int colActual){
        Nodo* listVecinos = obtenerVecinos(filActual,colActual);
        int cantVecinos = getCantVecinos(filActual,colActual);
        if(listVecinos==NULL){
            return true;
        }else if(cantVecinos==0){
            return true;
        }else{
            return false;
        }
    }

    Nodo backTrack(int filActual, int colActual){
        //int cantVecinos = getCantVecinos(filActual,colActual);
        int fil = filActual;
        int col = colActual;
        if(grafo[fil][col].hayCamAbajo()){
            return grafo[fil+1][col];
        }
        else if(grafo[fil][col].hayCamIzq()){
            return grafo[fil][col-1];
        }else if(grafo[fil][col].hayCamDer()){
            return grafo[fil][col+1];
        }else{
            return grafo[fil-1][col];
        }
    }


    void depthSearchAux(int filActual, int colActual){
        int  fActual = filActual;
        int cActual = colActual;
        grafo[fActual][cActual].setConectado(true);

        if(todosRelacionados()){}
        else{
            while(stuck(fActual,cActual)==false){
             cout<<"Stuck es false "<<endl;
            //OBTIENE LA CANT VECINOS
            int cantVecinos = getCantVecinos( fActual,cActual );
            cout<<cantVecinos<<endl;
            //OBTIENE LA LISTA DE VECINOS
            Nodo* listaVecinos = obtenerVecinos( fActual,cActual );

            //HACE UN RAND PARA ELEGIR AL VECINO
            int myRand = getRandom(cantVecinos);

            //SETEA LOS VALORES DEL VECINO
            int fVecino = listaVecinos[myRand].getPosFila();
            int cVecino = listaVecinos[myRand].getPosColum();
            cout<<fVecino<<" "<<cVecino<<endl;
            //BUSCA CUAL RELACION TENIAN LAS CELDAS
            int tipoRelacion= cualRelacion( fActual,cActual,fVecino,cVecino);
            cout<<tipoRelacion<<endl;
            //HACE EL TIPO DE RELACION ENTRE LAS CELDAS
            hacerRelac(fActual,cActual,tipoRelacion);
            cout<<"Hizo relacion"<<endl;
            //SETEA AL NODO VECINO COMO CONECTADO
            grafo[fVecino][cVecino].setConectado(true);
            cout<<"Puso como conectado"<<endl;
            //CAMBIA LOS VALORES DE LAS CELDAS
            fActual = fVecino;
            cActual = cVecino;
            cout<<"Cambio el actual"<<endl;
            if(!todosRelacionados()){
                        cout<<"Aun no relacionados"<<endl;
                        Nodo pasado = backTrack(fActual,cActual);
                        cout<<"hizo BACKTRACK "<<pasado.getPosFila()<<" "<<pasado.getPosColum()<<endl;
                        depthSearchAux(pasado.getPosFila(),pasado.getPosColum());
            }else{}
        }
    }

    }

    void depthSearch(){
        srand(time(NULL));
        depthSearchAux(0,0);
    }

    Nodo** getGrafo(){
        return grafo;
    }
};

#endif // LABERINTO_iH_INCLUDED
