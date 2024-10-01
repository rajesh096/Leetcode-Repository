class Solution {
public:
    string intToRoman(int num) {
        string st=to_string(num);
        int n=st.size();
        map<int,string> mp={
            {1,"I"},{5,"V"},{10,"X"},{50,"L"},{100,"C"},{500,"D"},{1000,"M"}
        };
        string res="";
        for(int i=0;i<n;i++){
            int cv=st[i]-'0';
            int p=n-i-1;
            int po=pow(10,p)+0.1;
            if(cv==4){
                res+=mp[po]+mp[5*po];
            }
            else if(cv==9){
                res+=mp[po]+mp[10*po];
            }
            else{
                if(cv>=5){
                    res+=mp[5*po];
                    cv%=5;
                }
                while(cv--){
                    res+=mp[po];
                }
            }
        }
        return res;
    }
};