class Solution {
public:
    bool dfs(int node, vector<int> &visited, vector<vector<int>> &adj) {
        if (visited[node] == 1) return true;  
        if (visited[node] == 2) return false; 

        visited[node] = 1; 
        for (int neighbor : adj[node]) {
            if (dfs(neighbor, visited, adj)) return true;
        }
        visited[node] = 2; 
        return false;
    }

    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> adj(numCourses);
        for (const auto& pair : prerequisites) {
            adj[pair[1]].push_back(pair[0]);
        }

        vector<int> visited(numCourses, 0); 
        for (int i = 0; i < numCourses; ++i) {
            if (visited[i] == 0) {
                if (dfs(i, visited, adj)) return false;
            }
        }
        return true;
    }
};
