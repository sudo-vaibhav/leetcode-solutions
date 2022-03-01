class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int zCount = 0;
        int n = nums.size();
        for(int i=0;i<n;i++){
            if(nums[i]==0) {
                zCount++;
            }
            else{
                nums[i-zCount] = nums[i];
            }
        }
        
        for(int i=n-1;i>=0&&zCount;i--,zCount--){
            nums[i] = 0;
        }
    }
};