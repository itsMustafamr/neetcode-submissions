class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #hashmap method
        # seen = set()
        # for i in nums:
        #     if i in seen:
        #         return i
        #     seen.add(i)
        # return -1
        #now proper way use of linked list cycle problem
        # so we basically apply alogorithm to find the cycle...ie which is duplicate
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]] # or just do fast*2 or somethign like that
            if slow == fast:
                break
            
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
