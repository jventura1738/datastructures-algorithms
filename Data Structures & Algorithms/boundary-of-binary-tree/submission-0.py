# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        ans = [root.val]
        right = []

        def left_boundary(root: TreeNode) -> None:
            if root.left:
                ans.append(root.val)
                left_boundary(root.left)
            elif root.right:
                ans.append(root.val)
                left_boundary(root.right)

        def right_boundary(root: TreeNode) -> None:
            if root.right:
                right.append(root.val)
                right_boundary(root.right)
            elif root.left:
                right.append(root.val)
                right_boundary(root.left)
            
        def leaves(root: TreeNode) -> None:
            if root.left:
                leaves(root.left)
            if root.right:
                leaves(root.right)
            if not root.left and not root.right:
                ans.append(root.val)
        
        if root.left:
            left_boundary(root.left)
        
        if root.right:
            right_boundary(root.right)
        
        if root.left or root.right:
            leaves(root)
        
        return ans + right[::-1]
        