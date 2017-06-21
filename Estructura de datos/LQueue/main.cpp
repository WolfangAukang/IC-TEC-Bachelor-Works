#include <iostream>
#include "include\LQueue.h"
#include "include/Node.h"
#include <string>
using namespace std;

int main()
{
    //este método crea una lista, agrega tres elementos y luego la recorre con un ciclo
    LQueue<int> * cola = new LQueue<int>();
    cola->enqueue(5);
    cola->enqueue(10);
    cola->enqueue(20);
    cola->dequeue();
    cola->dequeue();
    cola->dequeue();
    cola->enqueue(20);
    cout << cola->length() << endl;
    cout << cola->frontvalue() << endl;
    if (cola->length() != 0)
    {
        cola->checkelements();
    }
    cout << endl;
    cola->dequeue();
    if (cola->length() != 0)
    {
        cola->checkelements();
    }
    return 0;
}
