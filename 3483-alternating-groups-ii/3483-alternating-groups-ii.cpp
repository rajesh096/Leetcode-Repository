class Solution {
public:
    int numberOfAlternatingGroups(vector<int>& colors, int k) {
        int n = colors.size();
        for(int i=0;i<k-1;i++){
            colors.push_back(colors[i]);
        }
        int res =0, wrong = 0, prev = colors[0];
        for(int i=1;i<k;i++){
            if(prev==colors[i]) wrong++;
            prev = colors[i];
        }
        if(!wrong) res++;
        if(colors[0]==colors[1]) wrong--;
        for(int i=k;i<colors.size();i++){
            // cout<<i<<" "<<prev<<" "<<wrong<<endl;
            if(colors[i-k+1]!=colors[i-k+2] && !wrong){
                if(prev!=colors[i]){
                    res++;
                }
                // else{
                //     wrong++;
                // }
            }
            else if(colors[i-k+1]==colors[i-k+2]){
                wrong--;
            }
            if(prev==colors[i]){
                wrong++;
            }
            prev = colors[i];
        }
        return res;
    }
};