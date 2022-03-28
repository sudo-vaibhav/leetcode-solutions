class Solution {
public:
    bool search(vector<int>& nums, int target) {
        short l = 0,r=nums.size()-1,mid,val;
        while(l<=r){
            mid = l+(r-l)/2;
            val = nums[mid];
            if(val==target) return true;
            
            if(nums[l]<val){
                if(nums[l]<=target && target<=val){
                    r= mid-1;
                }
                else{
                    l=mid+1;
                }
            }
            else if(nums[l]>val){
                if(val<=target && target<=nums[r]){
                    l=mid+1;
                }
                else{
                    r=mid-1;
                }
            }
            else{
                l+=1;
            }
        }
        
        return false;
    }
};