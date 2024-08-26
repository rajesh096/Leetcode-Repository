class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        
        valid_positions = {0} 
        for i in range(1, len(s) + 1):
            for j in valid_positions:
                if s[j:i] in wordSet:
                    valid_positions.add(i)
                    break
            print(valid_positions)
        
        return len(s) in valid_positions
