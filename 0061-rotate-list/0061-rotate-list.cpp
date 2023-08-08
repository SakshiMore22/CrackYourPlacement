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
    ListNode* rotateRight(ListNode* head, int k) {
        if(head==NULL || head->next==NULL || k==0){
            return head;
        }
        int cnt=1;
        ListNode* temp=head;
        while(temp->next!=NULL){
            cnt=cnt+1;
            temp=temp->next;
        }
        temp->next=head;
        cout<<cnt<<endl;
        k=k%cnt;
        int K=cnt-k-1;
        cout<<K<<endl;
        ListNode* temp2=head;
        while (K>0){
            temp2=temp2->next;
            K-=1;
        }
        ListNode* ans=temp2->next;
        temp2->next=NULL;
        return ans;
    }
};