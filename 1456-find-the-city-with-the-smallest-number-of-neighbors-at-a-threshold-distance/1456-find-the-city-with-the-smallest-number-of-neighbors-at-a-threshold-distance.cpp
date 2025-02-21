class Solution {
public:
    int findTheCity(int n, vector<vector<int>>& edges, int distanceThreshold) {
        vector<vector<int>> des(n,vector<int>(n, INT_MAX));
        for(auto edge : edges){
            des[edge[0]][edge[1]] = edge[2];
            des[edge[1]][edge[0]] = edge[2];
        }
        for(int i=0;i<n;i++) des[i][i] = 0;
        for(int i=0; i<n;i++){
            for(int j = 0; j<n;j++){
                for(int k = 0; k < n ; k++){
                    if(des[i][k] == INT_MAX || des[j][i] == INT_MAX) continue;
                    des[j][k] = min(des[j][i]+des[i][k], des[j][k]);
                }
            }
        }
        int cy = n;
        int res = -1;
        for(int i=0;i<n;i++){
            int cnt = 0;
            for(int j = 0;j<n;j++){
                if(des[i][j]<=distanceThreshold){
                    cnt++;
                }
            }
            if(cnt <= cy){
                cy = cnt;
                res = i;
            }
        }
        return res;
    }
};