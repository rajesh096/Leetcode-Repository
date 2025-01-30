class Solution {
public:
    long long dfs(int id, const vector<vector<int>>& adj, vector<int>& par, vector<int>& temp, vector<int>& vis, int p = -1) {
        vis[id] = 1;
        par[id] = p;
        temp.push_back(id);
        for (auto it : adj[id]) {
            if (!vis[it]) {
                long long z = dfs(it, adj, par, temp, vis, id);
                if (z != -1) {
                    return z;
                }
            } else if (vis[it] == 1) {
                long long s = 1;
                while (id != it) {
                    s++;
                    id = par[id];
                }
                return s;
            }
        }
        return -1;
    }

    int longestCycle(vector<int>& edges) {
        int N = edges.size();
        vector<vector<int>> adj(N);
        vector<int> par(N, -1);
        vector<int> vis(N, 0);
        long long res = -1; 

        for (int i = 0; i < N; i++) {
            if (edges[i] != -1) {
                adj[i].push_back(edges[i]);
            }
        }

        for (int i = 0; i < N; i++) {
            if (!vis[i]) {
                vector<int> temp;
                long long result = dfs(i, adj, par, temp, vis);
                if (result != -1) {
                    res = max(res, result);
                }
                for (auto it : temp) {
                    vis[it] = 2;
                }
            }
        }
        return res;
    }
};
