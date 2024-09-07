# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        # Start the search from the current root and also explore the left and right children
        return self.dfs(root, head) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
    
    def dfs(self, root: Optional[TreeNode], head: Optional[ListNode]) -> bool:
        if not head:  # If we've reached the end of the linked list, we found a match
            return True
        if not root:  # If the tree is exhausted but the list is not, no match
            return False
        # If the current node values match, recursively check the left and right subtrees
        if root.val == head.val:
            return self.dfs(root.left, head.next) or self.dfs(root.right, head.next)
        return False
 