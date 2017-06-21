#include <iostream>
#define defaultSize 100
using namespace std;

template <typename E> class List{
private:
    void operator = (const List&) {}
    List(const List&) {}
public:
    List() {}
    virtual ~List() {}

    virtual void clear() = 0; //Limpia contenido de lista para dejarla vacía

    virtual void insert(const E& item) = 0; //Inserta un elemento en la posicion correspondiente

    virtual void append(const E& item) = 0; //Inserta un elemento al final de la lista

    virtual E remove() = 0; //Remueve y elimina el elemento correspondiente

    virtual void moveToStart() = 0; //Se establece la cabeza de la lista como la posición correspondiente

    virtual void moveToEnd() = 0; //Se establece la cola de la lista como la posición correspondiente

    virtual void prev() = 0; //Se mueve el indicador de la posición correspondiente a la izquierda

    virtual void next() = 0; //Se mueve el indicador de la posición correspondiente a la derecha

    virtual int length() const = 0; //Retorna la cantidad de elementos en la lista

    virtual int currPos() const = 0; //Retorna la posición del elemento correspondiente

    virtual void moveToPos(int pos) = 0; //Mueve el indicador hacia una posicion deseada

    virtual const E& getValue() const = 0; //Retorna el elemento de la posicion correspondiente
};

template <typename E>
class AList : public List<E> {
private:
    int maxSize; //Tamaño máximo de la lista
    int listSize; //Número actual de ítems
    int curr; //Posición correspondiente
    E* listArray; //Arreglo que sostiene elementos de la lista

public:
    AList(int size = defaultSize) { //Constructor
        maxSize = size;
        listSize = curr = 0;
        listArray = new E[maxSize];
    }

    ~AList() { delete [] listArray; } //Destructor

    void clear() {  //Reinicializa lista
        delete [] listArray; //Elimina arreglo
        listSize = curr = 0; //Resetea el tamaño
        listArray = new E[maxSize]; //Crea nuevo arreglo
    }

    void insert(const E& it) { //Inserta un elemento en la posición correspondiente
        Assert(listSize < maxSize, "List capacity exceeded");
        for(int i=listSize; i>curr; i--) //Mueve elementos hacia adelante
            listArray[i] = listArray[i-1];
        listArray[curr] = it;
        listSize++; //Incrementa tamaño de la lista
    }
};
