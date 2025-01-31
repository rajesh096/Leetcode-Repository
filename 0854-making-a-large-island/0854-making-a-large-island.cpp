class Solution {
public:
    int dx[4] = {-1,0,0,1};
    int dy[4] = {0,-1,1,0};
    int largestIsland(vector<vector<int>>& grid) {
        int n = grid.size(), m = grid[0].size();
        vector<vector<int>> vis(n, vector<int> (m, 0));
        int l = 0;
        queue<pair<int, int>> q;
        map<int, int> mp;
        int temp = 0;
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(!vis[i][j] && grid[i][j]==1){
                    // temp++;
                    q.push({i,j});
                    vis[i][j] = ++l;
                    int count = 0;
                    while(!q.empty()){
                        int x = q.front().first, y = q.front().second;
                        q.pop();
                        temp++;
                        count++;
                        for(int k=0;k<4;k++){
                            int nx = x + dx[k];
                            int ny = y + dy[k];
                            if(nx>=0 && nx<n && ny>=0 && ny<m && !vis[nx][ny] && grid[nx][ny] == 1){
                                vis[nx][ny] = l;
                                q.push({nx,ny});
                            }
                        }
                    }
                    mp[l] = count;
                }
            }
        }
        if(temp==0) return 1;
        if(temp == n*m) return temp;
        int res = 0;
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(grid[i][j]==0){
                    int val = 0 ;
                    set<int> s;
                    for(int k=0;k<4;k++){
                        int nx = i + dx[k];
                        int ny = j + dy[k];
                        if(nx>=0 && ny>=0 && nx<n && ny<m && grid[nx][ny]==1 && !(s.find(vis[nx][ny]) != s.end())){
                            val += mp[vis[nx][ny]];
                            s.insert(vis[nx][ny]);
                        }
                    }
                    res = max(res, val+1);
                }
            }
        }
        return res;
    }
};