// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


 // } Driver Code Ends
//Function to determine if graph can be coloured with at most M colours such
//that no two adjacent vertices of graph are coloured with same colour.
bool solve(int node, int V, bool graph[101][101],int m, unordered_map<int,int>& colors){
    if(node==V) return true;
    // bool possible = false;
    for(int color=0;color<m;color++){
        bool colorInUse = false;
        for(int neighbor=0;neighbor<V;neighbor++){
            if(graph[node][neighbor]&&node!=neighbor&&colors.count(neighbor)&& colors[neighbor]==color){
                colorInUse = true;
                break;
            }
        }
        if(!colorInUse){
            colors[node] = color;
            if(solve(node+1,V,graph,m,colors)){
                return true;
            }
            colors.erase(node);
        }
    }
    
    return false;
}

bool graphColoring(bool graph[101][101], int m, int V)
{
    // your code here
    unordered_map<int, int> colors;
    return solve(0,V,graph,m,colors);
}

// { Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, m, e;
        cin >> n >> m >> e;
        int i;
        bool graph[101][101];
        for (i = 0; i < n; i++) {
            memset(graph[i], 0, sizeof(graph[i]));
        }
        for (i = 0; i < e; i++) {
            int a, b;
            cin >> a >> b;
            graph[a - 1][b - 1] = 1;
            graph[b - 1][a - 1] = 1;
        }
        cout << graphColoring(graph, m, n) << endl;
    }
    return 0;
}
  // } Driver Code Ends