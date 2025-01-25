class Solution {
private:
    int time = 1;
    void dfs(int id,int parent, int tin[], int low[], vector<int> &vis, vector<int> adj[], vector<vector<int>> &res){
        vis[id]=1;
        tin[id]=low[id]=time;
        time++;
        for(auto i : adj[id]){
            if(i==parent) continue;
            if(!vis[i]){
                dfs(i,id,tin,low,vis,adj,res);
                low[id] = min(low[id],low[i]);
                if(low[i]>tin[id]){
                    res.push_back({i,id});
                }
            }
            else{
                low[id] = min(low[id],low[i]);
            }
        }
    }

public:
    vector<vector<int>> criticalConnections(int n, vector<vector<int>>& connections) {
        vector<int> adj[n];
        for(auto j:connections){
            adj[j[0]].push_back(j[1]);
            adj[j[1]].push_back(j[0]);

        }
        vector<vector<int>> res;
        int tin[n], low[n];
        vector<int> vis(n,0);
        dfs(0,-1,tin,low, vis, adj, res);
        return res;
    }
};