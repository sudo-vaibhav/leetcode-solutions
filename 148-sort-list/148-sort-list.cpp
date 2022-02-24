// O(nlogn) time and O(logn) space due to recursive stack - top down approach
// class Solution {
// public:
//     ListNode* sortList(ListNode* head) {
//         if(!head||!head->next){
//             return head;
//         }
//         auto mid = getMid(head);
//         auto left = sortList(head);
//         auto right = sortList(mid);
//         return merge(left,right);
//     }
    
//     ListNode* getMid(ListNode* head){
//         ListNode* midPrev = nullptr;
//         while(head&&head->next){
//             midPrev = (midPrev==nullptr) ? head: midPrev->next;
//             head = head->next->next;
//         }
        
//         ListNode* mid = midPrev->next;
//         midPrev->next= nullptr;
//         return mid;
//     }
    
//     ListNode* merge(ListNode* list1, ListNode* list2){
//         ListNode* dummyHead = new ListNode(0);
//         ListNode* ptr = dummyHead;
//         while(list1&&list2){
//             if(list1->val<list2->val){
//                 ptr->next = list1;
//                 list1 = list1->next;
//             }
//             else{
//                 ptr->next = list2;
//                 list2 = list2->next;
//             }
//             ptr = ptr->next;
//         }
//         if(list1) ptr->next = list1;
//         else ptr->next = list2;
        
//         return dummyHead->next;
//     }
// };


// O(nlogn) time complexity, O(1) space complexity
class Solution{
    ListNode* tail = new ListNode();
    ListNode* nextSubList = new ListNode();
    
    public:
    ListNode* sortList(ListNode* head) {
        if(head&&head->next){
            int n = getCount(head);
            ListNode* start = head;
            ListNode* dummyHead = new ListNode(0);
            for(int size=1;size<n;size*=2){
                tail = dummyHead;
                while(start){
                    if(!start->next){
                        tail->next = start;
                        break;
                    }
                    else{
                        ListNode* mid = split(start,size);
                        merge(start,mid);
                        start = nextSubList;
                    }
                }
                start = dummyHead->next;
            }
            return dummyHead->next;
        }
        else{
            return head;
        }
    }
    
    ListNode* split(ListNode* start, int size){
        ListNode* midPrev = start;
        ListNode* end = start->next;
        for(int index = 1;index<size && (midPrev->next||end->next);index++){
            if(end->next){
                end = (end->next->next)?end->next->next : end->next;
            }
            if(midPrev->next){
                midPrev = midPrev->next;
            }
        }
        ListNode* mid = midPrev->next;
        nextSubList = end->next;
        midPrev->next = nullptr;
        end->next = nullptr;
        return mid;
    }
    
    void merge(ListNode* list1,ListNode* list2){
        ListNode dummyHead(0);
        ListNode* newTail = &dummyHead;
        while (list1 && list2) {
            if (list1->val < list2->val) {
                newTail->next = list1;
                list1 = list1->next;
                newTail = newTail->next;
            } else {
                newTail->next = list2;
                list2 = list2->next;
                newTail = newTail->next;
            }
        }
        newTail->next = (list1) ? list1 : list2;
        // traverse till the end of merged list to get the newTail
        while (newTail->next) {
            newTail = newTail->next;
        }
        // link the old tail with the head of merged list
        tail->next = dummyHead.next;
        // update the old tail with the new tail of merged list
        tail = newTail;
    }
    
     int getCount(ListNode* head) {
        int cnt = 0;
        ListNode* ptr = head;
        while (ptr) {
            ptr = ptr->next;
            cnt++;
        }
        return cnt;
    }
    
};