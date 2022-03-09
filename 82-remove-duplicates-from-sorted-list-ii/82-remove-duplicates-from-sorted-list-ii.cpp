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
    ListNode* deleteDuplicates(ListNode* head) {
        auto temp = head;
        auto prev = new ListNode(INT_MAX);
        prev->next = temp;
        while(temp){
            if(temp->next&&temp->next->val==temp->val){
                auto dupVal = temp->val;
                while(prev->next && prev->next->val==dupVal){
                    prev->next = prev->next->next;
                }
                temp = prev->next;
                if(prev->val==INT_MAX) head= temp;
            }
            else{
                prev=prev->next;
                temp = temp->next;
            }
            
        }
        return head;
    }
};