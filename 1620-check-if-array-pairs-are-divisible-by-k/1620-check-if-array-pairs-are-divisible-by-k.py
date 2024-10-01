class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainder_count = [0] * k
    
        # Count the remainder frequency
        for num in arr:
            remainder = num % k
            remainder_count[remainder] += 1
        
        # Now check for valid pairing conditions
        for r in range(k):
            if r == 0:
                # Special case: remainder 0 must pair with another remainder 0
                if remainder_count[r] % 2 != 0:
                    return False
            else:
                # The count of remainder r must match the count of (k - r) % k
                if remainder_count[r] != remainder_count[k - r]:
                    return False
        
        return True