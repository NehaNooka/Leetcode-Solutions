# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        q=deque()
        q.append(root)
        while q:
            qLen=len(q)
            level=[]
            for i in range(qLen):
                ele=q.popleft()
                if ele:
                    level.append(ele.val)
                    q.append(ele.left)
                    q.append(ele.right)
            if level:
                ans.append(level)
        return ans


        
        