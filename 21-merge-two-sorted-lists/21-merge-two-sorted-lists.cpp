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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        auto h1 = list1,h2= list2;
        auto res = new ListNode();
        auto ans = res;
        while(h1&&h2){
            auto v1 = h1->val;
            auto v2 = h2->val;
            
            if(v1<v2){
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