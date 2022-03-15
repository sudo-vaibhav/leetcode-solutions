/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        auto slow = head,fast = head;
        do{
            if(!fast||!fast->next) return NULL;
            slow = slow->next;
            fast = fast->next->next;
        }while(fast!=slow);
        
        fast = head;
        
        while(fast!=slow){
            fast = fast->next;
            slow = slow->next;
        }
        
        return slow;
        
    }
};