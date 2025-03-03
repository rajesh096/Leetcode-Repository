class Solution {
public:
    vector<int> applyOperations(vector<int>& nums)
    {
        for (int i=0; i<nums.size()-1; i++)
        {
            if (nums[i] == nums[i+1])
            {
                nums[i] *= 2;
                nums[i+1] = 0;
            }
        }

        int n = nums.size();
        int nonZeroIndex = 0; 

    
        for (int i = 0; i < n; i++)
        {
            if (nums[i] != 0)
            {
                swap(nums[i], nums[nonZeroIndex]);
                nonZeroIndex++;
            }
        }
        return nums;
    }
};