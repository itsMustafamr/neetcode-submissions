# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # prev = None
        # curr = head

        # while curr != None:  #basically while curr not null
        #     temp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = temp
        # return prev

        # curr = head #initializuing curr to be first or 1st node 
        # #then while curr! pointing to null you can set curr.next = node2
        # prev = None

        # temp = curr.next

        # # curr.next (basically the pointer of cur pointing to next node)
        # # curr.next = ball (basically sets ball to be 2nd list node and cur beibng 1st)
        # #curr = ball
        # # or both command together => curr = curr.next

        prev = None
        curr = head

        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


            
    

        