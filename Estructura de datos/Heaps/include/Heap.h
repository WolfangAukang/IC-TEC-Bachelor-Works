#ifndef HEAP_H
#define HEAP_H

template <typename Key, typename E>
class HeapNode
{
    public:
        Key key;
        E element;
};

template <typename Key, typename E>
class MaxHeap
{
    private:
        int maxSize;
        int size;
        HeapNode<Key, E>* elements;
    public:
        MaxHeap(int pMaxSize){
            maxSize=pMaxSize;
            size=0;
            elements = new HeapNode<Key,E>[maxSize]
        }
        int leftChild(int pos){
            return 2*pos+1;
        }
        int rightChild(int pos){{
            return 2*pos+2;
        }
        int parent(int pos){
            if (pos <= o){
                return -1;
            }
            return (pos-1)/2;
        }
        bool isLeaf(int pos){
            return leftChild(pos) >= size;
        }
        void swap(int i,int j){
            E tempE = elements[i].element;
            Key tempK = elements[i].key;
            elements[i].element = elements[j].element;
            elements[i].key = elements[j].key;
            elements[j].element = tempE;
            elements[j].key = tempK;
        }
        void siftUp(int pos){
            int i = pos;
            while ((i > 0 ) && (elements[i].key > elements[parent(i)].key)){
                swap(i,parent(i));
                i = parent(i);
            }
        }
        void insert(Key k, E it) throw(runtime_error){
            if (size==maxSize){
                throw runtime_error("Full heap");
            }
            elements[size].key = k;
            elements[size].element = it;
            siftUp(size);
            size++;
        }
};

#endif // HEAP_H
