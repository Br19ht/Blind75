# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l, r = head, head
        counter = 0

        while r:
            r = r.next
            counter += 1
        
        counter = counter // 2
        
        for i in range(counter):
            l = l.next
        
        return l
            