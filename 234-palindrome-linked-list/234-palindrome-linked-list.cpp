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
    void pl(ListNode* head){

        while(head){
            cout<<head->val<<"\t";
            head = head->next;
        }
        
        cout<<endl;
        
    }
    bool isPalindrome(ListNode* head) {
        if(!head->next) return true;
        if(!head->next->next) return head->val == head->next->val;
        
        auto slow = head, fast = head;
        ListNode* prev = NULL;
        while(fast&&fast->next){
            fast = fast->next->next;
            auto temp = slow->next;
            slow->next = prev;
            prev = slow;
            slow = temp;
        }
        if(fast){
            fast = slow->next;
        }
        else{
            fast = slow;
        }
        // if(!fast){
        slow  = prev;
        // }
        
        pl(slow);
        pl(fast);
        
        while(fast&&slow){
            if(fast->val!=slow->val){
                return false;
            }
            fast = fast->next;
            slow = slow->next;
        }
        return true;
    }
};