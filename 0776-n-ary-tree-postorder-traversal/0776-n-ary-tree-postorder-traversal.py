"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res=[]
        def traverse(node):
            if not node:
                return
        
            for child in node.children:
                traverse(child)
            
            # Visit the current node after its children
            result.append(node.val)
        result=[]
        traverse(root)        
        return result