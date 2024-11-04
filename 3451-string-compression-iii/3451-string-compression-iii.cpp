class Solution {
public:
    string compressedString(string word) {
        char ch=word[0];
        int c=1;
        string res;
        for(int i=1;i<word.size();i++){
            if(word[i]==ch && c<9){
                c+=1;
            }
            else{
                res+=to_string(c)+ch;
                ch=word[i];
                c=1;
            }
        }
        res+=to_string(c)+ch;
        return res;
    }
};