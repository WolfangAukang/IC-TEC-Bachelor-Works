#ifndef LQUEUE_H
#define LQUEUE_H

#include "Node.h"
#include <stdexcept>
using namespace std;

template <typename E>
class LQueue
{
    private:
        Node<E>* frontp;
        Node<E>* rearp;
        int sizec;

    public:
        //Constructoor de colas//
        LQueue()
        {
            frontp = rearp = new Node<E>();
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
        void enqueue(E insertar)
        {
            rearp->next =  new Node<E>(insertar);
            rearp = rearp->next;
            sizec++;
        }

        //Eliminar elemento de la cola//
        E dequeue() throw(runtime_error)
        {
            if (sizec == 0)
            {
                throw runtime_error("Empty queue");
            }
            Node<E>* ltemp = frontp->next;
            frontp->next = ltemp->next;
            E elem = ltemp->element;
            delete ltemp;
            sizec--;
            cout << "\n" << elem << "\n" << endl;
            if (frontp->next == NULL){
                rearp = frontp;
            }
        }

        //Retornar primer elemento de cola//
        E frontvalue() throw(runtime_error)
        {
            if (sizec == 0)
            {
                throw runtime_error("Empty queue");
            }
            E elem = frontp->next->element;
            return elem;
        }

        //Retorna tamaño de cola//
        int length()
        {
            return sizec;
        }

        //Retorna elementos de cola//
        E checkelements() throw(runtime_error)
        {
            if (sizec == 0)
            {
                throw runtime_error("Empty queue");
            }
            Node<E>* ltemp = frontp->next;
            while (ltemp != NULL)
            {
                E elem = ltemp->element;
                cout << elem << " ";
                ltemp = ltemp->next;
            }
        }

};

#endif // LQUEUE_H
