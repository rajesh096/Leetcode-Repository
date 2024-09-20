class Solution:
    def shortestPalindrome(self, s: str) -> str:
       
        rev_s = s[::-1]
        
        # Create a new string temp
        temp = s + "#" + rev_s
        
        # Compute KMP table
        n = len(temp)
        kmp_table = [0] * n
        
        # Build the KMP table
        for i in range(1, n):
            j = kmp_table[i - 1]
            
            while j > 0 and temp[i] != temp[j]:
                j = kmp_table[j - 1]
            
            if temp[i] == temp[j]:
                j += 1
            
            kmp_table[i] = j
        
        # Find the length of the longest palindrome prefix
        longest_palindrome_prefix_len = kmp_table[-1]
        
        # Add the remaining characters of rev_s in front of s
        return rev_s[:len(s) - longest_palindrome_prefix_len] + s


