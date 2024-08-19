class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.strip(" ").split(' ')
        l=l[::-1]
        st=""
        for i in l:
            if i != "":
                st+=i
                st+=" "
            
        return st.strip()