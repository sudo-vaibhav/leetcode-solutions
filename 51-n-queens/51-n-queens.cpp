class Solution {
public:
    vector<string> convert(vector<vector<int>>& matrix){
        vector<string> res;
        for(auto row:matrix){
            string temp = "";
            for(auto v:row){
                temp+= (v==0) ? "." : "Q";
            }
            
            res.push_back(temp);
        }
        return res;
    }
    bool check(int row,int col,int n,vector<vector<int>>& matrix){
        // for(int j=0;j<n;j++){
        //     if(matrix[j][col]) return false;
        // }
        for(int j=0;j<n;j++){
            if(matrix[row][j]) return false;
        }
        int i=0;
        for(int j=col-1;j>=0;j--){
            i++;
            if(row-i>=0 && matrix[row-i][j]){
                return false;
            }
            if(row+i<n && matrix[row+i][j]){
                return false;
            }
        }
        
        return true;
    }
    void solve(int col, int n, vector<vector<int>>& matrix,vector<vector<string>>& ans){
        for(int row = 0;row<n;row++){
            if(check(row,col,n,matrix)){
                matrix[row][col] = 1;
                if(col==n-1){
                    ans.push_back(convert(matrix));
                }else{
                    solve(col+1,n,matrix,ans);    
                }
                matrix[row][col] = 0;
            }
        }
    }
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<int>> queenMatrix;
        for(int i=0;i<n;i++){
            queenMatrix.push_back(vector<int>(n,0));
        }
        vector<vector<string>> ans;
        solve(0,n,queenMatrix,ans);
        return ans;
    }
};