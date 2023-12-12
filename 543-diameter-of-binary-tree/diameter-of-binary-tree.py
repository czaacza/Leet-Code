# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        max_d = [0]
        def dfs(node):
            if node is None:
                return 0
            
            left_h = dfs(node.left)
            right_h = dfs(node.right)
            
            curr_d = left_h + right_h
            
            max_d[0] = max(max_d[0], curr_d)
            
            return max(left_h, right_h) + 1
    
        dfs(root)
        
        return max_d[0]