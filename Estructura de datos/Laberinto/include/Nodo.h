#ifndef NODO_H_INCLUDED
#define NODO_H_INCLUDED
#include "Jugador.h"
using namespace std;

class Nodo{
private:
   bool objeto;     //Si tiene algun objeto
   Jugador* jugador;    //Si el jugador esta posicionado en ese nodo
   int  posFila;
   int  posColum;
   bool camArriba;
   bool camAbajo;
   bool camIzq;
   bool camDer;
   bool conectado;
   bool visitado;
public:
    Nodo(int fila=0, int column =0){
        jugador = NULL;
        objeto = false;
        posFila = fila;
        posColum = column;
        camArriba = false;
        camAbajo = false;
        camIzq = false;
        camDer = false;
        conectado = false;
        visitado = false;
    }
    //GETTERS
    bool getVisitado(){
        return visitado;
    }
    bool hayCamArriba(){
        return camArriba;
    }
    bool hayCamAbajo(){
        return camAbajo;
    }
    bool hayCamIzq(){
        return camIzq;
    }
    bool hayCamDer(){
        return camDer;
    }
    int getPosFila(){
        return posFila;
    }
    int getPosColum(){
        return posColum;
    }
    bool hayObjeto(){
        return objeto;
    }
    bool hayJugador(){
        if(jugador!=NULL)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
    //SETTER
    void setVisitado(bool visita){
        visitado = visita;
    }
    void setJugador(Jugador* pjugador){
        jugador = pjugador;
    }
    void setObjeto(bool pobjeto){
        objeto = pobjeto;
    }
    void setPosFila(int pfila){
        posFila = pfila;
    }
    void setPosColum(int pcolum){
        posColum = pcolum;
    }
    void setCamArriba(bool conf){
        camArriba =conf;
    }
    void setCamAbajo(bool conf){
        camAbajo = conf;
    }
    void setCamIzq(bool conf){
        camIzq = conf;
    }
    void setCamDer(bool conf){
          camDer = conf;
    }
    bool getConectado(){
        return conectado;
    }
    void setConectado(bool conexion){
        conectado = conexion;
    }
    Jugador* getJugador(){
        return jugador;
    }
};


#endif // NODO_H_INCLUDED
