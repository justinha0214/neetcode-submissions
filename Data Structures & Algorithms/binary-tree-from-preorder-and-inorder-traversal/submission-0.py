# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # The concept behind this question is to just determine the relation between
        # the preorder and inorder arrays, using this relationship to build the new array
        # preorder = [1,2,3,4], inorder = [2,1,3,4]
        # for preorder, the first node is the root of the tree, use this to start
        # the root of the tree will always be the middle of the tree, use this 
        # in the inorder array to find what's on the left of the tree vs the right
        # establishing this mid is all that's needed, then we use recursive calls to 
        # build the tree itself.    
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root