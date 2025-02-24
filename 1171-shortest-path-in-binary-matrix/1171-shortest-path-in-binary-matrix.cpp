class Solution {
public:
    int dx[8] = {-1,-1,-1,0,0,1,1,1};
    int dy[8] = {0,-1,1,-1,1,0,-1,1};
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        int p = 0, q = 0, x = grid.size()-1, y = grid[0].size()-1;
        if(grid[p][q] || grid[x][y]) return -1;
        vector<vector<int>> dest(grid.size(), vector<int> (grid[0].size(), INT_MAX));
        queue<pair<int, int>> qu;
        qu.push({p,q});
        dest[p][q]= 0;
        while(!qu.empty()){
            int a = qu.front().first, b = qu.front().second;
            qu.pop();
            for(int i=0;i<8;i++){
                int na = a + dx[i];
                int nb = b + dy[i];
                if(na >=0 && na<grid.size() && nb>=0 && nb<grid[0].size() && grid[na][nb]==0 && dest[a][b] + 1 < dest[na][nb]){
                    dest[na][nb] = dest[a][b] + 1;
                    qu.push({na,nb});
                }
            }
        }
        return (dest[x][y] == INT_MAX)? -1 : dest[x][y]+1;
    }
};