class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Convert wordDict into a set for O(1) lookup
        wordSet = set(wordDict)
        
        # Use a list to track positions that are valid starting points for words
        valid_positions = {0}  # Start with the 0th position (before the first character)
        
        # Iterate through the string by expanding the end of potential substrings
        for i in range(1, len(s) + 1):
            for j in valid_positions:
                # Check if the substring s[j:i] is in the wordSet
                if s[j:i] in wordSet:
                    # If we find a valid word, add the current end position i to valid_positions
                    valid_positions.add(i)
                    break
        
        # If the last position is in valid_positions, the entire string can be segmented
        return len(s) in valid_positions
