class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # fail
        # l, r = 0, 1
        # count = 0
        # maxP = 0

        # while r < len(s):
        #     if ord(s[l]) != ord(s[r]):
        #         count += 1
        #         maxP = max(maxP, count)
        #     else:
        #         l = r
        #         count = 0
        #     r += 1
        # return maxP 
        #brut force - O(m * n) = O(n^2)
        # res = 0
        # for i in range(len(s)):
        #     charSet = set()
        #     for j in range(i, len(s)):
        #         if s[j] in charSet:
        #             break
        #         charSet.add(s[j])
        #     res = max(res, len(charSet))
        # return res

        #window + set method - O(n)
        # charSet = set()
        # l = 0
        # res = 0

        # for r in range(len(s)):
        #     while s[r] in charSet:
        #         charSet.remove(s[l])
        #         l += 1
        #     charSet.add(s[r])
        #     res = max(res, r - l + 1) #r - l + 1 gives the current windows size
        # return res

        l = 0
        r = 1
        word = set()
        res = 0
        for r in range(len(s)):
            while s[r] in word:
                word.remove(s[l])
                l += 1
            word.add(s[r])
            res = max(res, r - l + 1)
        return res




        





        