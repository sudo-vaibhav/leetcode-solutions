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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* dummy= new ListNode();
        auto temp = new ListNode();
        temp=dummy;
        int carry = 0;
        while(l1||l2){
            auto tot = carry;
            if(l1){
                tot+=l1->val;
                l1 = l1->next;
            }
            
            if(l2){
                tot+=l2->val;
                l2 = l2->next;
            }
            
            if(tot>=10){
                carry = 1;
            }
            else{
                carry = 0;
            }
            temp->next = new ListNode(tot%10);
            temp = temp->next;
        }
        
        if(carry){
            temp->next = new ListNode(1);
        }
        return dummy->next;
    }
};