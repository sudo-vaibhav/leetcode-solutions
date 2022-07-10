class Solution {
    
    public int getDist(ArrayList<Integer> startingCell,int houseCount,int[][] grid,boolean[][] ineligible){
        int m = grid.length,n=grid[0].length;
        boolean[][] vis = new boolean[m][n];
        int ans = 0;
        Queue<ArrayList<Integer>> q = new LinkedList<ArrayList<Integer>> ();
        int[][] diffs = {
            {0,-1},
            {-1,0},
            {1,0},
            {0,1}
        };
        q.add(startingCell);
        vis[startingCell.get(0)][startingCell.get(1)]=true;
        int steps = 0;
        int visitedHouses = 0;
        while(q.size()!=0){
            int lenq = q.size();
            for(int x=0;x<lenq;x++){
                var cur = q.poll();
                int i=cur.get(0),j=cur.get(1);
                if(grid[i][j]==1){
                    ans+= steps;
                    visitedHouses++;
                }
                else{
                    for(var diff:diffs){
                        int I = i+diff[0],J = j+diff[1];
                        if (0<=I && I<m && 0<=J && J<n){
                            if(grid[I][J]!=2 && !vis[I][J]){
                                vis[I][J] = true;
                                var temp = new ArrayList<Integer>();
                                temp.add(I);temp.add(J);
                                q.add(temp);
                            }
                        }
                    }
                }
            }
            
            steps++;
        }
        if (visitedHouses==houseCount){
            return ans;
        }
        else{
            
//             mark all other visited empty cells as ineligible as those cant reach either
            for(int i=0;i<m;i++){
                for(int j=0;j<n;j++){
                    if(vis[i][j]){
                        ineligible[i][j]=true;
                    }
                }
            }
            return Integer.MAX_VALUE;
        }
        
    }
    
    public int shortestDistance(int[][] grid) {
        int m = grid.length,n=grid[0].length;
        int houseCount = 0;
        ArrayList<ArrayList<Integer>> emptyCells = new ArrayList<>();
        boolean[][] ineligible = new boolean[m][n];
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(grid[i][j]==0){
                    var temp = new ArrayList<Integer>();
                    temp.add(i);
                    temp.add(j);
                    emptyCells.add(temp);
                }
                else if(grid[i][j]==1){
                    houseCount++;
                }
            }
        }
        
        var ans = Integer.MAX_VALUE; 
        for(var ec:emptyCells){
            if(!ineligible[ec.get(0)][ec.get(1)]){
                var temp = getDist(ec,houseCount,grid,ineligible);
                ans = Math.min(temp,ans);
            }
        }
        
        if(ans==Integer.MAX_VALUE) return -1;
        return ans;
        
    }
}