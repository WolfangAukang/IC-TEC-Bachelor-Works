#ifndef LQUEUE_H_INCLUDED
#define LQUEUE_H_INCLUDED
#include "Node.h"
using namespace std;

class LQueue
{
    private:
        Node* frontp;
        Node* rearp;
        int sizec;

    public:
        //Constructoor de colas//
        LQueue()
        {
            //Nodo* p = new Nodo(-1,-1);
            frontp = rearp = new Node();
            sizec = 0;
        }


        //Destructor de colas//
        ~LQueue()
        {
            clearqueue();
            delete frontp;
        }

        //Limpiador de colas//
        void clearqueue()
        {
            rearp = frontp->next;
            while (frontp->next != NULL){
                frontp->next = frontp->next->next;
                delete rearp;
                rearp = frontp->next;
            }
            rearp = frontp;
            sizec = 0;
        }

        //Insertar elemento en cola//
        void enqueue(Nodo insertar)
        {
            rearp->next =  new Node(insertar);
            rearp = rearp->next;
            sizec++;
        }

        //Eliminar elemento de la cola//
        Nodo dequeue()
        {
            if (sizec == 0)
            {
                return frontp->element;
            }
            else{
                Node* ltemp = frontp->next;
                frontp->next = ltemp->next;
                Nodo elem = ltemp->element;
                delete ltemp;
                sizec--;
                return elem;     //cout << elem << endl;
                }
        }

        //Retornar primer elemento de cola//
        Nodo frontvalue()
        {
            if (sizec == 0)
            {
                return frontp->element;
            }else{
                Nodo elem = frontp->next->element;
                return elem;
            }
        }

        //Retorna tamaño de cola//
        int length()
        {
            return sizec;
        }

        //Retorna elementos de cola//
        void checkelements()
        {
            if (sizec > 0){
            Node* ltemp = frontp->next;
            while (ltemp != NULL)
            {
                Nodo elem = ltemp->element;
                cout << elem.getPosFila() << " ";
                ltemp = ltemp->next;
            }
           }
        }

};

#endif // LQUEUE_H_INCLUDED
