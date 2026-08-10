# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        #this wont be enough
        # node.val < root
        # node.val > root

        # return True

        # else:
        #     return False

        # we do two comparisons -> -infi < x < infi

        def valid(node, left, right):
            if not node:
                return True
            
            if not (node.val < right and node.val > left):
                return False
            
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)#here node.val is the parent and parent should always be less than the right bound tree
        return valid(root, float("-inf"), float("+inf"))


