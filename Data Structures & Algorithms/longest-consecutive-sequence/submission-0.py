class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # way 1 - sorting
        # nums.sort()
        # longest = 1
        # curr = 1

        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i - 1]:
        #         continue  # skip duplicates
        #     elif nums[i] == nums[i - 1] + 1:
        #         curr += 1
        #         longest = max(longest, curr)
        #     else:
        #         curr = 1

        # return longest
        # way 2 - brut force
        # longest = 0
        # for num in nums:
        #     length = 1
        #     current = num
        #     while current + 1 in nums:
        #         current += 1
        #         length += 1
        #     longest = max(longest, length)
        # return longest
        #way 3 - hashset - best
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
        # way 4 - hashmap - best
        # mp = defaultdict(int)
        # res = 0

        # for num in nums:
        #     if not mp[num]:
        #         mp[num] = mp[num - 1] + mp[num + 1] + 1
        #         mp[num - mp[num - 1]] = mp[num]
        #         mp[num + mp[num + 1]] = mp[num]
        #         res = max(res, mp[num])
        # return res


