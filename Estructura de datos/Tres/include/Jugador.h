#ifndef JUGADOR_H_INCLUDED
#define JUGADOR_H_INCLUDED

#include "Nodo.h"
using namespace std;

class Jugador{
    private:
        bool vivo;
        int nivel;        // level
        int cantPistas;   // El jugador va a tener una cierta cantidad por default, pero podra ganar/perder
        int colectados; // Objetos que podra recoger en el transcurso del laberinto
        Nodo* actual;     // Posicion del jugador dentro de laberinto
    public:
        Jugador(Nodo* _actual=NULL, int _cantPistas=3){
            nivel  = 1;
            cantPistas = _cantPistas;
            colectados = 0;
            actual = _actual;
            vivo = true;
        }

        //GETTERS
        Nodo* ubicacionActual(){return actual;}
        int   getNivel()       {return nivel;}
        int   getCantPistas()  {return cantPistas;}
        int   getColectados()  {return colectados;}
        bool estaVivo()        {return vivo;}
        //SETTERS
        void setUbicacionActual(Nodo* _actual){
            actual = _actual;
        }
            //ADD
        void setNivel(){
            nivel++;
        }
        void addPistas(){
            cantPistas++;
        }
        void addColectados(){
            colectados++;
        }
            //REMOVE
        void removePista(){
            if(cantPistas==0){
                die();
            }else{
                cantPistas--;
            }
        }
        void die(){
            vivo = false;
        }

};


#endif // JUGADOR_H_INCLUDED
