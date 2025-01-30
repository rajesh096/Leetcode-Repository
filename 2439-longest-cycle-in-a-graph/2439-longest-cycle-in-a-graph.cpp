class Solution {
public:
    int longestCycle(vector<int>& edges) {
        int n = edges.size(), l = -1;
        vector<int> visit(n, 0);

        for (int i = 0, time = 1, j, curr_time; i < n; i++) {
            j = i, curr_time = time;
            while (j != -1 && !visit[j]) {
                visit[j] = time++;
                j = edges[j];
            }
            if (j != -1 && visit[j] >= curr_time) l = max(l, time - visit[j]);
        }

        return l;
    }
};