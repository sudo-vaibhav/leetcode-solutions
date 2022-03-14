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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        auto dummy = new ListNode();
        auto temp = head;
        dummy->next = head;
        // int k=1;
        while(n--){
            temp = temp->next;
            // k++;
        }
        while(temp){
            temp = temp->next;
            dummy = dummy->next;
        }
        
        cout<<dummy->val;
        if(dummy->next==head){
            return head->next;
        }else{
            dummy->next = dummy->next->next;
            return head;
        }

    }
};