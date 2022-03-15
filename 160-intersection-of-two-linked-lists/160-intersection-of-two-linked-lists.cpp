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
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        auto tempA = headA,tempB=headB;
        while(tempA&&tempB){
            tempA = tempA->next;
            tempB = tempB->next;
        }
        ListNode* temp;
        if(!tempA){
            tempA = headB;
            while(tempB){
                tempB = tempB->next;
                tempA = tempA->next;
            }
            tempB = headA;
        }
        else{
            tempB = headA;
            while(tempA){
                tempB = tempB->next;
                tempA = tempA->next;
            }
            tempA = headB;
        }
        
        while(tempB&&tempA){
            if(tempB==tempA) return tempA;
            tempB = tempB->next;
            tempA = tempA->next;
        }
        
        return tempA;
        
    }
};