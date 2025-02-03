class Solution {
public:
    vector<vector<int>> highestPeak(vector<vector<int>>& grid) {
        int n = grid.size(), m = grid[0].size();
        vector<vector<int>> res(n, vector<int>(m, INT_MAX));
        queue<pair<int, int>> q;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == 1) {
                    res[i][j] = 0;
                    q.push({i, j});
                }
            }
        }

        int dx[4] = {-1, 0, 0, 1};
        int dy[4] = {0, -1, 1, 0};

        while (!q.empty()) {
            pair<int, int> cell = q.front(); 
            int x = cell.first;
            int y = cell.second;
            q.pop();

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (nx >= 0 && nx < n && ny >= 0 && ny < m && res[nx][ny] > res[x][y] + 1) {
                    res[nx][ny] = res[x][y] + 1;
                    q.push({nx, ny});
                }
            }
        }

        return res;
    }
};