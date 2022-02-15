# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def getMinMax(self, minmax):
        res = [-1, -1]
        res[0] = float('inf')
        res[1] = minmax[-1] - minmax[0]
        for i in range(len(minmax) - 1):
            res[0] = min(res[0], minmax[i + 1] - minmax[i])

        return res

    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        res = [-1, -1]
        if head == None or head.next == None or head.next.next == None:
            return res
        minmax = []

        pre = None
        cur = head
        cur_i = 0

        while cur.next != None:
            if pre and (pre.val < cur.val > cur.next.val):
                minmax.append(cur_i)
            elif pre and (pre.val > cur.val < cur.next.val):
                minmax.append(cur_i)

            cur_i += 1
            pre = cur
            cur = cur.next

        if len(minmax) > 1:
            return self.getMinMax(minmax)
        else:
            return res
