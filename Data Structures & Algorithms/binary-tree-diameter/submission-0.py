# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #recursively do DFS but that gives height. for diameter we include a global variable too.
        #basically max of subtrees + 1

        self.res = 0


        def dfs(curr): # this is base dfs but for getting height
            if not curr:
                return 0

            
            left = dfs(curr.left)
            right = dfs(curr.right)

            self.res = max(self.res, left + right)
            return 1 + max(left, right)

        dfs(root)
        return self.res


        