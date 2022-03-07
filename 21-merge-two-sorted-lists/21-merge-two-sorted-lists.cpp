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
    ListNode* mergeTwoLists(ListNode* h1, ListNode* h2) {
        ListNode* res = new ListNode();
        ListNode* ans = res;
        while(h1&&h2){
            if(h1->val<h2->val){
                ans->next = h1;
                h1 = h1->next;
            }
            else{
                ans->next = h2;
                h2 = h2->next;
            }
            ans = ans->next;
        }
        
        while(h1){
            ans->next = h1;
            h1 = h1->next;
            ans = ans->next;
        }
        while(h2){
            ans->next = h2;
            h2 = h2->next;
            ans = ans->next;
        }
        return res->next;
        
    }
};