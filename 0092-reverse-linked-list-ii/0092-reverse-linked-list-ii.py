# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)

        prevLeft, cur= dummy,head
        for i in range(left-1):
            cur=cur.next
            prevLeft=prevLeft.next
        
        prev=None
        for i in range(right-left+1):
            tmp=cur.next
            cur.next=prev
            prev,cur=cur,tmp
        
        prevLeft.next.next=cur
        prevLeft.next=prev
        return dummy.next