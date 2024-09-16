class Solution {
public:
    int numberOfSteps(int num) {
        int c=0;
        while(num>0){
            c++;
            if((num&1)==0){
                num=num/2;
            }
            else{
                num--;
            }
        }
        return c;
    }
};