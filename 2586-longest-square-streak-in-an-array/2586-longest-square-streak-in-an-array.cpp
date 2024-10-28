class Solution {
public:
    int longestSquareStreak(vector<int>& nums) {
        set<long long> s(nums.begin(), nums.end());  
        int len = 0;  

        for (int num : nums) {
            int currentLength = 1;
            long long currentNum = num;

            while (currentNum <= sqrt(LLONG_MAX) && s.find(currentNum * currentNum) != s.end()){
                currentLength++;
                currentNum *= currentNum; 
            }
            len = max(len, currentLength);  
        }
        return len >1 ? len : -1;
    }
};
