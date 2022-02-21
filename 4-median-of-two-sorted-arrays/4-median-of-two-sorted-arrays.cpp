class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        nums1.insert(nums1.end(),nums2.begin(),nums2.end());
        
        sort(nums1.begin(),nums1.end());
        
        int N = nums1.size();
        if(N%2==1){
            return nums1[N/2];
        }else{
            return (nums1[N/2]+nums1[N/2-1])/2.0;
        }
    }
};