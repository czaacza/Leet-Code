# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def areSame(root1, root2):
            if root1 is None and root2 is None:
                return True
            
            if root1 is None or root2 is None:
                return False
            
            if root1.val != root2.val:
                return False
            
            return root1.val == root2.val and areSame(root1.left, root2.left) and areSame(root1.right, root2.right)
        
        def dfs(root, subRoot):
            if root is None:
                return False
            
            return areSame(root, subRoot) or dfs(root.left, subRoot) or dfs(root.right, subRoot)
        
        return dfs(root, subRoot)
                
            
            
        
        
        
        
        
        