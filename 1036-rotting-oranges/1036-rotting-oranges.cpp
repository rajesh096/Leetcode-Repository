class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        if(grid.empty()) return -1;
        queue<pair<int,int>> q;
        int tot = 0,cnt = 0, days = 0,n = grid.size(), m = grid[0].size();
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(grid[i][j]!=0) tot++;
                if(grid[i][j]==2) q.push({i,j});
            }
        }
        int dx[4] = {-1,0,0,1};
        int dy[4] = {0,-1,1,0};
        while(!q.empty()){
            int si = q.size();
            cnt+=si;
            while(si--){
                int x=q.front().first, y = q.front().second;
                q.pop();
                for(int i=0;i<4;i++){
                    int nx = x + dx[i];
                    int ny = y + dy[i];
                    if(nx>=0 && nx<n && ny>=0 && ny<m && grid[nx][ny]==1){
                        grid[nx][ny] = 2;
                        q.push({nx,ny});
                    }
                }
                
            }
            if(!q.empty()) days++;
        }
        return tot==cnt?days:-1;
    }
};