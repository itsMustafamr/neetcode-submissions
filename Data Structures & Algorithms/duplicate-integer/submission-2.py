class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # way 1
        # duplicate = set()
        # for i in nums:
        #     if i in duplicate:
        #         return True
        #     duplicate.add(i)
        # return False
        # way 2
        # nums.sort()
        # for i in range(len(nums)-1):
        #     if nums[i] == nums[i+1]:
        #         return True
        # return False
        # way 3
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    return True
        return False



        



         