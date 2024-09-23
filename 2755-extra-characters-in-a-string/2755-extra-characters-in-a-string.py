class Solution:
    def minExtraChar(self, st: str, dictionary: List[str]) -> int:
        # d={}
        # s=st
        # for i in dictionary:
        #     d[i]=len(i)
        # d=dict(sorted(d.items(), key=lambda item: item[1],reverse=True))
        # for i in d:
        #     s=s.replace(i,'1')
    
        # res=0
        # for i in s:
        #     if i!='1':
        #         res+=1
        # return res

        word_set = set(dictionary)
        n = len(st)
        
        # Initialize dp array where dp[i] represents the minimum extra characters from index i to the end
        dp = [0] * (n + 1)
        
        # Process from the end of the string to the beginning
        for i in range(n - 1, -1, -1):
            # By default, take 1 extra character (the character at position i)
            dp[i] = dp[i + 1] + 1
            
            # Check all possible substrings starting from index i
            for j in range(i + 1, n + 1):
                if st[i:j] in word_set:
                    dp[i] = min(dp[i], dp[j])
        
        # dp[0] will hold the minimum extra characters starting from index 0
        return dp[0]
