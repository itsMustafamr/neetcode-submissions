class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # L = 0
        # R = len(nums) - 1

        # while L <= R:
        #     mid = (L + R) // 2
        #     if nums[mid] < target:
        #         L = L + 1
        #     elif nums[mid] > target:
        #         R = R - 1
        #     else:
        #         return mid
    
        # return -1
        l = 0
        r = len(nums) - 1
        # binary search first we need to make sure the input is sorted

        while l <= r:
            mid = (l + r)// 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        
        return -1