// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
class Solution{

	public:
	int maxSumIS(int nums[], int n)  
	{  
       vector<int> dp(n); // represents max sum of increasing subsequences ending with i
       for(auto i=0;i<n;i++){
           dp[i] = nums[i]; // at least include yourself
       }
       
       for(auto i=1;i<n;i++){
           for(auto j=0;j<i;j++){
               if(nums[j]<nums[i]){
                   dp[i] = max(dp[i],nums[i]+dp[j]);
               }
           }
       }
       
       return *max_element(dp.begin(),dp.end());
	}  
};

// { Driver Code Starts.
int main() 
{
   	
   
   	int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;

        int a[n];

        for(int i = 0; i < n; i++)
        	cin >> a[i];

      

	    Solution ob;
	    cout << ob.maxSumIS(a, n) << "\n";
	     
    }
    return 0;
}

  // } Driver Code Ends