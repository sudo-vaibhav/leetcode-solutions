// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
class Solution
{
    struct Meeting{
        int start;
        int end;
        public:
        Meeting(int startTime, int endTime){
            start = startTime;
            end = endTime;
        }
    };
    public:
    //Function to find the maximum number of meetings that can
    //be performed in a meeting room.
    int maxMeetings(int start[], int end[], int n)
    {
        if(n<=1) {
            return n;
            
        }else{
            
            int meetingsCount = 1;
            vector<Meeting> meetings;
            for(int i=0;i<n;i++){
                meetings.push_back(Meeting(start[i],end[i]));
            }        
            
            sort(meetings.begin(),meetings.end(),[](Meeting m1, Meeting m2){
                return m1.end < m2.end;
            });
            
            
            // for(auto i:meetings){
            //     cout<<i.start<<" "<<i.end<<endl;
            // }
            
            auto prev = meetings[0];
            for(int i=1;i<n;i++){
                auto cur = meetings[i];
                if(cur.start>prev.end){
                    meetingsCount++;
                    prev = cur;
                }
                else{
                    
                }
            }
            return meetingsCount;
        
        }
        
    }
};

// { Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        int start[n], end[n];
        for (int i = 0; i < n; i++) cin >> start[i];

        for (int i = 0; i < n; i++) cin >> end[i];

        Solution ob;
        int ans = ob.maxMeetings(start, end, n);
        cout << ans << endl;
    }
    return 0;
}  // } Driver Code Ends