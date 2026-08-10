class Solution:
    def findMin(self, nums: List[int]) -> int:
        #way 1 brutforce
        # return min(nums)

        #way 2 binary search
        # res = nums[0]
        # l, r = 0, len(nums) - 1

        # while l <= r:
        #     if nums[l] < nums[r]:
        #         res = min(res, nums[l])
        #         break

        #     m = (l + r) // 2
        #     res = min(res, nums[m])
        #     if nums[m] >= nums[l]:
        #         l = m + 1
        #     else:
        #         r = m - 1
        # return res


        # for x in nums:
        #     return min(nums)
        
        l = 0
        r = len(nums) - 1
        res = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            # this is for doing sorted case then rest for not sorted case
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1

        return res 

     
            
        