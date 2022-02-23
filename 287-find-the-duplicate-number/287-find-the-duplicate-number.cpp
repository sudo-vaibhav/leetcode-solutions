
// int Partition(vector<int> &v, int start, int end){
	
// 	int pivot = end;
// 	int j = start;
// 	for(int i=start;i<end;++i){
// 		if(v[i]<v[pivot]){
// 			swap(v[i],v[j]);
// 			++j;
// 		}
// 	}
// 	swap(v[j],v[pivot]);
// 	return j;
	
// }

// void Quicksort(vector<int> &v, int start, int end ){

// 	if(start<end){
// 		int p = Partition(v,start,end);
// 		Quicksort(v,start,p-1);
// 		Quicksort(v,p+1,end);
// 	}
	
// }

// class Solution {
// public:
//     int findDuplicate(vector<int>& nums) {
//         auto n = nums.size();
//         Quicksort(nums,0,n-1);
//         cout<<endl;
//         for(auto i=0;i<n-1;i++){
//            if(nums[i]==nums[i+1])
//            {
//                return nums[i];
//            }        
//         }
//         return 0;
//     }
// };

class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        for(int i=0;i<nums.size();i++){
            auto val = abs(nums[i]);
            if(nums[val-1]<0) return val;
            nums[val-1] = -nums[val-1];
        }       
        return 0;
    }
};