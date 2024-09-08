# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        temp = head
        length = 0
        ans = []
        while temp:
            length += 1
            temp = temp.next
            
        extra_nodes = length % k
        part_size = length // k
        
        curr = head
        for i in range(k):
            part_head = curr
            part_length = part_size + (1 if i < extra_nodes else 0)

            for j in range(part_length-1):
                if curr:
                    curr = curr.next
            
            if curr:
                next_part = curr.next
                curr.next = None
                curr = next_part

            ans.append(part_head)

        while len(ans)< k:
            ans.append(None)
        return ans
                   