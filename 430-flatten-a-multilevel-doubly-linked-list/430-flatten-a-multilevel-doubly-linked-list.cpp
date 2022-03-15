/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* prev;
    Node* next;
    Node* child;
};
*/

class Solution {
public:
    void appendToEnd(Node* flattenedChildList,Node* flattenedNextList){
        auto temp = flattenedChildList;
        while(temp->next){
            temp = temp->next;
        }
        temp->next = flattenedNextList;
        if(flattenedNextList)
        flattenedNextList->prev = temp;
    }
    Node* flatten(Node* head) {
        if(!head) return head;
        auto flattenedChildList = flatten(head->child);
        auto flattenedNextList = flatten(head->next);
        
        
        head->child = NULL;
        if(flattenedChildList){
            flattenedChildList->prev = head;
            head->next = flattenedChildList;
            
            appendToEnd(flattenedChildList,flattenedNextList);
        }
        
        return head;
    }
};