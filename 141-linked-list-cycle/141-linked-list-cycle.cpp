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
    bool hasCycle(ListNode *head) {
        auto slow = head,fast = head;
        if (!fast||!fast->next) return false;
        while(fast&&fast->next){
            fast = fast->next->next;
            if(fast==slow) return true;
            slow = slow->next;
        }
        
        return fast==slow;
    }
};