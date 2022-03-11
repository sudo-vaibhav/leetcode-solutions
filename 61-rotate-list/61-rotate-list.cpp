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
    pair<int,ListNode*> getLength(ListNode* head){
        int c=0;
        ListNode* prev=NULL;
        while(head){
            c++;
            prev = head;
            head = head->next;
        }
        return {c,prev};
    }
    ListNode* rotateRight(ListNode* head, int k) {
        auto ans = getLength(head);
        auto prev = ans.second;
        cout<<ans.first<<endl;
        if(ans.first<=1||k%ans.first==0) return head;
        k = k%ans.first;
        int r = ans.first-k-1;
        auto rthNode = head;
        while(r--){
            rthNode = rthNode->next;
        }
        auto res = rthNode->next;
        rthNode->next = NULL;
        prev->next = head;
        return res;
    }
};