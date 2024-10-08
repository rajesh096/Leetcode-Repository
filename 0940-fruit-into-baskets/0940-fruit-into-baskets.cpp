class Solution {
public:
    int totalFruit(vector<int>& fruits) {
        unordered_map<int,int> mp;
        int i=0,j=0;
        int m=0;
        while(j<fruits.size()){
            // if(mp.find(fruits[j]) != mp.end()){
            //     fruits[j]+=1;
            // }
            // else{
            //     fruits[j]=1;
            // }
            mp[fruits[j]]++;
            cout<<fruits[j]<<endl;
            while(mp.size()>2){
                mp[fruits[i]]-=1;
                if(mp[fruits[i]]==0) mp.erase(fruits[i]);
                i++;
            }
            if(mp.size()<=2) m=max(m,j-i+1);
            j++;
        } 
        return m;
    }
};