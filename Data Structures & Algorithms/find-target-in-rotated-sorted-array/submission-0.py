class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #way 1 - brut force
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i
        
        # return -1
        #way 2 - binary search
        L = 0  
        R = len(nums) - 1
        
        while L <= R:
            mid = (L + R) // 2

            if target == nums[mid]:
                return mid

            if nums[L] <= nums[mid]:
                if target > nums[mid] or target < nums[L]:
                    L = mid + 1
                else:
                    R = mid - 1
                # elif target < nums[L]:
                #     L = mid + 1
            #right sorted portion
            else:
                if target < nums[mid] or target > nums[R]:
                    R = mid - 1
                else:
                    L = mid + 1

        return -1

                    





        