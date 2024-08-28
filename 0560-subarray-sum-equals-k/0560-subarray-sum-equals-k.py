from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0
        prefix_sum_map = {0: 1}  # Dictionary to store prefix sums

        for num in nums:
            current_sum += num

            # Check if (current_sum - k) exists in the prefix_sum_map
            if current_sum - k in prefix_sum_map:
                count += prefix_sum_map[current_sum - k]

            # Update the prefix_sum_map with the current sum
            if current_sum in prefix_sum_map:
                prefix_sum_map[current_sum] += 1
            else:
                prefix_sum_map[current_sum] = 1

        return count
