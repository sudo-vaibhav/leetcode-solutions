class Solution {
public:
    int subsetXORSum(vector<int>& nums) {
        int ans = 0;
        for(int i=0;i<pow(2,nums.size());i++){
            auto c = i;
            int j=0;
            int temp = 0;
            while(c>0){
                int toTake = c&1;
                c>>=1;
                temp^=nums[j]*toTake;
                j++;
            }
            ans+=temp;
        }
        return ans;
    }
};