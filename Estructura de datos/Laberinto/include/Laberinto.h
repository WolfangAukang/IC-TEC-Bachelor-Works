#ifndef LABERINTO_H_INCLUDED
#define LABERINTO_H_INCLUDED
#include "Nodo.h"
#include <stdlib.h>
#include <ctime>
#include <algorithm>
#include "LQueue.h"

using namespace std;

class Laberinto{
    private:
        int nivel;
        int cantFila;
        int cantColum;
        Nodo** grafo;

    public:
         Laberinto(int  numFilas, int numColumnas){
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

    void imprimirGrafo(){
        cout<<"\n IMPRESION"<<endl;
        for(int i =0; i < cantFila; i++){
            for(int j = 0; j < cantColum; j++){
                cout<<"\nFila: "<<i<<" Columna: "<<j<<endl;
                cout<<"\nAbajo: "<<grafo[i][j].hayCamAbajo();
                cout<<"\nArriba: "<<grafo[i][j].hayCamArriba();
                cout<<"\nDer: "<<grafo[i][j].hayCamDer();
                cout<<"\nIzq: "<<grafo[i][j].hayCamIzq()<<endl;
                cout<<grafo[i][j].getVisitado()<<endl;
                cout<<""<<endl;
            }
        }
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
            // cout<<"Stuck es false "<<endl;
            //OBTIENE LA CANT VECINOS
            int cantVecinos = getCantVecinos( fActual,cActual );
            //cout<<cantVecinos<<endl;
            //OBTIENE LA LISTA DE VECINOS
            Nodo* listaVecinos = obtenerVecinos( fActual,cActual );

            //HACE UN RAND PARA ELEGIR AL VECINO
            int myRand = getRandom(cantVecinos);

            //SETEA LOS VALORES DEL VECINO
            int fVecino = listaVecinos[myRand].getPosFila();
            int cVecino = listaVecinos[myRand].getPosColum();
            //cout<<fVecino<<" "<<cVecino<<endl;
            //BUSCA CUAL RELACION TENIAN LAS CELDAS
            int tipoRelacion= cualRelacion( fActual,cActual,fVecino,cVecino);
            //cout<<tipoRelacion<<endl;
            //HACE EL TIPO DE RELACION ENTRE LAS CELDAS
            hacerRelac(fActual,cActual,tipoRelacion);
            //cout<<"Hizo relacion"<<endl;
            //SETEA AL NODO VECINO COMO CONECTADO
            grafo[fVecino][cVecino].setConectado(true);
            //cout<<"Puso como conectado"<<endl;
            //CAMBIA LOS VALORES DE LAS CELDAS
            fActual = fVecino;
            cActual = cVecino;
            //cout<<"Cambio el actual"<<endl;
            if(!todosRelacionados()){
                // cout<<"Aun no relacionados"<<endl;
                Nodo pasado = backTrack(fActual,cActual);
                //cout<<"hizo BACKTRACK "<<pasado.getPosFila()<<" "<<pasado.getPosColum()<<endl;
                depthSearchAux(pasado.getPosFila(),pasado.getPosColum());
            }else{}
        }
    }

    }

    void depthSearch(){
        srand(time(NULL));
        depthSearchAux(1,1);
    }

    Nodo** getGrafo(){
        return grafo;
    }


    int* encontrarJugador(){
        int* par  = new int[2];
        par[0] = 0;
        par[1] = 0;
        for(int i = 0; i < cantFila; i++){
            for(int j = 0; j < cantColum; j++){
                if(grafo[i][j].hayJugador()){
                    par[0] = i;
                    par[1] = j;
                    return par;
                }
            }
        }return par;
    }

    int obtenerCantObjetos(){
        int objeto = 0;
        for(int i = 0; i < cantFila; i++){
            for(int j = 0; j < cantColum; j++){
                if(grafo[i][j].hayObjeto()){
                    objeto++;
                }
            }
        }return objeto;
    }

    int* ubicObjetos(){
        int cant = obtenerCantObjetos();
        int** ubicacion = new int*[cant];
        for(int k = 0; k < cant; k++){
            ubicacion[k] = new int[2];
        }
        for(int h = 0; h <cant; h++){
            for(int i = cantFila -1; i >= 0; i--){
                for(int j = cantColum -1; j >= 0; j--){
                if(grafo[i][j].hayObjeto()){
                        ubicacion[h][0] = i;
                        ubicacion[h][1] = j;
                    }
                }
            }
        }
        return ubicacion[0];
    }

    int* obtenerDestino(){
        if(obtenerCantObjetos()>0){
            int* fin = new int[2];
            fin[0] = ubicObjetos()[0];
            fin[1] = ubicObjetos()[1];
            return fin ;
        }else{
            int* fin = new int[2];
            fin[0] = cantFila-1;
            fin[1] = cantColum-1;
            return fin;
        }
}


    void clearVisitados(){
        for(int i = 0; i < cantFila; i++){
            for(int j = 0; j < cantColum; j++){
                grafo[i][j].setVisitado(false);
            }
        }
    }

    int** getMatrizLab(){
        int fMatriz = (cantFila*2)-1;
        int cMatriz = (cantColum*2)-1;
        int** matriz = new int*[fMatriz];

            for(int j=0; j <fMatriz;j++){
               matriz[j] = new int[cMatriz];
            }
        for(int q = 0; q < fMatriz; q++){
            for(int p = 0; p < cMatriz; p++){
                matriz[q][p] = 0;
            }
        }

        int fAct = 0;
        int cAct = 0;

        //int* destino = obtenerDestino();

        for(int m = 0; m < cantFila; ++m){
          for(int n = 0; n < cantColum; ++n){
           for(int o = 0; o < 4; o++){
                cout<<"m "<<m<<" n "<<n<<" f "<<fAct<<" c "<<cAct<<endl;
                if(o==0){
                    if(grafo[m][n].hayCamAbajo()){
                        matriz[fAct][cAct]  = 1;
                        matriz[fAct+1][cAct]= 1;
                    }
                }else if(o==1){
                    if(grafo[m][n].hayCamArriba()){
                        matriz[fAct][cAct]  = 1;
                        matriz[fAct-1][cAct]= 1;
                    }
                }else if(o==2){
                    if(grafo[m][n].hayCamIzq()){
                        matriz[fAct][cAct]  = 1;
                        matriz[fAct][cAct-1]= 1;
                    }
                }else{// if(o==3){
                    if(grafo[m][n].hayCamDer()){
                        matriz[fAct][cAct]  = 1;
                        matriz[fAct][cAct+1]= 1;
                    }
                //}else{
                //    if((destino[0]==m) && (destino[1]==n))
                //}
                }
            }cAct+=2;
        }fAct+=2;
        cAct=0;
    }
    for(int qe = 0; qe < fMatriz; qe++){
            for(int pe = 0; pe < cMatriz; pe++){
                cout<<matriz[qe][pe];
            }cout<<endl;
    }return matriz;
}

    bool noHayMasConexiones(Nodo pNodo){
     return cantVecinosNoVisitados(pNodo) <= 0;
    }

    int cantVecinosNoVisitados(Nodo pNodo){
            int i = 0;
        if(pNodo.hayCamAbajo()){
            if( grafo[pNodo.getPosFila()+1][pNodo.getPosColum()].getVisitado()==false){
                i++;
            }
        }
        if(pNodo.hayCamArriba()){
            if(grafo[pNodo.getPosFila()-1][pNodo.getPosColum()].getVisitado()==false){
                i++;
            }
        }
        if(pNodo.hayCamDer()){
            if(grafo[pNodo.getPosFila()][pNodo.getPosColum()+1].getVisitado()==false){
             i++;
            }
        }
        if(pNodo.hayCamIzq()){
            if(grafo[pNodo.getPosFila()][pNodo.getPosColum()-1].getVisitado()==false){
              i++;
            }
        }
        return i;
    }

    LQueue* getVecinosNoVisitados(Nodo pNodo){
        LQueue* listaVecinos= new LQueue();
        if(pNodo.hayCamAbajo()){
            if( grafo[pNodo.getPosFila()+1][pNodo.getPosColum()].getVisitado()==false){
                listaVecinos->enqueue(grafo[pNodo.getPosFila()+1][pNodo.getPosColum()]);
            }
        }
        if(pNodo.hayCamArriba()){
            if(grafo[pNodo.getPosFila()-1][pNodo.getPosColum()].getVisitado()==false){
                listaVecinos->enqueue(grafo[pNodo.getPosFila()-1][pNodo.getPosColum()]);
            }
        }
        if(pNodo.hayCamDer()){
            if(grafo[pNodo.getPosFila()][pNodo.getPosColum()+1].getVisitado()==false){
             listaVecinos->enqueue(grafo[pNodo.getPosFila()][pNodo.getPosColum()+1]);
            }
        }
        if(pNodo.hayCamIzq()){
            if(grafo[pNodo.getPosFila()][pNodo.getPosColum()-1].getVisitado()==false){
              listaVecinos->enqueue(grafo[pNodo.getPosFila()][pNodo.getPosColum()-1]);
            }
        }
        return listaVecinos;
    }

    int numPasosRecorridoAux(Nodo pNodo, Nodo buscado){
        if((pNodo.getPosFila()==buscado.getPosFila()) && (pNodo.getPosColum()==buscado.getPosColum())){
            return 0;
        }else{
            return numPasosRecorrido(pNodo, buscado);
        }
    }


    int numPasosRecorrido(Nodo pNodo, Nodo buscado){
        grafo[pNodo.getPosFila()][pNodo.getPosColum()].setVisitado(true);
        if( (pNodo.getPosFila()==buscado.getPosFila()) && (pNodo.getPosColum()==buscado.getPosColum()) ){
            return 1;
        }
        else if(noHayMasConexiones(pNodo)){
                cout<<"F "<<pNodo.getPosFila()<<" C "<<pNodo.getPosColum()<<endl;
            return 0;
        }
        else{
            LQueue* vecinos = getVecinosNoVisitados(pNodo);
            if(cantVecinosNoVisitados(pNodo)==1){
                Nodo vecino1 = vecinos->dequeue();
                grafo[vecino1.getPosFila()][vecino1.getPosColum()].setVisitado(true);
                return 1 + numPasosRecorridoAux(vecino1,buscado);
            }
            else if(cantVecinosNoVisitados(pNodo)==2){
                Nodo vecino1 = vecinos->dequeue();
                Nodo vecino2 = vecinos->dequeue();
                grafo[vecino1.getPosFila()][vecino1.getPosColum()].setVisitado(true);
                grafo[vecino2.getPosFila()][vecino2.getPosColum()].setVisitado(true);
                return numPasosRecorridoAux(vecino1,buscado) + numPasosRecorridoAux(vecino2,buscado);
            }
            else if(cantVecinosNoVisitados(pNodo)==3){
                Nodo vecino1 = vecinos->dequeue();
                Nodo vecino2 = vecinos->dequeue();
                Nodo vecino3 = vecinos->dequeue();
                grafo[vecino1.getPosFila()][vecino1.getPosColum()].setVisitado(true);
                grafo[vecino2.getPosFila()][vecino2.getPosColum()].setVisitado(true);
                grafo[vecino3.getPosFila()][vecino3.getPosColum()].setVisitado(true);
                return numPasosRecorridoAux(vecino1,buscado)+ numPasosRecorridoAux(vecino2,buscado) + numPasosRecorridoAux(vecino3,buscado);
            }else{
                Nodo vecino1 = vecinos->dequeue();
                Nodo vecino2 = vecinos->dequeue();
                Nodo vecino3 = vecinos->dequeue();
                Nodo vecino4 = vecinos->dequeue();
                grafo[vecino1.getPosFila()][vecino1.getPosColum()].setVisitado(true);
                grafo[vecino2.getPosFila()][vecino2.getPosColum()].setVisitado(true);
                grafo[vecino3.getPosFila()][vecino3.getPosColum()].setVisitado(true);
                grafo[vecino4.getPosFila()][vecino4.getPosColum()].setVisitado(true);
                return numPasosRecorridoAux(vecino1,buscado)+ numPasosRecorridoAux(vecino2,buscado)
                 + numPasosRecorridoAux(vecino3,buscado) + numPasosRecorridoAux(vecino4,buscado);
            }
        }
    }

    bool hayCamino(Nodo pNodo, Nodo buscado){
        return numPasosRecorrido(pNodo,buscado) >= 1;
    }

};

#endif // LABERINTO_iH_INCLUDED
