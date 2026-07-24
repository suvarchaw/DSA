# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flipMatchVoyage(self, root, voyage):
         res = []
         self.i = 0
         def dfs(root):
             if not root: return True
             if root.val != voyage[self.i]: return False
             self.i += 1
             if root.left and root.left.val != voyage[self.i]:
                 res.append(root.val)
                 root.left, root.right = root.right, root.left
             return dfs(root.left) and dfs(root.right)
         return res if dfs(root) else [-1]