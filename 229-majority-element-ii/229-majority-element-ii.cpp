class Solution {
public:
    void verify(int n,vector<int>&nums,vector<int>& ans){
        int c=0;
        for(auto num:nums){
            if(num==n)c++;
        }
        
        if(c>nums.size()/3&&find(ans.begin(),ans.end(),n)==ans.end())ans.push_back(n);
    }
    
    vector<int> majorityElement(vector<int>& nums) {
        int num1=-1,num2=-1,c1=0,c2=0;
        vector<int> ans;
        for(auto num:nums){
            if(num1==num)c1++;
            else if(num2==num)c2++;
            else if(c1==0) {num1=num;c1=1;}
            else if(c2==0) {num2=num;c2=1;}
            else{c1--;c2--;}
        }
        
        verify(num1,nums,ans);
        verify(num2,nums,ans);
        return ans;
    }
};