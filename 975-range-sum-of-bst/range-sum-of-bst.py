# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        curr_sum = 0
        def dfs(node):
            nonlocal curr_sum
            if node is None:
                return curr_sum
            
            dfs(node.left)
            dfs(node.right)

            if node.val >= low and node.val <= high:
                curr_sum += node.val
            
        dfs(root)
        return curr_sum

            

        