class Solution {
public:
    ListNode *reverseKGroup(ListNode *head, int k) {
        if (!head || k == 1) return head;
        ListNode *dummy = new ListNode(-1);
        ListNode *pre = dummy, *cur = head;
        dummy->next = head;
        int i = 0;
        while (cur) {
            ++i;
            if (i % k == 0) {
                pre = reverseOneGroup(pre, cur->next);
                cur = pre->next;
            } else {
                cur = cur->next;
            }
        }
        return dummy->next;
    }
    ListNode *reverseOneGroup(ListNode *pre, ListNode *next) {
        ListNode *last = pre->next;
        ListNode *cur = last->next;
        while(cur != next) {
            last->next = cur->next;
            cur->next = pre->next;
            pre->next = cur;
            cur = last->next;
        }
        return last;
    }
};