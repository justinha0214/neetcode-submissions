# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Create recursive function to check if any given subRoot is a valid BST
        def valid(node, left, right) -> bool:
            if node is None: # empty node is considered valid
                return True
            # if the node is not within bounds, we know this isn't valid
            if not (node.val > left and node.val < right):
                return False
            # Make recursive call to left and right nodes, setting the boundaries accordingly
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)
        # Make recursive call with original boundaries set to -inf and +inf
        return valid(root, float("-inf"), float("inf"))
       