class Solution {
public:
    string getSmallestString(int n, int k) {
        int z = 0;
        z += k/26;
        k = k%26;
        n =n-z;
        string res;
        while(n>0){
            if(n>0 & k==0){
                n++;
                k = 26;
                z--;
                res+= 'a';
            }
            else if(n==1){
                res+= char(97+k-1);
            }
            else{
                res+= 'a';
            }
            n--;
            k--;
        }
        for(int i=0;i<z;i++){
            res+='z';
        }
        return res;
    }
};