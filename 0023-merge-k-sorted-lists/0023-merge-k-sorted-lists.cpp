/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        vector<int> res;
        int i=0;
        for(ListNode* ll:lists){
            ListNode* p=ll;
            
            while(p){
                res.push_back(p->val);
                p=p->next;
                cout<<res[i++];
            }
        }
        sort(res.begin(),res.end());
        ListNode* head = nullptr; 
        ListNode* tail = nullptr;  
        for (int k : res) {
            ListNode* newNode = new ListNode(k); 
            
            if (!head) {
                head = newNode;  
                tail = newNode;  
            } else {
                tail->next = newNode; 
                tail = newNode;        
            }
        }
        return head;
    }
};