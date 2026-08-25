class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #we can do it by sorting it - nlog(n)
        #or we can do is better by taking max heap it will be n + klogn

        # #sort answer
        # nums.sort()
        # return nums[len(nums) - k]

        # quick select ansewr
        # its average case is O(n) but worst case O(n^2)

        k = len(nums) - k

        def quickSelect(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p > k:
                return quickSelect(l, p - 1)
            elif p < k:
                return quickSelect(p + 1, r)
            else:
                return nums[p]

        return quickSelect(0, len(nums) - 1)

