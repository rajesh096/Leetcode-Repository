class Solution {
public:
    int dx[4] = {-1, 0, 0, 1};
    int dy[4] = {0, -1, 1, 0};
    int minTimeToReach(vector<vector<int>>& moveTime) {
        int n = moveTime.size() , m = moveTime[0].size();
       priority_queue<pair<int, pair<int, int>>, vector<pair<int, pair<int, int>>>, greater<pair<int, pair<int, int>>>> pq;
       vector<vector<int>> res (n, vector<int>(m, INT_MAX));
        int time = 0;
        moveTime[0][0] = 0;
        res[0][0] = 0;
        pq.push({time,{0, 0}});
        while(!pq.empty()){
            int size = pq.size();
            for(int k = 0; k < size; k++){
                int time = pq.top().first;
                int row = pq.top().second.first;
                int col = pq.top().second.second;
                pq.pop();

                if(row == n - 1 && col == m - 1) return time;
                for(int i = 0; i < 4; i++){
                    int x = row + dx[i];
                    int y = col + dy[i];

                    if(x >= 0 && x < n && y >=0 && y < m){
                        int t = max(time, moveTime[x][y])+1;
                        if(t < res[x][y]){
                            res[x][y] = t;
                            pq.push({t,{x, y}});
                        }
                    }
                }
            }    
        }
        return -1;
    }
};