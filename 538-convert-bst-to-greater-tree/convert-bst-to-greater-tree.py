# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    """
since this is a BST, we can do a inorder traversal (inversed, from right to left),
during this process, track the sum and update the node.val
"""

class Solution:
    def convertBST(self, root):
        self.total = 0
        
        def helper(node):
            if not node: return
            helper(node.right)
            node.val += self.total
            self.total = node.val
            helper(node.left)
        
        helper(root)
        return root
        