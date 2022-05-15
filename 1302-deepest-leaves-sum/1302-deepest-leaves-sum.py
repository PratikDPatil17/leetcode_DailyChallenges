# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = [root]
        level = []
        while q and root:
            res = 0
            for node in q:
				# We keep on adding node.val and resetting it to get last level value.
                res += node.val
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            q = level
            level = []
        return res