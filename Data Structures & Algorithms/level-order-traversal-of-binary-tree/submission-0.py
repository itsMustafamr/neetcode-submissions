# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        #level treversal
        #root - levle 1 - level 2 
        #each levels sub list is going to put to a single big list.
        # thats the solution

        #BFS on tree and addd value to list
        # we need a queue data structure
        # adding element to the queue and poping from the start

        res = []
        q = collections.deque() #its called deck not dee queeee = how we initialize a queue
        q.append(root)

        while q:
            qlength = len(q)
            level = []
            for i in range(qlength):
                node = q.popleft()
                if node: # basically check node is not null
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)

        return res




        