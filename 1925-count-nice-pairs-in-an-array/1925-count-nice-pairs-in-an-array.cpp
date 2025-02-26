class Solution {
public:
    int rev(int i){
        int val = 0;
        while(i > 0){
            val = (val * 10) + (i % 10);
            i /= 10;
        }
        return val;
    }

    int countNicePairs(vector<int>& nums) {
        unordered_map<int, int> mp;
        for(int it : nums){
            mp[it - rev(it)]++;
        }
        long long res = 0;
        for(auto v : mp){
            long long a = v.second;
            res += (a * (a - 1)) / 2;
            res %= 1000000007;
        }

        return (int)(res % 1000000007);
    }
};
