// { Driver Code Starts
// Program to find the maximum profit job sequence from a given array 
// of jobs with deadlines and profits 
#include<bits/stdc++.h>
using namespace std; 

// A structure to represent a job 
struct Job 
{ 
    int id;	 // Job Id 
    int dead; // Deadline of job 
    int profit; // Profit if job is over before or on deadline 
}; 


 // } Driver Code Ends
/*
struct Job 
{ 
    int id;	 // Job Id 
    int dead; // Deadline of job 
    int profit; // Profit if job is over before or on deadline 
};
*/

class Solution 
{
    struct comp{
        public:
        bool operator()(Job j1, Job j2){
            return j1.profit < j2.profit; // whichever has a higher profit should be on top
        }
    };
    public:
    //Function to find the maximum profit and the number of jobs done.
    vector<int> JobScheduling(Job arr[], int n) 
    { 
        // your code here
        // DRY RUN
        
        priority_queue <Job,vector<Job>,comp> pq,copy_pq;
        
        int maxDead=-1;
        for(int i=0;i<n;i++){
            pq.push(arr[i]); // {(3,1,40), (4,1,30) , (1,4,20), (2,1,10)}
        
            maxDead = max(maxDead,arr[i].dead);
        }
        
        vector<int> slots(maxDead,-1);
        // copy_pq = pq;
        // while(!copy_pq.empty()){
        //     cout<< "profit: "<<copy_pq.top().profit<<" deadline:"<<copy_pq.top().dead<<endl;
        //     copy_pq.pop();
        // }
        int doneJobs=0,profit =0;
        while(!pq.empty()){
            auto currentJob = pq.top(); // {3,1,40} -> {4,1,30} -> {1,4,20} -> {2,1,10}
            pq.pop();
            for(int i=currentJob.dead-1;i>=0;--i){
                if(slots[i]==-1){
                    slots[i] = currentJob.id;
                    profit+= currentJob.profit;
                    doneJobs++;
                    break;
                }
            }
        }
        
        
        return {doneJobs,profit};
    } 
    
};

// { Driver Code Starts.
// Driver program to test methods 
int main() 
{ 
    int t;
    //testcases
    cin >> t;
    
    while(t--){
        int n;
        
        //size of array
        cin >> n;
        Job arr[n];
        
        //adding id, deadline, profit
        for(int i = 0;i<n;i++){
                int x, y, z;
                cin >> x >> y >> z;
                arr[i].id = x;
                arr[i].dead = y;
                arr[i].profit = z;
        }
        Solution ob;
        //function call
        vector<int> ans = ob.JobScheduling(arr, n);
        cout<<ans[0]<<" "<<ans[1]<<endl;
    }
	return 0; 
}


  // } Driver Code Ends