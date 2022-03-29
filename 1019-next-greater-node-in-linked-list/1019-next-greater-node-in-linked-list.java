/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public int[] nextLargerNodes(ListNode head) {
        var s = new Stack<Integer>();
        var temp = head;
        var vals = new ArrayList<Integer>();
        var h = new HashMap<Integer,Integer>();
        int t= 0;
        while(temp!=null){
            vals.add(temp.val);
            while(!s.empty() && vals.get(s.peek())<temp.val){
                h.put(s.pop(),temp.val);
            }
            s.push(t);
            h.put(t,0);
            t++;
            temp=temp.next;
        }
        
        var ans = new int[vals.size()];
        for(int i=0;i<vals.size();i++){
            ans[i]=((int)h.get(i));
        }
        
        return ans;
    }
}