class Solution {
public:
    long long countBadPairs(vector<int>& nums) {
        long long n = nums.size();
        long long pairs = (n*(n-1))/2;
        unordered_map<long long, long long> freq;
        long long count = 0;
        for(int i = 0; i < nums.size(); i++)
        {
            int key = nums[i] - i;
            count += freq[key];
            freq[key]++; 
        }
        return pairs - count;

    }
};