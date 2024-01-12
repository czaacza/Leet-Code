# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        max_diff = 0
        def dfs(node, max_an, min_an):
            nonlocal max_diff
            if node is None:
                return
            
            max_an = max(max_an, node.val)
            min_an = min(min_an, node.val)
        
            max_diff = max(max_diff, abs(max_an - min_an))
            
            dfs(node.left, max_an, min_an)
            dfs(node.right, max_an, min_an)
        
        dfs(root, 0, math.inf)

        return max_diff
        

        