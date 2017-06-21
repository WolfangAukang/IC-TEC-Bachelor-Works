#ifndef NODE_H_INCLUDED
#define NODE_H_INCLUDED
#include "Nodo.h"
using namespace std;

class Node
{
    public:
        Nodo element;
        Node* next;
        Node(Nodo pElement, Node* pNext = NULL) {
            element = pElement;
            next = pNext;
        }
        Node(Node* pNext = NULL) {
            next = pNext;
        }
};

#endif // NODE_H_INCLUDED
