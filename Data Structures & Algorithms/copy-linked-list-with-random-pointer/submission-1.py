"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
# we will be doing a 2 pass here
# fist we create a copy of all the nodes then we create hashmap where we map the original node
# to a new node
# in the 2nd pass we do the pointer connecting
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        otc = { None : None } # so that case were null : null is covered

        cur = head
        while cur:
            copy = Node(cur.val) # copt the current node value
            otc[cur] = copy # puting it in hashmap
            cur = cur.next

        cur = head 
        while cur: #2nd pass
            copy = otc[cur]
            copy.next = otc[cur.next]
            copy.random = otc[cur.random]
            cur = cur.next


        return otc[head]