class Solution {
public:
    int countCompleteComponents(int n, vector<vector<int>>& edges) {
        vector<vector<int>> adj(n);
        for(auto edge : edges){
            adj[edge[0]].push_back(edge[1]);
            adj[edge[1]].push_back(edge[0]);
        }
        queue<int>q;
        vector<int> vis(n,0);
        int res=0;
        for(int i=0;i<n;i++){
            if(!vis[i]){
                q.push(i);
                vis[i] = 1;
                int nod = 0, edg = 0;
                while(!q.empty()){
                    nod++;
                    int node = q.front();
                    q.pop();
                    for(int it:adj[node]){
                        if (it!=node)edg++;
                        if(!vis[it]){
                            vis[it] = 1;
                            q.push(it);
                        }
                    }
                }
                cout<<edg<<endl;
                edg/=2;
                if(edg == (nod*(nod-1))/2) res++;
            }
            
        }
        return res;
    }
};