class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n=nums.size();
        int s=(n*(n+1))/2;
        int res=0;
        for(int i:nums) res+=i;
        return s-res;
    }
};