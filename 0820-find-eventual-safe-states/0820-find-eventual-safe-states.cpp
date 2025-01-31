class Solution {
public:
    bool dfs(int node, vector<vector<int>> &graph, vector<int>&vis, vector<int> &incycle){
        if(incycle[node]==1){
            return true;
        }
        if(vis[node]){
            return false;
        }
        vis[node] = 1;
        incycle[node] = 1;
        for(int it : graph[node]){
                if(dfs(it, graph, vis, incycle)){
                    return true;
                }
            
        }
        incycle[node] = 2;
        return false;
    }
    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        int v = graph.size();
        vector<int>vis(v, 0);
        vector<int> incycle(v, 0);
        for(int i=0;i<v;i++){
            dfs(i,graph,vis,incycle);
            
        }
        vector<int> res;
        for(int i=0;i<v;i++){
            if(incycle[i]==2) res.push_back(i);
        }
        return res;
    }
};