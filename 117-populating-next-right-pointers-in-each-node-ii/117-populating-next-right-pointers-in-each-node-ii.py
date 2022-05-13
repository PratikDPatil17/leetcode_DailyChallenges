"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        prev = [root, -1]
        stack = [[root, 0]]
        while stack:
            r, d = stack.pop(0)
            if not r:
                continue
            
            if prev[1] == d:
                prev[0].next = r
            
            prev = [r, d]
            stack += [[r.left,  d+1]]
            stack += [[r.right, d+1]]
            
        return root