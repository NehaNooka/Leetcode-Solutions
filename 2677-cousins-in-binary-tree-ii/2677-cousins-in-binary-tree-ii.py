# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return
        level_sums=[]
        queue=deque([root])
        while queue:
            level_len=len(queue)
            lev=0
            for i in range(level_len):
                ele=queue.popleft()
                lev+=ele.val
                if ele.left: queue.append(ele.left)
                if ele.right: queue.append(ele.right)
            
            level_sums.append(lev)
        
        queue=deque([root])
        root.val=0
        level=0
        while queue:
            for _ in range(len(queue)):
                ele=queue.popleft()

                child_sum=0
                if ele.left: child_sum+=ele.left.val
                if ele.right: child_sum+=ele.right.val

                if ele.left:
                    ele.left.val=level_sums[level+1]-child_sum
                    queue.append(ele.left)
                if ele.right:
                    ele.right.val=level_sums[level+1]-child_sum
                    queue.append(ele.right)
            level+=1
        
        return root
