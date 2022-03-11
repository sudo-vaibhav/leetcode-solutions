
struct Node
{
    Node *prev, *next;
    int val;

public:
    Node()
    {
        prev = NULL;
        next = NULL;
        val = INT_MAX;
    }
    Node(int k)
    {
        prev = NULL;
        next = NULL;
        val = k;
    }
};
struct List
{
    Node *head, *tail;
    int size;

public:
    List()
    {
        head = new Node();
        tail = new Node();
        head->next = tail;
        tail->prev = head;
        size = 0;
    }

    Node *pushFront(int key)
    {
        Node* node = new Node(key);
        node->prev = head;
        node->next = head->next;
        node->next->prev = node;
        head->next = node;
        size++;
        return node;
    }

    int getSize()
    {
        return size;
    }

    Node *popBack()
    {
        if (head->next != tail)
        {
            
            auto toBeDeleted = tail->prev;
            toBeDeleted->prev->next = toBeDeleted->next;
            toBeDeleted->next->prev = toBeDeleted->prev;
            size--;
            return toBeDeleted;
        }
        else
        {
            // cout<<"not deleting "<<endl;
            return NULL;
        }
    }

    void remove(Node *node)
    {
        if (node->prev && node->next)
        {

            auto beforeDelete = node->prev;
            auto afterDelete = node->next;
            beforeDelete->next = afterDelete;
            afterDelete->prev = beforeDelete;
            size--;
        }
    }
};

class LFUCache
{
public:
    int maxSize, curSize, minFreq;
    map<int, int> keyFreq, keyVal;
    map<int, List *> freqList;
    map<int, Node *> keyNode;

    LFUCache(int capacity)
    {
        maxSize = capacity;
        minFreq = 0;
        curSize = 0;
    }

    void put(int key, int value)
    {
        if (maxSize == 0)
            return;

        if (keyFreq.count(key))
        {
            keyVal[key] = value;
            updateFreqList(key);
        }
        else
        {
            if (curSize >= maxSize)
            {
                
                List* l = freqList[minFreq];
                // cout<<"l's ("<<minFreq<<") first element is: "<<l->head->next->val<<endl;
                auto removedNode = l->popBack();
                keyVal.erase(removedNode->val);
                keyFreq.erase(removedNode->val);
                keyNode.erase(removedNode->val);
                curSize--;
            }
            minFreq = 1;
            curSize++;
            keyFreq[key] = 1;
            keyVal[key] = value;
            if (!freqList.count(minFreq))
                freqList[minFreq] = new List();
            keyNode[key] = freqList[minFreq]->pushFront(key);
            // auto temp = freqList[minFreq]->head;
            // while(temp){
            //     temp = temp->next;
            // }
            // cout<<endl;
        }
        // cout<<key<<endl;
//         for(auto m:keyFreq){
//             cout<<m.first<<" "<<m.second<<"\t";
//         }
        
        // cout<<endl<<"minFreq: "<<minFreq<<endl;
    }

    void updateFreqList(int key)
    {
        auto freq = keyFreq[key];
        auto newFreq = freq + 1;

        // remove from previous list
        // for(auto m:keyFreq){
        //     cout<<m.first<<" "<<m.second<<"\t";
        // }
        freqList[freq]->remove(keyNode[key]);
        // cout<<"updating freq list, freq:"<<freq<<" minFreq:"<<minFreq<<endl;
        if (freqList[freq]->getSize() == 0 && minFreq == freq)
        {
            minFreq++;
        }
        keyNode.erase(key);
        // keyFreq.erase(key);
        if (!freqList.count(newFreq))
        {
            freqList[newFreq] = new List();
        }
        auto node = freqList[newFreq]->pushFront(key);
        keyFreq[key] = newFreq;
        keyNode[key] = node;
    }

    int get(int key)
    {
        if (!keyVal.count(key))
        {
            return -1;
        }
        else
        {
            auto val = keyVal[key];
            updateFreqList(key);
            return val;
        }
    }
};