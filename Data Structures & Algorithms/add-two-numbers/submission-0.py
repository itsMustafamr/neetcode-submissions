# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # if not l1 and not l2 and carry == 0:
        #     return None
        
        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry : # or you can say l1 or l2 is not null:
            v1 = l1.val if l1 else 0 # means l1 is not null else it is 0
            v2 = l2.val if l2 else 0

            #new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10 # cuz we only want the once place
            cur.next = ListNode(val)

            #update pointers
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

        