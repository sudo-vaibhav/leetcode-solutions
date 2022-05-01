class Solution {
public:
    bool hasCycle(
    int i, int n,vector<vector<int>>& graph,bool visited[],
    bool dfsVisited[],vector<int>& ans, vector<int>& path
    ){
        visited[i] =1;
        dfsVisited[i]=1;
        for(auto neighbor: graph[i]){
            if(!visited[neighbor]){
                if(hasCycle(neighbor,n,graph,visited,dfsVisited,ans,path)){
                    return true;
                }
            }
            else{
                if(dfsVisited[neighbor]) return true;
            }
        }
        
        dfsVisited[i] = 0;
        path.insert(path.begin(),i);
        if(path.size()==n){
            ans.insert(ans.end(),path.begin(),path.end());
        }
        // path.pop_back();
        return false;
    }
    
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<int> ans,path;
        bool visited[numCourses],dfsVisited[numCourses];
        memset(visited,false,numCourses);
        memset(dfsVisited,false,numCourses);
        vector<vector<int>> graph(numCourses);
        
        for(auto p: prerequisites){
            graph[p[1]].push_back(p[0]);
        }
        
        for(int i=0;i<numCourses;i++){
            if(!visited[i]&&hasCycle(i,numCourses,graph,visited,dfsVisited,ans,path)){
                return {};
            }
        }
        
        return ans;
        
    }
};