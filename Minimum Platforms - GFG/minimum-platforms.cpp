// { Driver Code Starts
// Program to find minimum number of platforms
// required on a railway station
#include <bits/stdc++.h>
using namespace std;


 // } Driver Code Ends
class Solution{
  
    public:
    //Function to find the minimum number of platforms required at the
    //railway station such that no train waits.
    int findPlatform(int arr[], int dep[], int n)
    {
    	// Your code here
    	if(n<=0) return n;
    	
    	// 0 to 2359
        vector<int> platformReq(2360,0);
        
        for(int i=0;i<n;i++){
            platformReq[arr[i]]++;
            platformReq[dep[i]+1]--;
        }
    
        int maxReq = 1;
        // now we will see cumulated platform requirements
        for(int i=1;i<2360;i++){
            platformReq[i] += platformReq[i-1];
            maxReq = max(platformReq[i],maxReq);
        }
        return maxReq;
    }
    
};


// { Driver Code Starts.
// Driver code
int main()
{
    int t;
    cin>>t;
    while(t--) 
    {
        int n;
        cin>>n;
        int arr[n];
        int dep[n];
        for(int i=0;i<n;i++)
            cin>>arr[i];
        for(int j=0;j<n;j++){
            cin>>dep[j];
        }
        Solution ob;
        cout <<ob.findPlatform(arr, dep, n)<<endl;
    } 
   return 0;
}  // } Driver Code Ends