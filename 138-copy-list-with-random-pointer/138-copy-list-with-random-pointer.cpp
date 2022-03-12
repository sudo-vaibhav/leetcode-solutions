/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

// O(n) time O(n) space
// class Solution {
// public:
//     Node* copyRandomList(Node* head) {
//         auto dummy = new Node(0);
//         auto it = dummy;
//         auto temp = head;
//         map<Node*,Node*> cache;
        
        
//         while(temp){
//             if(cache.count(temp)){
//                 it->next = cache[temp];
//             }
//             else{
//                 it->next = new Node(temp->val);
//                 cache[temp] = it->next;
//             }
            
//             if(temp->random==NULL) {
//                 it->next->random = NULL;
//             }
//             else if(cache.count(temp->random)){
//                 it->next->random = cache[temp->random];
//             }
//             else{
//                 cache[temp->random] = new Node(temp->random->val);
//                 cache[temp->random]->next = temp->random->next;
//                 it->next->random = cache[temp->random];
//             }
            
//             it = it->next;
//             temp = temp->next;
            
//         }
        
//         return dummy->next;
//     }
// };

class Solution{
    public:
    void printList(Node* head){
        auto temp = head;
        while(temp){
            cout<<temp->val;
            if(temp->random){
                cout<<" ("<<temp->random->val<<")";
            }
            cout<<"\t";
            temp = temp->next;
        }
        cout<<endl;
    }
    
    Node* copyRandomList(Node* head) {
        if(!head) return NULL;
        
        // step1 - create new elements and place them adjacently
        auto temp = head;
        while(temp){
            auto nextNode = temp->next;
            auto copyNode = new Node(temp->val);
            copyNode->next = nextNode;
            temp->next = copyNode;
            temp = copyNode->next;
        }
        
        printList(head);
        
        // step2 - now establish random pointers
        auto oldIter = head;
        auto newIter = head->next;
        while(true){
            if(oldIter->random==NULL) newIter->random = NULL;
            else{
                newIter->random = oldIter->random->next;    
            }
            
            oldIter = oldIter->next->next;
            if(newIter->next){
                newIter = newIter->next->next;
            }
            else{
                break;
            }
            
        }
        
        printList(head);
        
        // step3 - establish next pointers and restore both old and new lists to final form
        oldIter = head;
        newIter = head->next;
        auto ans = newIter;
        while(newIter){
            auto nextOldNode = newIter->next;
            Node* nextNewNode;
            if(!nextOldNode){
                newIter->next = NULL;
                oldIter->next = NULL;
                break;
            }
            else{
                nextNewNode = nextOldNode->next;
            }
            
            
            oldIter->next = nextOldNode;
            newIter->next = nextNewNode;
            
            newIter = newIter->next;
            oldIter = oldIter->next;
        }
        
        cout<<"final:\n";
        printList(head);
        printList(ans);
        return ans;
    }
};