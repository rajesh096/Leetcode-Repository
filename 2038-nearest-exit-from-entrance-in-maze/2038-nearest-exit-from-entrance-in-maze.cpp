class Solution {
public:
    int dx[4] = {-1,0,0,1};
    int dy[4] = {0,-1,1,0};
    int nearestExit(vector<vector<char>>& maze, vector<int>& entrance) {
        int n = maze.size(), m = maze[0].size();
        int s = entrance[0], r = entrance[1];
        vector<vector<int>> res(n, vector<int> (m, INT_MAX));
        queue<pair<int, int>> q;
        
        q.push({s,r});
        res[s][r] = 0;
        int mini = INT_MAX;
        while(!q.empty()){
            int x = q.front().first, y = q.front().second;
            q.pop();
            for(int i=0;i<4;i++){
                int nx = x + dx[i];
                int ny = y + dy[i];
                if(nx>=0 && nx<n && ny>=0 && ny<m && maze[nx][ny]=='.' && res[x][y] + 1 < res[nx][ny]){
                    res[nx][ny] = res[x][y] + 1;
                    q.push({nx,ny});
                    if(nx==0 || ny == 0 || nx == n-1 || ny == m-1){
                        mini = min(mini, res[nx][ny]);
                    }
                }
            }
        }
        return  mini==INT_MAX ? -1 : mini;
    }
};