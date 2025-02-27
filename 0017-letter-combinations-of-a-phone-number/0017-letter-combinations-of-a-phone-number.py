from typing import List

class Solution:
    def letterCombinations(self, d: str) -> List[str]:
        if not d:
            return []
        
        dic = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        
        def backtrack(index: int, path: List[str]):
            if index == len(d):
                result.append("".join(path))
                return
            
            letters = dic[d[index]]
            for letter in letters:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()
        
        result = []
        backtrack(0, [])
        return result
