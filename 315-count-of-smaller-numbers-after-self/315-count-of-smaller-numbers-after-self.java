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

class Pair{
    public int num;
    public int idx;
    public Pair(int num, int idx){
        this.num = num;
        this.idx = idx;
    }
}
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
        var cc = new ArrayList<Pair>();
        for(int i=0;i<n;i++){
            cc.add(new Pair(nums[i],i));
        }
        
        var comp = new Comparator<Pair>(){
            public int compare(Pair p1,Pair p2){
                if (p1.num<p2.num){
                    return -1;
                }
                else if(p1.num>p2.num){
                    return 1;
                }
                return 0;
            }
        };
        Collections.sort(cc,comp);
        // sort(NUMS.begin(),NUMS.end());
        for(int i=0;i<n;i++){
            nums[cc.get(i).idx] = i+1;
        }
        
        
        st = new ArrayList<STNode>();
        // 4*N,STNode());
        for(int i=0;i<4*n;i++){
            st.add(new STNode(0));
        }
        
        var ans = new ArrayList<Integer>();
        
        for(int i=n-1;i>=0;i--){
            var cur = nums[i];
            ans.add(query(1,1,n,cur).count);            
            update(1,1,n,cur);
        }
        Collections.reverse(ans);
        return ans;
    }
}