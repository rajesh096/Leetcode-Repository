class Solution {
public:
    int minMoves(int target, int maxDoubles) {
        int res=0;
        while(target>1){
            if(target%2==1){
                target--;
                res++;
            }
            if(maxDoubles!=0){
                target/=2;
                res++;
                maxDoubles--;
            }
            else{
                res+=(target-1);
                target=1;
            }
        }
        return res;
    }
};