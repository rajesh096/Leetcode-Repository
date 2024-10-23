class Solution {
public:
    double averageWaitingTime(vector<vector<int>>& customers) {
        double total=0;
        int arival=0;
        for(int i=0;i<customers.size();i++){
            arival=max(arival,customers[i][0]);
            int s=arival+customers[i][1];
            total+=s-customers[i][0];
            arival=s;
        }
        return total/customers.size();
    }
};