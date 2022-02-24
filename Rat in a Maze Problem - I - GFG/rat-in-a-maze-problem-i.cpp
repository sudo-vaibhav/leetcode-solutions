// { Driver Code Starts
// Initial template for C++

#include <bits/stdc++.h>
using namespace std;


 // } Driver Code Ends
// User function template for C++

class Solution{
    char getMove(int row, int col, int i, int j){
        if(row<i){
            return 'D';
        }
        if(row>i){
            return 'U';
        }
        if(col<j){
            return 'R';
        }
        return 'L';
    }
    public:
    
    void solve(int row, int col,vector<vector<int>>&m, vector<string>& ans,set<pair<int,int>>& visited,
    string path
    ){
        int n = m.size();
        if(row==n-1&&col==n-1){
            // string temp="";
            // for(char i:path){
            //     temp+=i;
            // }
            
            ans.push_back(path);
            return;
        }    
        
      vector<pair<int,int>> nextMoves = {{row-1,col},{row+1,col},{row,col-1},{row,col+1}};
      
      for(auto move:nextMoves){
          // check if its a legal move
          if(move.first>=0&&move.second>=0&&move.first<n&&move.second<n&&
            m[move.first][move.second]==1&&!visited.count({move.first,move.second})
            ){
              visited.insert({move.first,move.second});
              path+=getMove(row,col,move.first,move.second);
              solve(move.first,move.second,m,ans,visited,path);
              path.pop_back();
              visited.erase({move.first,move.second});
            }
      }
    }
    vector<string> findPath(vector<vector<int>> &m, int n) {
        // Your code goes here
        vector<string> ans;
        if(m[0][0]==0) return ans;
        string path="";
        set<pair<int,int>> visited;
        visited.insert({0,0});
        solve(0,0,m,ans,visited,path);
        return ans;
    }
};

    


// { Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<vector<int>> m(n, vector<int> (n,0));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cin >> m[i][j];
            }
        }
        Solution obj;
        vector<string> result = obj.findPath(m, n);
        sort(result.begin(), result.end());
        if (result.size() == 0)
            cout << -1;
        else
            for (int i = 0; i < result.size(); i++) cout << result[i] << " ";
        cout << endl;
    }
    return 0;
}  // } Driver Code Ends