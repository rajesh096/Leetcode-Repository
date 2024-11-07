#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

class Solution {
public:
    int jump(vector<int>& nums) {
        int n = nums.size();
        if (n <= 1) return 0;  // Already at the end, no jump needed.

        vector<int> dp(n, INT_MAX);  // DP array initialized to a large value.
        dp[0] = 0;  // Start position, no jump required.

        for (int i = 0; i < n; ++i) {
            if (dp[i] == INT_MAX) continue;  // Skip unreachable positions
            
            int maxJump = min(i + nums[i], n - 1);  // Max reachable position from i
            for (int j = i + 1; j <= maxJump; ++j) {
                dp[j] = min(dp[j], dp[i] + 1);  // Update the minimum jumps to reach position j
            }
        }

        return dp[n - 1];  // Minimum jumps to reach the last index.
    }
};
