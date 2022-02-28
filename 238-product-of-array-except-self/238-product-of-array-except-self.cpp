class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int zCount = 0;
        int prod = accumulate(nums.begin(),nums.end(),1, [&zCount](int a, int b) mutable{
            int ans = a;
            if(b!=0){
                ans *=b; 
            }
            else{
                // cout<<"this runs"<<endl;
                zCount++;
            }
            // cout<<a<<" "<<b<<endl;
            return ans;
        });
        // cout<<"zCount"<<zCount<<endl;
        vector<int> ans;
        for(int i=0;i<nums.size();i++){
            if(zCount>1){
                ans.push_back(0);
            }
            else if(zCount==1){
                ans.push_back(nums[i]==0? prod: 0);
            }
            else{
                if(nums[i]!=0)
                ans.push_back(prod*pow(nums[i],-1));
            }
        }
        
        return ans;
        
    }
};