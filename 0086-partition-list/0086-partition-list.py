# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        leftHead=ListNode()
        l=leftHead
        rightHead=ListNode()
        r=rightHead

        while head:
            if head.val<x:
                l.next=head
                l=l.next
            else:
                r.next=head
                r=r.next
            head=head.next
        
        l.next=rightHead.next
        r.next=None
        return leftHead.next


        