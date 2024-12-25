# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        res=[]
        q=deque([root])
        while q:
            levelMax=float(-inf)
            for _ in range(len(q)):
                ele=q.popleft()
                levelMax=max(levelMax,ele.val)
                if ele.left: q.append(ele.left)
                if ele.right: q.append(ele.right)
            res.append(levelMax)
        return res
        