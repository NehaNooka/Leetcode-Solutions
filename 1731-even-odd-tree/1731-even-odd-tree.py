# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue=deque([root])
        even=True
        while queue:
            prev=float('-inf') if even else float('inf')
            for _ in range(len(queue)):
                ele=queue.popleft()
                if even and (ele.val%2==0 or ele.val<=prev):
                    return False
                elif not even and (ele.val%2==1 or ele.val >=prev):
                    return False
                
                if ele.left: queue.append(ele.left)
                if ele.right:queue.append(ele.right)
                prev=ele.val
            even= not even

        return True
        