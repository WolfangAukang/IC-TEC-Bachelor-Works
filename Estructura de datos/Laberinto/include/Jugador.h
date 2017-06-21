#ifndef JUGADOR_H_INCLUDED
#define JUGADOR_H_INCLUDED

using namespace std;

class Jugador{
    private:
        bool vivo;
        int nivel;        // level
        int cantPistas;   // El jugador va a tener una cierta cantidad por default, pero podra ganar/perder
        int colectados; // Objetos que podra recoger en el transcurso del laberinto

    public:
        Jugador (){
            nivel  = 1;
            cantPistas = 0;
            colectados = 0;
            vivo = true;
        }

        //GETTERS
        int   getNivel()       {return nivel;}
        int   getCantPistas()  {return cantPistas;}
        int   getColectados()  {return colectados;}
        bool estaVivo()        {return vivo;}
        //SETTERS
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
        void setColectados(int colec){
            colectados = colec;
        }

        void setNumPistas(int pistas){
            cantPistas+= pistas;
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
