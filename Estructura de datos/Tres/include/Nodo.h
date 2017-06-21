#ifndef NODO_H_INCLUDED
#define NODO_H_INCLUDED
using namespace std;

class Nodo{
private:
    bool adyacencia; //camino
    bool inicial;    //Si es el nodo inicial
    bool fin;        //Si es el nodo final
    bool pista;      //Si tiene una pista o no
    bool objeto;     //Si tiene algun objeto
    bool jugador;    //Si el jugador esta posicionado en ese nodo
   int  posicionX;
   int  posicionY;
public:
    Nodo(){//int posX, int posY){
        adyacencia= jugador = false;
        inicial= fin = objeto = pista= false;
        //posicionX = posX;
        //posicionY = posY;
    }

    //GETTERS
    bool hayCamino() {return adyacencia;}
    bool esInicial() {return inicial;}
    bool esFinal()   {return fin;}
    bool hayObjeto() {return objeto;}
    bool hayPista()  {return pista;}
    bool hayJugador(){return jugador;}

    int  getX()      {return posicionX;}
    int  getY()      {return posicionY;}

    //SETTERS
    void setCamino(bool adyacente){
        adyacencia = adyacente;
    }
    void eliminarCamino(){
        setCamino(false);
    }
    void crearCamino(){
        setCamino(true);
    }
    void setInicial(){
        inicial = true;
    }
    void setFinal(){
        fin = true;
    }
    void setJugador(bool estaJugador){
        jugador= estaJugador;
    }
    void setX(int posX){posicionX = posX;}
    void setY(int posY){posicionY = posY;}

        //ADD y REMOVE
    void addPista(){
        pista = true;
    }
    bool removePista(){
        bool eliminado = pista;
        pista = false;
        return eliminado;
    }
    void addObjeto(){
        objeto = true;
    }
    bool removeObjeto(){
        bool eliminado = objeto;
        objeto = false;
        return eliminado;
    }

};


#endif // NODO_H_INCLUDED
