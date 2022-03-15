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
    ListNode* reverse(ListNode* start,const ListNode* end){
        ListNode *prev = NULL,*temp;
        while(start!=end){
            temp =  start->next;
            start->next = prev;
            prev = start;
            start = temp;
        }
        return prev;
    }
    ListNode* reverseKGroup(ListNode* head,const int k) {
        if(k==1) return head;
        int t;
        ListNode *temp = head,*ans=NULL,*prevstart=NULL,*tempans,*start;
        while(true){
            start = temp;
            t=0;
            while(t++<k){
                if(!temp){
                    return ans;
                }
                temp = temp->next;
            }
            tempans = reverse(start,temp);
            if(!ans){
                ans = tempans;
            }
            if(prevstart){
                prevstart->next = tempans;
            }
            prevstart = start;
            start->next = temp;            
        }
        return ans;
    }
};