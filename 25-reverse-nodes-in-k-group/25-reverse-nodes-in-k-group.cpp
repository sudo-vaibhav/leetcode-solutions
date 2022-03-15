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
        // cout<<"inside reverse"<<endl;
        auto h = start;
        // while(h!=end){
        //     cout<<h->val<<"\t";
        //     h= h->next;
        // }
        // cout<<endl;
        auto prev = end;
        while(start!=end){
            auto temp =  start->next;
            start->next = prev;
            prev = start;
            start = temp;
        }
        
        // cout<<"now see reverse"<<endl;
        auto g = prev;
        // while(g){
        //     cout<<g->val<<"\t";
        //     g = g->next;
        // }
        // cout<<endl;
        // cout<<"going outside of reverse"<<endl;
        return prev;
    }
    int getLength(ListNode* head){
        auto temp = head;
        int c= 0;
        while(temp){
            c++;
            temp = temp->next;
        }
        
        return c;
    }
    ListNode* reverseKGroup(ListNode* head, int k) {
        if(k==1) return head;
        auto n = getLength(head);
        // cout<<"length : "<<n<<endl;
        int t = 0,c=0;
        bool first = true;
        ListNode* ans;
        auto temp = head;
        ListNode* prevstart=NULL;
        while(c+k<=n){
            // cout<<"main val: "<<temp->val<<endl;
            auto x = temp;
            
//             while(x){
//                 cout<<x->val<<"\t";
//                 x = x->next;
//             }
//             cout<<endl;
            auto start = temp;
            t=0;
            while(t<k){
                // cout<<temp->val<<endl;
                temp = temp->next;
                c++;t++;
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