# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0
        def dfs(node):
            nonlocal res
            if node is None:
                return
            if node.val >= low and node.val <= high:
                res += node.val
                dfs(node.right)
                dfs(node.left)
            elif node.val < low:
                dfs(node.right)
            elif node.val > high:
                dfs(node.left)
        
        dfs(root)

        return res
        