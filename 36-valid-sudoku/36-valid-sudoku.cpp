class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        int n = board.size();
        vector<vector<bool>> rowPresent(n,vector<bool>(n,false));
        auto colPresent = rowPresent;
        map<pair<int,int>,set<int>> sectionPresent;
        
        
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                    if(board[i][j]!='.'){
                        int pos = board[i][j] - '1';
                    if(rowPresent[i][pos]){
                        return false;
                    }
                    else{
                        rowPresent[i][pos] = true;
                    }

                    if(colPresent[j][pos]){
                        return false;
                    }
                    else{
                        colPresent[j][pos] = true;
                    }

                    auto I = i/3,J=j/3;
                    if(sectionPresent.count({I,J})&&sectionPresent[{I,J}].count(pos)){
                        return false;
                    }
                    else{
                        sectionPresent[{I,J}].insert(pos);
                    }
                }
                
            }
        }
        
        return true;
    }
};