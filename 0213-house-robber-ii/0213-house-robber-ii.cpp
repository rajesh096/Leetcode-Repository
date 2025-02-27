class Solution {
public:
    int func(vector<int> nums){
        if(nums.size()==0) return 0;
        if(nums.size()==1) return nums[0];
        vector<int> dp (nums.size(), 0);
        dp[0] = nums[0];
        dp[1] = max(nums[1],nums[0]);
        for(int i=2;i<nums.size();i++){
            dp[i] = max(dp[i-1],dp[i-2]+nums[i]);
        }
        return dp[nums.size()-1];
    }
    int rob(vector<int>& nums) {
        int n = nums.size();
        if(n==1) return nums[0];
        vector<int> arr1, arr2;
        for(int i=0;i<n;i++){
            if(i!=0) arr1.push_back(nums[i]);
            if(i!=n-1) arr2.push_back(nums[i]);
        }
        return max(func(arr1), func(arr2));
    }
};