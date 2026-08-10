# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #BFS solution
        res = []
        q = collections.deque([root])

        #check right child and add it to the queue

        while q:
            rightside = None
            qlength = len(q) # taking at that level

            for i in range(qlength):
                node = q.popleft() #poping 
                if node:
                    rightside = node
                    q.append(node.left)
                    q.append(node.right)

            if rightside:     
                res.append(rightside.val)
        return res

