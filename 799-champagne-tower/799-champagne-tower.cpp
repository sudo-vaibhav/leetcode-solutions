class Solution {
public:
    double champagneTower(int poured, int query_row, int query_glass) {
        double flow[102][102];
        for(auto i=0;i<102;i++){
            for(auto j=0;j<102;j++){
                flow[i][j] = 0.0;
            }
        }
        
        flow[0][0] = poured;
        
        for(int r=0;r<=query_row;r++){
            for(int c=0;c<=r;c++){
                double temp = (flow[r][c]-1.0)/2.0;
                
                if(temp>0){
                    flow[r+1][c] +=temp;
                    flow[r+1][c+1] +=temp;
                }
            }
        }
        
        return min(flow[query_row][query_glass],1.0);
    }
};