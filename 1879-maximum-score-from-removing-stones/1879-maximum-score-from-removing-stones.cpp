class Solution {
public:
    int maximumScore(int a, int b, int c) {
        priority_queue<int> pq;
        pq.push(a);
        pq.push(b);
        pq.push(c);
        int result = 0;
        while(true){
            int temp1 = pq.top();pq.pop();
            int temp2 = pq.top();pq.pop();
            if(temp2<=0) break;
            temp1--;temp2--;
            result++;
            pq.push(temp1);
            pq.push(temp2);
        }
        return result;
    }
};