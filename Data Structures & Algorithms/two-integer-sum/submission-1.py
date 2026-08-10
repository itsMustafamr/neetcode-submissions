class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # way 1 - for loop - brut force
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # way 2 - hashmap
        # value : index -> mapping
        # one pass rule or concept is used
        prevVal = {}

        for i, n in enumerate(nums):
        # enumerate(nums) allows you to loop over the list
        # with both the index and the value.


            diff = target - n
            if diff in prevVal:
                return [prevVal[diff], i]
            prevVal[n] = i
        return 

