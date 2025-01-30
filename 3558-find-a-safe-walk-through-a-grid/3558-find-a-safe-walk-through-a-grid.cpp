
class Solution {
public:
    int dx[4] = {-1, 0, 0, 1};
    int dy[4] = {0, -1, 1, 0};

    bool findSafeWalk(vector<vector<int>>& grid, int health) {
        int n = grid.size(), m = grid[0].size();
        vector<vector<vector<bool>>> visited(n, vector<vector<bool>>(m, vector<bool>(health + 1, false)));
        queue<pair<pair<int, int>, int>> q;

        if (grid[0][0] == 1) health--;
        if (health < 1) return false;

        q.push({{0, 0}, health});
        visited[0][0][health] = true;

        while (!q.empty()) {
            int x = q.front().first.first;
            int y = q.front().first.second;
            int h = q.front().second;
            q.pop();

            if (x == n - 1 && y == m - 1) return true;

            for (int i = 0; i < 4; ++i) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
                    int newHealth = h - grid[nx][ny];
                    if (newHealth >= 1 && !visited[nx][ny][newHealth]) {
                        visited[nx][ny][newHealth] = true;
                        q.push({{nx, ny}, newHealth});
                    }
                }
            }
        }

        return false;
    }
};
