# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # place = set()
        # cur = head# if next == null
        # while curr:
        #     if cur in place:
        #         return True
        #     place.add(cur)
        #     cur = cur.next
        # return False

        # a = set()
        # c = h
        # while c:
        #     if c in a:
        #         T
        #     a.add(c)
        #     c = c.next
        # return F
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
                
        return False