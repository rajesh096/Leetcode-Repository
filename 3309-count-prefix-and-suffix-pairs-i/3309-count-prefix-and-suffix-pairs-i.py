class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(str1, str2):
            flag1 = False
            flag2 = False
            for i in range(len(str1)):
                if(str1[i]==str2[i]):
                    flag1 = True
                else:
                    flag1 = False
                    break
            if(flag1==False):
                return False
            val = len(str2)-len(str1)
            for i in range(len(str1)-1,-1,-1):
                if(str1[i]==str2[i+val]):
                    flag2 = True
                else:
                    flag2 = False
                    break
            if(flag2==False):
                return False
            return True
        
        result = 0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if(len(words[i])<=len(words[j]) and isPrefixAndSuffix(words[i], words[j])):
                    result += 1
        return result