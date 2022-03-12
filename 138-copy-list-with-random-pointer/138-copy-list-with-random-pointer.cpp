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

class Solution {
public:
    Node* copyRandomList(Node* head) {
        auto dummy = new Node(0);
        auto it = dummy;
        auto temp = head;
        map<Node*,Node*> cache;
        
        
        while(temp){
            if(cache.count(temp)){
                it->next = cache[temp];
            }
            else{
                it->next = new Node(temp->val);
                cache[temp] = it->next;
            }
            
            if(temp->random==NULL) {
                it->next->random = NULL;
            }
            else if(cache.count(temp->random)){
                it->next->random = cache[temp->random];
            }
            else{
                cache[temp->random] = new Node(temp->random->val);
                cache[temp->random]->next = temp->random->next;
                it->next->random = cache[temp->random];
            }
            
            it = it->next;
            temp = temp->next;
            
        }
        
        return dummy->next;
    }
};