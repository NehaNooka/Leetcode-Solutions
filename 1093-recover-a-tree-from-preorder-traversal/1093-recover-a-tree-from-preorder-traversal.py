# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> TreeNode:
        for i in range(100,0,-1):
            traversal = traversal.replace("-"*i,chr(i+65))

        def function(result,depth):
            result = result.split(chr(depth+65))
            root = TreeNode(int(result[0]))
            root.left = function(result[1],depth+1) if len(result) > 1 else None
            root.right = function(result[2],depth+1) if len(result) > 2 else None
            return root 

        return function(traversal,1)