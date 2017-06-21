#ifndef HASHTABLE_H
#define HASHTABLE_H
#include "HashNode.h"
#include "LinkedList.h"
#include <stdexcept>
#include <math.h>
#include <cstdlib>

using namespace std;

template <typename Key, typename E>
class HashTable
{
private:
    int maxSize;
    int size;
    LinkedList<Key, E>* elements;

    // Función hash
    int h(Key pKey) {
        return compress(hashCodeCyclicShift(pKey));
    }
    // Genera un código hash polinomial con constante de 33
    int hashCodePolynomial(Key pKey) {
        int a = 33;
        int result = 0;
        while (pKey != 0)
        return result;
    }
    // Gemera un código hash con corrimiento cíclico con corrimientos
    // de 7 hacia la izquierda y 25 a la derecha. Usa XOR para unir
    // los bits.
    template <typename T>
    int hashCodeCyclicShift(T pKey) {
        int result = 0;
        char* bytes = reinterpret_cast<char*>(&pKey);
        for (unsigned int i = 0; i < sizeof(pKey); i++) {
            result = (result << (7)) ^ (result >> (25));
            result += (int) bytes[i];
        }
        return result;
    }
    // Caso especial de la misma función para strings
    int hashCodeCyclicShift(string pKey) {
        int result = 0;
        for (unsigned int i = 0; i < pKey.length(); i++) {
            result = (result << (7)) ^ (result >> (25));
            result += (int) pKey.at(i);
        }
        return result;
    }
    // Función de compresión por multiplicación, suma y división
    int compress(int pHashCode) {
        int a = 1097;
        int b = 1279;
        // ...
    }
    // Función que dibuja los bits de un entero, para propósitos
    // de prueba
    void printBits(int n) {
        int value = n;
        string result = "";
        for (int i = 0; i < 32; i++) {
            result = (value % 2? "o" : "_") + result;
            value = value / 2;
        }
        cout << result << endl;
    }

public:
    HashTable(int pMaxSize = 1021) {
        maxSize = pMaxSize;
        elements = new LinkedList<Key,E>[maxSize];
        size = 0;
    }
    ~HashTable() {
        delete [] elements;
    }
    // Retorna true si la llave indicada se encuentra
    // en la tabla hash.
    bool containsKey(Key pKey) {
        return elements[h(pKey)].containsKey(pKey);
    }
    // Inserta un nuevo par llave valor.
    // Lanza excepción si la llave ya se encuentra en
    // la tabla hash.
    void put(Key pKey, E pElement) throw(runtime_error) {
        if (elements[h(pKey)].containsKey(pKey)) {
            throw runtime_error("Key already exists.");
        }
        // ...
    }
    // Actualiza el elemento asociado a la llave indicada.
    // Lanza excepción si la llave no se encuentra.
    void set(Key pKey, E pElement) throw(runtime_error) {
        if (!(elements[h(pKey)].containsKey(pKey))) {
            throw runtime_error("Key not found.");
        }
        // ...
    }
    // Retorna el elemento asociado a la llave indicada.
    // Lanza excepción si la llave no se encuentra.
    E get(Key pKey) throw(runtime_error) {
        if (!(elements[h(pKey)].containsKey(pKey))) {
            throw runtime_error("Key not found.");
        }
        // ...
    }
    // Elimina el nodo con la llave indicada.
    // Lanza excepción si la llave no se encuentra.
    E remove(Key pKey) throw(runtime_error) {
        if (!(elements[h(pKey)].containsKey(pKey))) {
            throw runtime_error("Key not found.");
        }
        // ...
    }
    // Retorna la cantidad de nodos en la tabla hash.
    int getSize() {
        return size;
    }
};

#endif // HASHTABLE_H
