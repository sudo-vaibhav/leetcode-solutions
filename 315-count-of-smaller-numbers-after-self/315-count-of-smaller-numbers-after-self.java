class STNode{
    int count;
    STNode(){
        this.count=0;
    }
    STNode(int count){
        this.count = count;
    }
};



// class Solution {
// public:
//     vector<int> countSmaller(vector<int>& nums) {
//         int n = nums.size();
//         vector<int> NUMS = nums;
//         sort(NUMS.begin(),NUMS.end());
//         int maxi = 1;
//         int i = 1;
//         map<int,int>cc;
//         for(auto num:NUMS){
//             if(!cc.count(num)){
//                 cc[num]=i;
//                 i+=1;
//             }
//         }
        
//         for(int j=0;j<n;j++){
//             nums[i]=cc[nums[i]];
//             maxi = max(maxi,nums[i]);
//         } 

//         int N = nums.size();
        
//         st = vector<STNode>(4*N,STNode());
        
        
//         auto ans = vector<int>(n);
        
//         for(int i=n-1;i>=0;i--){
//             auto cur = nums[i];
//             ans[n-1-i] = query(1,1,N,cur).count;            
//             update(1,1,N,cur);
//         }
//         return ans;
//     }
// };
class Solution {
    
    List<STNode> st;

    STNode merge(STNode node1,STNode node2){
        return new STNode(node1.count+node2.count);
    }


    // # returns the number of elements in scope of node less than val
    STNode query(int index,int l,int r,int val){
        if(val<l || l>r) return new STNode();
        else if (val>r)
            return st.get(index);
        else if (l==r)
            return new STNode();
        else{
            int mid = (l+r)/2;
            return merge(
                query(2*index,l,mid,val),
                query((2*index)+1,mid+1,r,val)
            );
        }
    }

    // # updates the node to have new value added equal to val
    void update(int index,int l,int r,int val){
        if (l>r || val<l || val>r) return;
        else if (l==r)
            st.get(index).count++;
        else{
            int mid = (l+r)/2;
            update(2*index,l,mid,val);
            update((2*index)+1,mid+1,r,val);
            st.set(index, merge(st.get(index*2),st.get((index*2)+1)));
        }
    }
    
    public List<Integer> countSmaller(int[] nums) {
        int n = nums.length;
        var NUMS = new ArrayList<Integer>();
        for(var num:nums){
            NUMS.add(num);
        }
        Collections.sort(NUMS);
        // sort(NUMS.begin(),NUMS.end());
        int maxi = 1;
        int i = 1;
        var cc = new TreeMap<Integer,Integer>();
        
        for(var num:NUMS){
            if(!cc.containsKey(num)){
                cc.put(num,i);
                i+=1;
            }
        }
        
        for(int j=0;j<n;j++){
            nums[j]=cc.get(nums[j]);
            maxi = Math.max(maxi,nums[j]);
        } 

        int N = nums.length;
        
        st = new ArrayList<STNode>();
        // 4*N,STNode());
        for(i=0;i<4*N;i++){
            st.add(new STNode(0));
        }
        
        var ans = new ArrayList<Integer>();
        
        for(i=n-1;i>=0;i--){
            var cur = nums[i];
            ans.add(query(1,1,N,cur).count);            
            update(1,1,N,cur);
        }
        Collections.reverse(ans);
        return ans;
    }
}