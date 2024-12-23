class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        presum=0
        result = 0
        prefix_dict={0:1}
        for val in nums:
            presum+=val
            if(presum-goal in prefix_dict):
                result+=prefix_dict[presum-goal]
            prefix_dict[presum]=prefix_dict[presum]+1 if presum in prefix_dict else 1
        return result