# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        prevLeft,cur=dummy,head
        for _ in range(left-1):
            prevLeft,cur=cur,cur.next
        
        prev=None
        for _ in range(right-left+1):
            tmpNext=cur.next
            cur.next=prev
            cur,prev=tmpNext,cur
        
        prevLeft.next.next=cur
        prevLeft.next=prev

        return dummy.next
