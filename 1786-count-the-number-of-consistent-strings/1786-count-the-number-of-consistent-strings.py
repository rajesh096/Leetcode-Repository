class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        c = 0
        for i in words:
            if set(i).issubset(allowed):
                c+=1
        return c