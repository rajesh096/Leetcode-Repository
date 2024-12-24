class Solution {
public:
    int maxSumSubmatrix(vector<vector<int>>& matrix, int k) {
        int row = matrix.size();
        int col = matrix[0].size();
        int maxSum = INT_MIN;

        for (int i = 0; i < row; i++) {
            vector<int> colSum(col, 0);
            for (int j = i; j < row; j++) {
                for (int c = 0; c < col; c++) {
                    colSum[c] += matrix[j][c];
                }
                maxSum = max(maxSum, findMax(colSum, k));
            }
        }
        return maxSum;
    }

private:
    int findMax(vector<int>& sum, int k) {
        int result = INT_MIN;
        set<int> prefixSet;
        prefixSet.insert(0); // Similar to set.add(0) in Java
        int prefixSum = 0;

        for (int num : sum) {
            prefixSum += num;

            // Find the smallest prefix >= prefixSum - k
            auto it = prefixSet.lower_bound(prefixSum - k);
            if (it != prefixSet.end()) {
                result = max(result, prefixSum - *it);
            }

            // Insert the current prefix sum into the set
            prefixSet.insert(prefixSum);
        }

        return result;
    }
};