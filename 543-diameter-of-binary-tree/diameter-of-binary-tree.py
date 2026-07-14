# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
     self.res = 0
     def helper(root):
        if not root: return 0
        left, right = helper(root.left), helper(root.right)
        self.res = max(self.res, left + right)
        return 1 + max(left, right)
     helper(root)
     return self.res
        