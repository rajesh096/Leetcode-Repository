class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:

        count  = 0
        results = []
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if self.isPrefixSuffix(words[i], words[j]):
                    results.append((words[i], words[j]))
                    count+=1
        
        # print(results)
        return count

    def isPrefixSuffix(self, word1, word2) -> bool:

        if word2.startswith(word1) and word2.endswith(word1):
            return True
        return False

        