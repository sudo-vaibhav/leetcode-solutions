class Solution {
public:
    unordered_map<int,bool> rowMap, upperDiagMap, lowerDiagMap;
    vector<string> convert(vector<vector<bool>>& matrix){
        vector<string> res;
        for(auto row:matrix){
            string temp = "";
            for(auto v:row){
                temp+= (v==false) ? "." : "Q";
            }
            
            res.push_back(temp);
        }
        return res;
    }
    bool check(int row,int col){
        if(rowMap.count(row)||upperDiagMap.count(col-row)||lowerDiagMap.count(col+row)) return false;
        return true;
    }
    void solve(int col, int n, vector<vector<bool>>& matrix,vector<vector<string>>& ans){
        for(int row = 0;row<n;row++){
            if(check(row,col)){
                matrix[row][col] = 1;
                rowMap[row]=true; 
                upperDiagMap[col-row]=true;
                lowerDiagMap[col+row]=true;
                if(col==n-1){
                    ans.push_back(convert(matrix));
                }else{
                    solve(col+1,n,matrix,ans);    
                }
                rowMap.erase(row); 
                upperDiagMap.erase(col-row); 
                lowerDiagMap.erase(col+row);
                matrix[row][col] = 0;
            }
        }
    }
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<bool>> queenMatrix;
        for(int i=0;i<n;i++){
            queenMatrix.push_back(vector<bool>(n,false));
        }
        vector<vector<string>> ans;
        solve(0,n,queenMatrix,ans);
        return ans;
    }
};