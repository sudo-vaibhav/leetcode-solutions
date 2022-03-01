class Solution {
public:
    void populate(int i, int j, vector<vector<int>>& board){
        int temp = board[i][j];
        int ans = 0;
        int n = board.size();
        int m = board[0].size();
        for(int r = -1;r<2;r++){
            for(int c=-1;c<2;c++){
                
                if(
                   !(r==0&&c==0)
                   &&(i+r>=0) && (i+r<n)
                   &&(j+c>=0) && (j+c<m)
                   && (board[i+r][j+c]>=1)
                  ){
                        ans++;
                }
            }
        }
        // cout<<i<<" "<<j<<" "<<ans<<endl;
        if(temp==0){
            ans*=-1;
        }
        if(ans==0){
            if(temp!=0){
                ans = INT_MAX;
            }
            else{
                ans = INT_MIN;    
            }
        }
        
        board[i][j] = ans;
    }
    
    void transition(int i, int j, vector<vector<int>>& board){
        // if live
        int val = board[i][j];
        int neighbors = abs(val);
        if(val>0){
            // live
            if(neighbors<2||neighbors>3){
                board[i][j] = 0;
            }
            else{
                board[i][j] = 1;
            }
            
        }
        else{
            if(neighbors==3){
                board[i][j] = 1;
            }
            else{
                board[i][j] = 0;
            }
            
        }
    }
    
    void gameOfLife(vector<vector<int>>& board) {
        for(auto i=0;i<board.size();i++){
            for(auto j=0;j<board[i].size();j++){
                populate(i,j,board);
                 cout<<board[i][j]<<"\t";
            }
            cout<<endl;
        }
        for(auto i=0;i<board.size();i++){
            for(auto j=0;j<board[i].size();j++){
                transition(i,j,board);
            }
        }
    }
};