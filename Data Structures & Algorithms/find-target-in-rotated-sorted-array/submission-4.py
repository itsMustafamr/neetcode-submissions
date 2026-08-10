class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #way 1 - brut force
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i
        
        # # return -1
        # #way 2 - binary search
        # L = 0  
        # R = len(nums) - 1
        
        # while L <= R:
        #     mid = (L + R) // 2

        #     if target == nums[mid]:
        #         return mid

        #     if nums[L] <= nums[mid]:
        #         if target > nums[mid] or target < nums[L]:
        #             L = mid + 1
        #         else:
        #             R = mid - 1
        #         # elif target < nums[L]:
        #         #     L = mid + 1
        #     #right sorted portion
        #     else:
        #         if target < nums[mid] or target > nums[R]:
        #             R = mid - 1
        #         else:
        #             L = mid + 1

        # return -1
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i
        
        # return -1
                    
        # l = 0
        # r = len(nums) - 1

        # while l <= r:
        #     mid = (l + r)// 2
        #     if nums[mid] < target:
        #         l = mid + 1
        #     elif nums[mid] > target:
        #         r = mid - 1
        #     elif nums[mid] == target:
        #         return mid
        # return -1

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1

            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
            




        