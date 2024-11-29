# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.temp=[]
        def inorder(node):
            if not node: return 
            inorder(node.left)
            self.temp.append(node)
            inorder(node.right)
        inorder(root)
        swapA,swapB=self.temp[0],self.temp[-1]

        for i in range(1,len(self.temp)):
            if self.temp[i].val<self.temp[i-1].val:
                swapA=self.temp[i-1]
                break
        for i in range(len(self.temp)-2,-1,-1):
            if self.temp[i].val>self.temp[i+1].val:
                swapB=self.temp[i+1]
                break
        swapA.val,swapB.val=swapB.val,swapA.val
            


        