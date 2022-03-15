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
    ListNode* reverse(ListNode* start, ListNode* end){
        auto prev = end;
        while(start!=end){
            auto temp =  start->next;
            start->next = prev;
            prev = start;
            start = temp;
        }
        return prev;
    }
//     int getLength(ListNode* head){
//         auto temp = head;
//         int c= 0;
//         while(temp){
//             c++;
//             temp = temp->next;
//         }
        
//         return c;
//     }
    ListNode* reverseKGroup(ListNode* head, int k) {
        if(k==1) return head;
        int t = 0;
        bool first = true;
        ListNode* ans;
        auto temp = head;
        ListNode* prevstart=NULL;
        while(true){
            auto start = temp;
            t=0;
            while(t<k){
                if(!temp){
                    return ans;
                }
                temp = temp->next;
                t++;
            }
            
        
            // cout<<"now running iter "<<t<<endl;
            
            
            auto tempans = reverse(start,temp);
            if(first){
                ans = tempans;
                first = false;
            }
            if(prevstart)
            prevstart->next = tempans;
            prevstart = start;
            // cout<<"start was: "<<start->val<<endl;
            // cout<<"temp was: "<<temp->val<<endl;
            start->next = temp;
            // cout<<"tempans: "<<tempans->val<<"\n";
            
        }
        return ans;
    }
};