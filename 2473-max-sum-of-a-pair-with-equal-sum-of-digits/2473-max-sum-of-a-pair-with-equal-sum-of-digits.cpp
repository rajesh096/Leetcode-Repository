class Solution {
public:
    int maximumSum(vector<int>& nums) {
        unordered_map<int, vector<int>> mp;
        for(int it : nums){
            int num = it;
            int sm = 0;
            while(num>0){
                sm+=num%10;
                num/=10;
            }
            mp[sm].push_back(it);
        }
        int res = -1;
        for(auto v : mp){
            int n = v.second.size();
            if(n>1){
                sort(v.second.begin(),v.second.end());
                res = max(res, v.second[n-1]+v.second[n-2]);
            }
        }
        return res;
    }
};