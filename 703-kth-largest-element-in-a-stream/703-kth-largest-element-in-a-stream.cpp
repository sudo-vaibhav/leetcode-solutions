class KthLargest {
public:
    priority_queue<int,vector<int>,greater<int>> large;
    int K;
    KthLargest(int k, vector<int>& nums) {
        K = k;
        sort(nums.begin(),nums.end());
        int c = 0,n = nums.size();
        int i=n-1;
        while(i>=0&&k>c){
            large.push(nums[i--]);
            c++;
        }
    }
    
    int add(int val) {
        large.push(val);
        if(large.size()>K){
            large.pop();
        }
        return large.top();
    }
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */