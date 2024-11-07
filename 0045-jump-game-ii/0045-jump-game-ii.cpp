#include <vector>
#include <climits>
using namespace std;

class Solution {
public:
    int jumpHelper(int i, vector<int>& nums, vector<int>& dp) {
        int n = nums.size();
        if (i >= n - 1) return 0;  // Reached the last index or beyond, no more jumps needed.
        
        if (dp[i] != -1) return dp[i];  // Return previously computed result to avoid redundant work.

        int minJumps = INT_MAX;  // Initialize minJumps to a large value.

        // Try every possible jump from the current position.
        for (int j = 1; j <= nums[i]; ++j) {
            int nextIndex = i + j;
            if (nextIndex < n) {
                int jumps = jumpHelper(nextIndex, nums, dp);
                if (jumps != INT_MAX) {  // Check if reaching the end is possible from this jump.
                    minJumps = min(minJumps, jumps + 1);
                }
            }
        }
        
        dp[i] = minJumps;  // Store the result in dp array for memoization.
        return dp[i];
    }
    
    int jump(vector<int>& nums) {
        int n = nums.size();
        vector<int> dp(n, -1);  // Initialize dp array with -1 (indicating uncomputed values).
        return jumpHelper(0, nums, dp);  // Start the recursive function from index 0.
    }
};
