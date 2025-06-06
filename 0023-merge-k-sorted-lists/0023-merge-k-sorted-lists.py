# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists)==0: return None

        def sort_lists(l1,l2):
            dummy=ListNode()
            res=dummy
            while l1 and l2:
                if l1.val<=l2.val:
                    res.next=l1
                    l1=l1.next
                else:
                    res.next=l2
                    l2=l2.next
                res=res.next
            if l1:
                res.next=l1
            if l2:
                res.next=l2  
            return dummy.next 

        while len(lists)>1:
            merged_lists=[]
            for i in range(0,len(lists),2):
                l1=lists[i]
                l2=lists[i+1] if (i+1)<len(lists) else None
                merged_lists.append(sort_lists(l1,l2))
            lists=merged_lists
        return lists[0]             

        