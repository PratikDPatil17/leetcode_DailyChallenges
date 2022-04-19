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
        curr = root
        prev = TreeNode (float('-inf'))
        replace = []
        stack = []
        
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
                
            tmp = stack.pop()
            
            if tmp.val < prev.val:
                replace.append ((prev, tmp))
                
            prev = tmp
            curr = tmp.right
            
        replace[0][0].val, replace[-1][1].val = replace[-1][1].val, replace[0][0].val
        
        
        
        