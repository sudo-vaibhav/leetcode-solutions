/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* oddEvenList(ListNode* head) {
        if(!head||!head->next) return head;
        auto d1 = new ListNode();
        auto d2 = new ListNode();
        
        d1->next = head;
        d2->next = head->next;
        
        auto ptr = head;
        auto ptr2 = head->next;
        
        while(ptr&&ptr2){
            ptr->next = ptr2->next;
            if(ptr->next){
                ptr2->next = ptr->next->next;
                ptr = ptr->next;
            }
            ptr2 = ptr2->next;
        }
        
        ptr -> next = d2->next;
        
        return d1->next;
        
    }
};