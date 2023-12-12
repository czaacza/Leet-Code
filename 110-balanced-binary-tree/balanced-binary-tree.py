# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isTreeBalanced = [True]
        def dfs(node):
            if node is None:
                return 0
            
            left_h = dfs(node.left)
            right_h = dfs(node.right)
            
            if abs(left_h - right_h) > 1:
                isTreeBalanced[0] = False
                return max(left_h , right_h) + 1
                
            
            return max(left_h , right_h) + 1
        
        dfs(root)
        return isTreeBalanced[0]
        