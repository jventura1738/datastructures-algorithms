# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def dfs(root: TreeNode, target_sum: int) -> bool:
            if not root.right and not root.left:
                return True if target_sum - root.val == 0 else False
            
            left, right = False, False
            if root.left:
                left = dfs(root.left, target_sum - root.val)
            if root.right:
                right = dfs(root.right, target_sum - root.val)
            
            return left or right
        
        return dfs(root, targetSum)
        