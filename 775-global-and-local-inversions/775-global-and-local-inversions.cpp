class Solution {
public:
    long long countLocalInversions(vector<int>& nums){
        long long ans = 0;
        for(int i=0;i<nums.size()-1;i++){
            if(nums[i]>nums[i+1]) ans++;
        }
        return ans;
    }
    void merge(vector<int>&nums,
               vector<int>&temp,
               int l, int mid, int r, long long& invCount){
       int i = l,j = mid+1,t=l;
        
        while(i<=mid&&j<=r){
            if(nums[i]<=nums[j]){
                temp[t++]=nums[i++];
            }
            else{
                invCount+=(mid-i+1);
                temp[t++]=nums[j++];
            }
        } 
        
        while(i<=mid){
            temp[t++] = nums[i++];
        }
        while(j<=r){
            temp[t++] = nums[j++];
        }
        
        for(i=l;i<=r;i++){
            nums[i]=temp[i];
        }
        
    }
    void mergeSort(vector<int>& nums,
                   vector<int>& temp,
                   int l, int r, long long& invCount){
        if(l>=r) return;
        int mid = l+(r-l)/2;
        mergeSort(nums,temp,l,mid,invCount);
        mergeSort(nums,temp,mid+1,r,invCount);
        merge(nums,temp,l,mid,r,invCount);
    }
    long long countInversions(vector<int>& nums,vector<int>& temp){
        long long invCount=0;
        mergeSort(nums,temp,0,nums.size()-1,invCount);
        return invCount;
    }
    
    bool isIdealPermutation(vector<int>& nums) {
        auto NUMS = nums;
        long long localInversions = countLocalInversions(nums),globalInversions = countInversions(nums,NUMS);
        
        // cout<<globalInversions<<" "<<localInversions<<endl;
        return globalInversions == localInversions;
    }
};