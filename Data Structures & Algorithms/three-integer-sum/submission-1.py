class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #way 1 brut force - O(n^3) 
        # seen = set()
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         for k in range(j + 1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 threenums = tuple(sorted([nums[i],nums[j],nums[k]]))
        #                 seen.add(threenums)
        # return [list(t) for t in seen]

        #way 2 - sorting + pointers
        # res = []
        # nums.sort()

        # for i, val in enumerate(nums):
        #     if i > 0 and val == nums[i - 1]:
        #         continue

        #     l, r = i + 1, len(nums) - 1
        #     while l < r:
        #         threeSum = val + nums[l] + nums[r]
        #         if threeSum > 0:
        #             r -= 1
        #         elif threeSum < 0:
        #             l += 1
        #         else:
        #             res.append([val, nums[l], nums[r]])
        #             l += 1
        #             while nums[l] == nums[l - 1] and l < r:
        #                 l += 1
        # return res
        # more clearner writing
        # res = []
        # nums.sort()

        # for i, val in enumerate(nums):
        #     if i > 0 and val == nums[i - 1]:
        #         continue  # skip duplicate first elements

        #     l, r = i + 1, len(nums) - 1
        #     while l < r:
        #         threeSum = val + nums[l] + nums[r]
        #         if threeSum < 0:
        #             l += 1
        #         elif threeSum > 0:
        #             r -= 1
        #         else:
        #             res.append([val, nums[l], nums[r]])
        #             l += 1
        #             r -= 1
        #             # skip duplicates
        #             while l < r and nums[l] == nums[l - 1]:
        #                 l += 1
        #             while l < r and nums[r] == nums[r + 1]:
        #                 r -= 1

        # return res
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]: #not to have duplicate / reuse the same value twice
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threesum = a + nums[l] + nums[r]
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        
        return res









        