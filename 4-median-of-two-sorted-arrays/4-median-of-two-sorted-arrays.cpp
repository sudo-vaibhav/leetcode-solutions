// run time complexity O((m+n)log(m+n)) , space complexity O(len(nums2))
// class Solution {
// public:
//     double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
//         nums1.insert(nums1.end(),nums2.begin(),nums2.end());
//         sort(nums1.begin(),nums1.end());
//         int N = nums1.size();
//         if(N%2==1){
//             return nums1[N/2];
//         }else{
//             return (nums1[N/2]+nums1[N/2-1])/2.0;
//         }
//     }
// };

// O(log(m+n)) solution
class Solution{
    public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {

        // [1,2]
        // [3,4]
        int m = nums1.size();
        int n = nums2.size();
        
        if(m>n) return findMedianSortedArrays(nums2,nums1);
            
        int N = m+n;
        
        int inEachHalf = (N+1)/2;
        // now we will do further calculations on basis of nums1
        int L = 0;
        int R = m;
        while(L<=R){
            int toTakeFromNums1 = L+(R-L)/2;
            int toTakeFromNums2 = inEachHalf - toTakeFromNums1;
            
            int l1 = toTakeFromNums1>0?nums1[toTakeFromNums1-1]:INT_MIN;
            int l2 = toTakeFromNums2>0?nums2[toTakeFromNums2-1]:INT_MIN;
            int leftMax = max(l1,l2);
            
            int r1 = toTakeFromNums1==m ? INT_MAX: nums1[toTakeFromNums1];
            int r2 = toTakeFromNums2==n ? INT_MAX: nums2[toTakeFromNums2];
            int rightMin = min(r1,r2);
            
            cout<<"fromn1: "<<toTakeFromNums1<<" fromn2: "<<toTakeFromNums2<<" leftMax:"<<leftMax<<" rightMin:"<<rightMin<<endl;
            if(leftMax<=rightMin){
                if(N%2==1){
                    return leftMax;
                }else{
                    return (leftMax+rightMin)/2.0;
                }
            }
            else{
                if(leftMax == l1){
                    R= toTakeFromNums1-1;
                }
                else{
                    L = toTakeFromNums1+1;
                }
            }
        }
        
        return 0;
    }
};